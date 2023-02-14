import tkinter
from src.styles import BACKGROUND
from src.screen import MainScreen
from src.functions import AppFunctions

class Manager(tkinter.Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title('Music player')

        # Create a container app
        container_app = tkinter.Frame(self)
        container_app.pack(
            side=tkinter.TOP,
            fill=tkinter.BOTH,
            expand=True,
        )

        # Configuration about responsive
        container_app.configure(background=BACKGROUND)
        container_app.grid_columnconfigure(0, weight=1)
        container_app.grid_rowconfigure(0, weight=1)

        main_scren = MainScreen(container_app)
        main_scren.grid(column=0, row=0, sticky=tkinter.NSEW)

        # Create config from app
        AppFunctions.load_settings()
        

if __name__ == '__main__':
    app = Manager()
    app.geometry('1000x700+0+0')
    app.mainloop()
