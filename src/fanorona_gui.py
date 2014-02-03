import tkinter as tk

BACKGROUND_COLOR = '#FFFFFF'
LINE_COLOR = '#212121'

CELL_SIDELENGTH = 80


class FanoronaGUI(object):
    def __init__(self, state):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(master=self.window,
                                width=720,
                                height=400,
                                background=BACKGROUND_COLOR)

        # Generate grid
        for i in range(1, 9):
            self.canvas.create_line(CELL_SIDELENGTH*i, 0, CELL_SIDELENGTH*i, 400, fill=LINE_COLOR)

        for i in range(1, 5):
            self.canvas.create_line(0, CELL_SIDELENGTH*i, 720, CELL_SIDELENGTH*i, fill=LINE_COLOR)

        # Bind event handlers
        self.canvas.bind('<Button-1>', self._on_button_click)

        self.canvas.pack()

    def run(self):
        self.window.mainloop()

    def _on_button_click(self, event: tk.Event) -> None:
        pass


if __name__ == '__main__':
    gui = FanoronaGUI(None)
    gui.run()
