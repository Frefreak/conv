#!/usr/bin/env python3

import argparse
import sys
import utils

import PySimpleGUI as sg

sg.theme('SystemDefaultForReal')
ttk_style = 'winnative'

file_browse = sg.FileBrowse(size=(10, 1), key="in")
layout = [  [sg.Input(), file_browse],
            [sg.Button('Ok', use_ttk_buttons=True)] ]

window = sg.Window('ffmpeg', layout, ttk_theme=ttk_style)

def main():
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Ok':
            try:
                r, err = utils.conv_audio_mp3(values['in'])
                if err is None:
                    sg.SystemTray.notify("conversion ok", r)
                else:
                    sg.SystemTray.notify("conversion failed", err)
            except Exception as e:
                    sg.SystemTray.notify("conversion failed", str(e))


    window.close()
if __name__ == "__main__":
    main()
