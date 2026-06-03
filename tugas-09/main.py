from tools import display_menu, select_menu

if __name__ == '__main__':
    while True:
        display_menu()
        menu = input('Pilih menu (1-4): ')
        is_done = select_menu(menu=menu)
        if is_done:
            break