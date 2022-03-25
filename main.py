#!/bin/python


import curses
from dialog import Dialog


def main(stdscr):
    dialogtest = Dialog(int(curses.LINES/2), curses.COLS, int(curses.LINES/2), 0)

    smolwin = curses.newwin(3,5,0,0)
    smolwin.box(0,0)

    dialogtest.title = "Speaker's Name"
    dialogtest.show_title()

    smolwin.noutrefresh()
    dialogtest.noutrefresh()
    curses.doupdate()

    smolwin.getch()


#code runs here
curses.wrapper(main)
