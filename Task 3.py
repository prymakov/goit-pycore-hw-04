import sys
import colorama
from pathlib import Path

def show_dir_structure(path, level=0):
    try:
        for item in path.iterdir():
            if item.is_dir():
                print("    " * level + colorama.Fore.YELLOW + colorama.Style.BRIGHT + item.name)
                show_dir_structure(item, level + 1)
            else:
                print("    " * level + colorama.Fore.GREEN + item.name)
    except PermissionError:
        print('    ' * level + colorama.Fore.RED + f"Permission denied: {path.name}")

def main():
    
    path = Path(sys.argv[1])

    if not path.exists():
        print(colorama.Fore.RED + "Вказаний шлях не існує.")
        return
    
    if not path.is_dir():
        print(colorama.Fore.RED + "Вказаний шлях не веде до папки.")
        return

    print(colorama.Fore.WHITE + f"Структура папки {path}:")
    
    show_dir_structure(path)

if __name__ == "__main__":
    main()