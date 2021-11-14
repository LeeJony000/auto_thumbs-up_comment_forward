import pyautogui
import time
import pyperclip


def qzone_pl():
    time.sleep(0.3)  # 等待 0.3 秒
    left, top, width, height = pyautogui.locateOnScreen('qzone_pl.png')  # 寻找评论图片；
    center = pyautogui.center((left, top, width, height))  # 寻找评论图片的中心
    pyautogui.click(center)  # 点击评论图标
    with open("qzone_pl.txt", "rb+") as f:
        byt = f.read()
        byt = byt.decode("utf-8")
        pyperclip.copy(byt)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.hotkey("ctrl", "enter")
        print("评论成功！")
        pyautogui.scroll(-1000)