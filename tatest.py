from pywinauto.application import Application

app = Application().connect(title="TestArchitect™")

app.TestArchitect.send_keys('{VK_MENU}')