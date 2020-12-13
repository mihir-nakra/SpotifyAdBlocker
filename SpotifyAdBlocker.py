from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import pyautogui
from pywinauto import Desktop
import time
rate = 3
confirmed = False
refreshRate =pyautogui.confirm(text="Choose the refresh rate (lower refresh time means it checks for ads more often)", title="Setup", buttons=[".1s", ".5s", "1s (recommended)", "3s (recommended)", "5s"])
if refreshRate == "1s (recommended)":
    rate = 1
elif refreshRate == "5s":
    rate = 5
elif refreshRate == ".5s":
    rate = .5
elif refreshRate == ".1s":
    rate = .1
elif refreshRate == None:
    quit()

while True:
    choice = pyautogui.confirm(text="Are you sure you want the refresh rate to be " + str(rate) + "s? (a low refresh rate can cause higher cpu usage)", title="Confirm", buttons=["Yes", "No", "Exit"])
    if choice == "Yes":
        break
    elif choice == None or choice == "Exit":
        quit()
    else:
        refreshRate =pyautogui.confirm(text="Choose the refresh rate (lower refresh time means it checks for ads more often)", title="Setup", buttons=[".1s", ".5s", "1s (recommended)", "3s (recommended)", "5s"])
        if refreshRate == "1s":
            rate = 1
        elif refreshRate == "5s":
            rate = 5
        elif refreshRate == ".5s":
            rate = .5
        elif refreshRate == ".1s":
            rate = .1
        elif refreshRate == None:
            quit()

windows = Desktop(backend="uia").windows()
winList = []
while True:
    windows = Desktop(backend="uia").windows()
    winList = []
    for w in windows:
        winList.append(w.window_text())
    sessions = AudioUtilities.GetAllSessions()
    if "Advertisement" in winList or "Spotify" in winList or "Spotify Free" in winList or "Click to Participate!" in winList:
        for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            if session.Process and session.Process.name() == "Spotify.exe":
                volume.SetMute(1, None)
    else:
        for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            if session.Process and session.Process.name() == "Spotify.exe":
                volume.SetMute(0, None)



    time.sleep(rate)

