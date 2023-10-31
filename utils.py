import curses


def menu(title, classes):
    def character(stdscr, ):
        attributes = {}

        bc = curses.COLOR_BLACK

        # make the 'normal' format
        curses.init_pair(1, 7, bc)
        attributes['normal'] = curses.color_pair(7)

        # make the 'highlighted' format
        curses.init_pair(2, 1, bc)
        attributes['highlighted'] = curses.color_pair(2)

        # handle the menu
        c = 0
        option = 0
        while c != 10:
            stdscr.erase()

            # add the title
            stdscr.addstr(f"{title}\n", curses.color_pair(1))

            # add the options
            for i in range(len(classes)):
                if i == option:
                    attr = attributes['highlighted']
                else:
                    attr = attributes['normal']

                stdscr.addstr(f'> ', attr)
                stdscr.addstr(f'{classes[i]}' + '\n', attr)
            c = stdscr.getch()

            if c == curses.KEY_UP and option > 0:
                option -= 1
            elif c == curses.KEY_DOWN and option < len(classes) - 1:
                option += 1
        return option

    return curses.wrapper(character)
