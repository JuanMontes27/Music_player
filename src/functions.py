'''
Python script to control app
'''
import tkinter
import os
import json
from tkinter import filedialog
from pathlib import Path
from pygame import mixer

class AppFunctions:
    _music_list = {}
    _music_listbox_ref = None
    _song_name_ref = None
    _play_button_ref = None
    _root_directory = Path(__file__).parent
    mixer.init()

    @classmethod
    def load_settings(cls) -> None:
        '''
        Create file to save some configurations about the
        music player
        '''
        json_file = os.path.join(cls._root_directory, 'config.json')
        # Case 1: Create json file if it not exist
        if not os.path.exists(json_file):
            content_json = json.dumps({
                'path': '',
            })
            with open(json_file, 'w') as file:
                file.write(content_json)
            return
        with open(json_file, 'r') as file:
            content = json.loads(file.read())
            cls._load_folder(path=content['path'])

    @classmethod
    def _save_path(cls, path:str) -> None:
        '''
        Save music folder path in a file json

        :param path: Music folder path
        :type path: str
        '''
        json_file = os.path.join(cls._root_directory, 'config.json')
        content_json = json.dumps({
                'path': f'{path}',
            })
        with open(json_file, 'w') as file:
            file.write(content_json)

    @classmethod
    def get_references(cls, listbox: tkinter.Listbox=None, label: tkinter.Label=None, button_play: tkinter.Button=None) -> None:
        '''
        Create reference of music listbox, label, buttons
        '''
        if listbox:
            cls._music_listbox_ref = listbox
            cls._music_listbox_ref.bind("<<ListboxSelect>>", lambda e: cls._play_selected_song(None))
        if label: cls._song_name_ref = label
        if button_play: cls._play_button_ref = button_play

    @classmethod
    def _show_music(cls, songs: list) -> None:
        '''
        Show the music into folder selected

        :param songs: List with the path of the songs
        :type songs: list
        '''
        songs_in_list = cls._music_listbox_ref.index('end')
        for item in range(songs_in_list):
            cls._music_listbox_ref.delete(item, tkinter.END)
        if not songs:
            cls._music_listbox_ref.insert(0, 'There are any song in this folder')
            return
        names_songs = []
        for i, song in enumerate(songs):
                cls._music_list.setdefault(i, song)
                names_songs.append(str(song.name).replace('.mp3', ''))
        cls._music_listbox_ref.insert(tkinter.END, *names_songs)


    @classmethod
    def _load_folder(cls, path:str=None) -> None:
        '''
        Select music folder

        :param path: Path from musci folder
        :type path: str
        '''
        directory = filedialog.askdirectory(title='Select music folder:') if path is None else path
        if not directory: return
        music_directory = Path(directory)
        cls._save_path(music_directory)
        songs = sorted([song for song in music_directory.glob('*.mp3')])
        cls._show_music(songs)

    @classmethod
    def _play_selected_song(cls, song_num:int=None) -> None:
        '''
        Play song and set on the cover

        :param song_num: Number (index) the song
        :type song_num: int
        '''
        song_index = cls._music_listbox_ref.curselection()
        if not song_index: return
        cls._song_name_ref.set(cls._music_listbox_ref.get(song_index[0]))
        name_song = cls._music_list[song_index[0]] if song_num is None else cls._music_list[song_num]
        try:
            mixer.music.unload()
            mixer.music.load(name_song)
            mixer.music.play()
        except Exception as e:
            print(f'Algo a sucdido -> {e}')


    @classmethod
    def toggle_music(cls) -> None:
        '''
        Play and pause the song current
        '''
        if mixer.music.get_busy():
            mixer.music.pause()
            cls._play_button_ref.configure(text="▶")
        else:
            mixer.music.unpause()
            cls._play_button_ref.configure(text="⏸")


    @classmethod
    def change_song(cls, action:str):
        '''
        Change the next song
        '''
        current_song = cls._music_listbox_ref.curselection()
        if not current_song: return
        if action == "back" and current_song[0] == 0: return
        if action == "next" and current_song[0] == len(cls._music_list) - 1: return
        cls._music_listbox_ref.select_clear(0, tkinter.END)
        pos = current_song[0] + 1 if action == "next" else current_song[0] - 1
        cls._music_listbox_ref.activate(pos)
        cls._music_listbox_ref.selection_set(pos, None)
        cls._play_selected_song(pos)
        cls._play_button_ref.configure(text="⏸")


if __name__ == '__main__':
    AppFunctions.create_config()
