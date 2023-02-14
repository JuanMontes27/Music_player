import tkinter
from src.styles import BACKGROUND, APP_TITLE
from src.app_view import View

class MainScreen(tkinter.Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configure(background=BACKGROUND)

        self._create_widgets()

    def _create_widgets(self) -> None:
        '''
        Create widgets to interact with the app
        '''
        tkinter.Label(self, text='Music player', **APP_TITLE).pack(
            side=tkinter.TOP,
            fill=tkinter.BOTH,
        )

        component_content = tkinter.Frame(self)
        component_content.configure(background=BACKGROUND)
        component_content.pack(
            side=tkinter.TOP,
            fill=tkinter.BOTH,
            expand=True,
            padx=5,
            pady=5,
        )
        component_content.grid_columnconfigure(0, weight=1)
        component_content.grid_rowconfigure(0, weight=1)
        View(component_content).grid(column=0, row=0, sticky=tkinter.NSEW)
        