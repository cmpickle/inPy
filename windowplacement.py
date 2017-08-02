import pyautogui as auto

chrome = auto.getWindow('Google Chrome')
chrome.restore()
chrome.move(-1920, 0)
chrome.maximize()

hipchat = auto.getWindow('HipChat')
hipchat.restore()
hipchat.move(2280, 250)

spotify = auto.getWindow('Spotify')
spotify.restore()
spotify.move(2200, 300)

outlook = auto.getWindow('Outlook')
outlook.restore()
outlook.move(1920, 0)
outlook.maximize()

skypeforbusiness = auto.getWindow('Skype for Business')
skypeforbusiness.restore()
skypeforbusiness.move(2000, 300)

fiddler = auto.getWindow('Telerik Fiddler Web Debugger')
fiddler.restore()
fiddler.move(2280, 250)

skype = auto.getWindow('Skype')
skype.restore()
skype.move(2280, 250)

slack = auto.getWindow('Slack')
slack.restore()
slack.move(2280, 250)