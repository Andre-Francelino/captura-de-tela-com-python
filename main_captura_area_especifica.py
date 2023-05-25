import pyautogui

screenshot = pyautogui.screenshot(region=(1, 25, 500, 300))
screenshot.save('screenshot de area especifica.png')
