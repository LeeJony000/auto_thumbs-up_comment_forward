import pyautogui
import time


def qzone_zan():
    time.sleep(0.3)    # 等待 0.3 秒
    left, top, width, height = pyautogui.locateOnScreen('qzone_zan.png')   # 寻找点赞图片；
    center = pyautogui.center((left, top, width, height))    # 寻找点赞图片的中心
    pyautogui.click(center)    # 点击点赞图标
    print('点赞成功！')