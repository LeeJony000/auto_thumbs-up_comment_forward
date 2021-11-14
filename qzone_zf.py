import pyautogui
import time


def qzone_zf():
    time.sleep(0.3)  # 等待 0.3 秒
    left, top, width, height = pyautogui.locateOnScreen('qzone_zf.png')  # 寻找转发图片；
    center = pyautogui.center((left, top, width, height))  # 寻找转发图片的中心
    pyautogui.click(center)  # 点击转发图标

    pyautogui.hotkey("ctrl", "enter")
    print("转发成功！")
    pyautogui.scroll(-1000)

    left3, top3, width3, height3 = pyautogui.locateOnScreen('qzone_cha.png')  # 寻找×图片；
    center3 = pyautogui.center((left3, top3, width3, height3))  # 寻找×图片的中心
    pyautogui.click(center3)  # 点击×图标
