import pyautogui
import time
import pyperclip
import sys
from qzone_zan import qzone_zan
from qzone_pl import qzone_pl
from qzone_zf import qzone_zf

if __name__ == "__main__":
    a = pyautogui.prompt("请输入功能所对应的标号：\n1:点赞\r2:评论\r3:转发\n4:点赞+评论\r5:点赞+转发\r6:点赞+评论+转发\n转发功能不稳定，等待后续维护")
    if a == '1':
        while True:
            if pyautogui.locateOnScreen("qzone_zan.png"):
                qzone_zan()
            else:
                pyautogui.scroll(-700)
                print("没有找到目标，屏幕下滚~")
    elif a == '2':
        while True:
            if pyautogui.locateOnScreen("qzone_pl.png"):
                qzone_pl()
            else:
                pyautogui.scroll(-700)
                print("没有找到目标，屏幕下滚~")
    elif a == '3':
        while True:
            if pyautogui.locateOnScreen("qzone_zf.png"):
                qzone_zf()
            else:
                pyautogui.scroll(-700)
                print("没有找到目标，屏幕下滚~")
    elif a == '4':
        while True:
            if pyautogui.locateOnScreen("qzone_zan.png"):
                qzone_zan()
            elif pyautogui.locateOnScreen("qzone_pl.png"):
                qzone_pl()
            else:
                pyautogui.scroll(-700)
                print("没有找到目标，屏幕下滚~")
    elif a == '5':
        while True:
            if pyautogui.locateOnScreen("qzone_zan.png"):
                qzone_zan()
            elif pyautogui.locateOnScreen("qzone_zf.png"):
                qzone_zf()
            else:
                pyautogui.scroll(-700)
                print("没有找到目标，屏幕下滚~")
    elif a == '6':
        while True:
            if pyautogui.locateOnScreen("qzone_zan.png"):
                qzone_zan()
            elif pyautogui.locateOnScreen("qzone_pl.png"):
                qzone_pl()
            elif pyautogui.locateOnScreen("qzone_zf.png"):
                qzone_zf()
            else:
                pyautogui.scroll(-700)
                print("没有找到目标，屏幕下滚~")
    else:
        sys.exit()
