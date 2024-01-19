from tkinter import *
# class Bida9:
#     def __init__(self, color):
#         self

class DamaBoard:
    def __init__(self, dama):
        self.dama = dama
        self.dama.title("DAMA")
        self.state = [[0, 3, 0, 3, 0, 3, 0, 3],
                      [3, 0, 3, 0, 3, 0, 3, 0],
                      [0, 3, 0, 3, 0, 3, 0, 3],
                      [1, 0, 1, 0, 1, 0, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0, 1],
                      [2, 0, 2, 0, 2, 0, 2, 0],
                      [0, 2, 0, 2, 0, 2, 0, 2],
                      [2, 0, 2, 0, 2, 0, 2, 0]]
        self.set_up()
    # def focus(self):
    #     self.focus_set()
    def get_cord(self,but):
        self.info = but.grid_info()
        self.row, self.column = self.info['row'], self.info['column']
        return (self.row, self.column)
    def set_up(self):
        self.bouto = [[None]*8 for _ in range(8)]
        for i in range(8):
            for j in range(8):
                color = "white" if (i + j) % 2 == 0 else "black" 
                bida9 = self.state[i][j]
                if (i + j) % 2 == 0:
                    self.bouto[i][j] = Button(self.dama, width=8, height=4, bg=color, state=DISABLED)
                else:
                    if i <= 2:
                        self.bouto[i][j] = Button(self.dama, text="O", fg="white", width=8, height=4,
                                                  bg=color, command=lambda: self.click(self.get_cord(self.bouto[i][j])))
                    elif i >= 5:
                        self.bouto[i][j] = Button(self.dama, text="X", fg="white", width=8, height=4,
                                                  bg=color, command=lambda: self.click(self.get_cord(self.bouto[i][j])))
                    else:
                        self.bouto[i][j] = Button(self.dama, width=8, height=4,
                                                  bg=color, command=lambda: self.click(self.get_cord(self.bouto[i][j])))    
                self.bouto[i][j].grid(row = i, column = j)
    def click(self, cliced_but_cor):
        print(cliced_but_cor[0], cliced_but_cor[1])
        if self.state[cliced_but_cor[0] + 1][cliced_but_cor[1] - 1] == 1 or self.state[cliced_but_cor[0] + 1][cliced_but_cor[1] + 1] == 1:
            self.bouto[cliced_but_cor[0] + 1][cliced_but_cor[1] - 1] = Button(self.dama, text="1", width=14, height=7, bg="#a0ebff")
            self.bouto[cliced_but_cor[0] + 1][cliced_but_cor[1] + 1] = Button(self.dama, text="1", width=14, height=7, bg="#a0ebff")
dama = Tk()
game = DamaBoard(dama)

dama.mainloop()
