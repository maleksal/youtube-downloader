from __future__ import unicode_literals

import os
import sys
import pathlib

import youtube_dl
import configparser

from tkinter import filedialog
from tkinter import *

import eel



class Youtube_Downloader():

    def __init__(self):

        # Configure
        self.download_options = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'nocheckcertificate': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        # Change Dir
        os.chdir(self.config_file()["PATH"]["OUTPUT"])

        # Song Directory
        if not os.path.exists('Songs'):
            os.mkdir('Songs')
        else:
            os.chdir('Songs')

    def config_file(self):
        #get data from config.ini
        
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'))
        return config

    def download_url_list(self, file_path):

        # Download multiple songs from list
        with youtube_dl.YoutubeDL(self.download_options) as dl:
            
            try:
                with open(file, 'r') as f:
                        for song_url in f:
                            dl.download([song_url])
                            print('\n -----------| Mp3 downloaded |-----------\n')
            except :
                print("\n[!] Check Path or URL")

                        
    def download_url(self, url):
        
        # download single song
        with youtube_dl.YoutubeDL(self.download_options) as dl:
            try:
                dl.download([url])
                print('\n -----------| Mp3 downloaded |-----------\n')
            except:
                pass
        



if __name__ == "__main__":    

    eel.init(f"{pathlib.Path(__file__).parent}/web")

    app = Youtube_Downloader()

    @eel.expose
    def js_url_download(url):
        app.download_url(url)


    @eel.expose
    def js_url_list_download(url_path):
        app.download_url_list(url_path)

    eel.start("index.html", size=(386,658))

