import curses


class Dialog:
    border="window" #border of the dialog window
    text="window" #smaller window rendered on top of the border
    title="string" #name field, goes on line 0 of the border
    prompt="string i guess" #fancy "you can advance text now" animation, goes on the last line of the border?


    def __init__(self, height, width, ystart, xstart):
        self.border = curses.newwin(height, width, ystart, xstart)
        self.border.box(0,0)
        self.text = curses.newwin(height-2, width-2, ystart+1, xstart+1)


    def noutrefresh(self):
        self.border.noutrefresh()
        self.text.noutrefresh()


    def show_title(self):
        self.border.box(0,0)
        self.border.addstr(0,1,self.title)


    def show_prompt(self):
        coords = self.border.getmaxyx()
        self.border.addstr(coords[0]-1,coords[1]-1-len(self.prompt), self.prompt)


