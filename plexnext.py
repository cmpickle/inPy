import pyautogui as auto

plex = auto.getWindow('Plex')
plex.restore()
plex.hotkey('ctrl', 'f')
#plex.minimize()