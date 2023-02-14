import tkinter
import src.styles as styles
from src.functions import AppFunctions

class View(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.song_name = tkinter.StringVar()
        AppFunctions.get_references(label=self.song_name)
        
        self._create_view()
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=2)
        self.configure(background=styles.BACKGROUND)


    def _create_view(self) -> None:
        '''
        Create the view of aplication
        '''
        tkinter.Button(self, text="Music folder 📁", command=AppFunctions._load_folder, **styles.BUTTONS).grid(column=0, row=0, sticky=tkinter.W)
        self.cover_image = tkinter.Label(self, text="🎵", **styles.COVER)
        self.cover_image.grid(column=0, row=1, sticky=tkinter.NSEW)
        
        songs_list = tkinter.Listbox(self, **styles.SONGS_LIST)
        songs_list.grid(column=1, row=0, rowspan=2, sticky=tkinter.NSEW)
        AppFunctions.get_references(listbox=songs_list)

        tkinter.Label(self, textvariable=self.song_name, **styles.SONG_NAME).grid(column=0, row=2, columnspan=2, sticky=tkinter.NS)
        
        button_container = tkinter.Frame(self)
        button_container.grid(column=0, row=3, columnspan=2, sticky=tkinter.NSEW)
        button_container.grid_columnconfigure(0, weight=1)
        button_container.grid_columnconfigure(1, weight=1)
        button_container.grid_columnconfigure(2, weight=1)
        tkinter.Button(
            button_container,
            text='⏮',
            command=lambda: AppFunctions.change_song('back'),
            **styles.BUTTONS).grid(
            column=0,
            row=0,
            sticky=tkinter.NSEW,
        )
        play_pasue = tkinter.Button(
            button_container, text='⏸',
            command=AppFunctions.toggle_music,
            **styles.BUTTONS)
        play_pasue.grid(
            column=1,
            row=0,
            sticky=tkinter.NSEW,
        )
        AppFunctions.get_references(button_play=play_pasue)
        tkinter.Button(
            button_container,
            text='⏭',
            command=lambda: AppFunctions.change_song('next'),
            **styles.BUTTONS).grid(
            column=2,
            row=0,
            sticky=tkinter.NSEW,
        )
