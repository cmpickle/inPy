import pyautogui as auto

print("moving chrome....")
chrome = auto.getWindow('Google Chrome')
if chrome != None:
	chrome.restore()
	chrome.move(-1920, 0)
	chrome.maximize()

print("moving HipChat....")
hipchat = auto.getWindow('HipChat')
if hipchat != None:
	hipchat.restore()
	hipchat.move(2280, 250)

print("moving Spotify....")
spotify = auto.getWindow('Spotify')
if spotify != None:
	spotify.restore()
	spotify.move(2200, 300)

print("moving Outlook....")
outlook = auto.getWindow('Outlook')
if outlook != None:
	outlook.restore()
	outlook.move(1920, 115)
	outlook.resize(960, 1040)

print("moving Skype for Business....")
skypeforbusiness = auto.getWindow('Skype for Business')
if skypeforbusiness != None:
	skypeforbusiness.restore()
	skypeforbusiness.move(2000, 300)

print("moving Fiddler....")
fiddler = auto.getWindow('Telerik Fiddler Web Debugger')
if fiddler != None:
	fiddler.restore()
	fiddler.move(2280, 250)

print("moving Skype....")
skype = auto.getWindow('Skype')
if skype != None:
	skype.restore()
	skype.move(2872, 635)
	skype.resize(980, 520)

print("moving Slack....")
slack = auto.getWindow('Slack')
if slack != None:
	slack.restore()
	slack.move(2880, 115)
	slack.resize(960, 520)
