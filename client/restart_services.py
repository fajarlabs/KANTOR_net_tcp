import psutil
import os
import time
from threading import Thread
import ctypes

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_HIDE = 0

hWnd = kernel32.GetConsoleWindow()
if hWnd:
    user32.ShowWindow(hWnd, SW_HIDE)

def combytcp_exe() :
	os.chdir('C:\\Users\\spkkl batam\\Desktop\\COMbyTCP\\')
	os.system('"C:\\Users\\spkkl batam\\Desktop\\COMbyTCP\\COMbyTCP.exe"')

thread = Thread(target=combytcp_exe)

service_name = "AisSender"
s = psutil.win_service_get(service_name)
os.system("taskkill /f /pid "+str(s.pid()))
os.system("taskkill /f /IM COMbyTCP.exe")
thread.start()
os.system("net start "+service_name)