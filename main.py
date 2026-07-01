from tools import menu
from manager import init_db

def main():
    init_db()
    menu()

if __name__ == "__main__":
    main()