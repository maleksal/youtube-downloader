from __future__ import unicode_literals

import os
import sys

import youtube_dl
import configparser


def config():
    """
    get data from config.ini
    """
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'))
    return config


def downloader(url):

    # Configure
    download_options = {
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
    os.chdir(config()["PATH"]["OUTPUT"])

    # Song Directory
    if not os.path.exists('Songs'):
        os.mkdir('Songs')
    else:
        os.chdir('Songs')

    # Download Songs
    with youtube_dl.YoutubeDL(download_options) as dl:
        dl.download([url])




if __name__ == "__main__":    
    
    try:
        url = str(sys.argv[1])
    except:
        print(" usage : download -U (for url) <url> ")

        sys.exit()
    
    downloader(url)
    



    

