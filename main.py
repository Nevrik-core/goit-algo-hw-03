import argparse
from pathlib import Path
import shutil

def parse_argv():
    parser = argparse.ArgumentParser(description="Копіює та сортує файли за розширенням.")
    parser.add_argument("-s", "--source", type=Path, required=True, help="Шлях до вихідної директорії")
    parser.add_argument("-o", "--output", type=Path, default=Path("dist"), help="Шлях до директорії призначення")
    return parser.parse_args()

def recursive_copy_and_sort(source: Path, output: Path):
    for item in source.iterdir():
        if item.is_dir():
            recursive_copy_and_sort(item, output)
        else:
            extension = item.suffix[1:]  
            folder = output / extension 
            folder.mkdir(exist_ok=True, parents=True)
            shutil.copy(item, folder)

def main():
    args = parse_argv()
    recursive_copy_and_sort(args.source, args.output)

if __name__ == "__main__":
    main()
