import pyautogui as auto

print("moving chrome....")
chrome = auto.getWindow('Google Chrome')
if chrome != None:
	chrome.restore()
	chrome.move(-1920, 0)
	chrome.maximize()

print("moving Spotify....")
spotify = auto.getWindow('Spotify')
if spotify != None:
	spotify.restore()
	spotify.move(-3500, 300)

print("moving Outlook....")
outlook = auto.getWindow('Outlook')
if outlook != None:
	outlook.restore()
	outlook.move(-3840, 0)
	outlook.resize(960, 1040)

print("moving Skype for Business....")
skypeforbusiness = auto.getWindow('Skype for Business')
if skypeforbusiness != None:
	skypeforbusiness.restore()
	skypeforbusiness.move(-3700, 200)

print("moving Fiddler....")
fiddler = auto.getWindow('Telerik Fiddler Web Debugger')
if fiddler != None:
	fiddler.restore()
	fiddler.move(-2280, 250)

print("moving Skype....")
skype = auto.getWindow('Skype')
if skype != None:
	skype.restore()
	skype.move(0, 0)
	skype.move(-2888, 492)
	skype.resize(970, 500)

print("moving HipChat....")
hipchat = auto.getWindow('HipChat')
if hipchat != None:
	hipchat.restore()
	hipchat.move(0, 0)
	hipchat.move(-2888, 492)
	hipchat.resize(970, 550)

print("moving Slack....")
slack = auto.getWindow('Slack')
if slack != None:
	slack.restore()
	slack.move(0, 0)
	slack.move(-2880, 0)
	slack.resize(960, 490)
