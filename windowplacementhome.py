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
	hipchat.move(-2280, 250)

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
	skype.restoe()
	skype.move(-2880, 500)
	skype.resize(980, 480)

print("moving Slack....")
slack = auto.getWindow('Slack')
if slack != None:
	slack.restore()
	slack.move(-2880, 0)
	slack.resize(960, 480)