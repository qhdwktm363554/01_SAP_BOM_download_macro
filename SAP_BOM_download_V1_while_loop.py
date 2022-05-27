import pandas as pd
import os, glob, time, pyautogui
import sys
from datetime import datetime
import ctypes


CURRENT_DIR = os.getcwd()



completed = 2
print(MLFB_len)

time.sleep(1.0)
pyautogui.press('enter')

# EXCEL_FILE_NAMES = glob.glob(os.path.join(CURRENT_DIR, '*.xls'))
EXCEL_FILE_NAMES = glob.glob('*.xls')
print(EXCEL_FILE_NAMES)
# if MLFB not in EXCEL_FILE_NAMES: break
# else: 

    


# if msg == 1: 
#     print("ok")






# try:
#     while True: 
#         while True: 
#             if keyboard.is_pressed('F3'):
#                 a0 = pyautogui.locateCenterOnScreen('a0_activeSAP.PNG')
#                 pyautogui.moveTo(a0)
#                 pyautogui.click()

list = os.path.join(CURRENT_DIR,'00_BOM_LIST.xlsx')
df = pd.read_excel(list)
df = pd.read_ex               
count = 0
MLFB_len = len(df)

try:

    for i in df['MLFB'].index:
        # df['MLFB'].index로 loc 이용해서 mlfb name을 얻는다.
        MLFB = df.loc[i, 'MLFB']
        print(MLFB)
        # BOM이름 넣어서 실행한다.
        a = pyautogui.locateCenterOnScreen('a_material.png')
        pyautogui.moveTo(a)
        pyautogui.moveRel(350, 0)
        pyautogui.click()
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')
        pyautogui.keyUp('ctrl')

        pyautogui.typewrite(MLFB)

        # b = pyautogui.locateCenterOnScreen('b_execute.png')
        # pyautogui.moveTo(b)
        # pyautogui.click()
        pyautogui.press('f8')
        time.sleep(2.5)

        # ALT+Y+T+A+I 누름 / down 누르고 enter까지
        pyautogui.keyDown('alt')
        pyautogui.press('y')
        pyautogui.press('t')
        pyautogui.press('a')
        pyautogui.press('i')
        pyautogui.keyUp('alt')
        time.sleep(2)
        pyautogui.press('down')
        pyautogui.typewrite(['enter'])
        time.sleep(2)

        # current_directory 입력하고
        # directory는 그냥 먼저 입력하고 시작하기 위해서 그냥 아래 코드 생략함
        # c = pyautogui.locateCenterOnScreen('c_Directory.png')
        # pyautogui.moveTo(c)
        # pyautogui.moveRel(350, 0)
        # pyautogui.click()
        # pyautogui.keyDown('ctrl')
        # pyautogui.press('a')
        # pyautogui.keyUp('ctrl')
        # pyautogui.typewrite(CURRENT_DIR)
        # pyautogui.click()
        # time.sleep(1.5)

        # file_name 입력해서 enter key 누름
        d = pyautogui.locateCenterOnScreen('d_Filename.png')
        pyautogui.moveTo(d)
        pyautogui.moveRel(350, 0)
        pyautogui.click()
        pyautogui.keyDown('ctrl')
        pyautogui.press('left')
        pyautogui.keyUp('ctrl')

        pyautogui.typewrite(MLFB)

        time.sleep(0.5)
        pyautogui.typewrite(['enter'])
        time.sleep(3)
        print(MLFB, " is completed")

        # 처음으로 돌아간다
        e = pyautogui.locateCenterOnScreen('e_go_back.png')
        pyautogui.moveTo(e)
        pyautogui.click()
        time.sleep(2)
        count += 1
        msg = ctypes.windll.user32.MessageBoxW(None, '{}/{}'.format(count, MLFB_len), "Download Status", 0)     # down 받은 MLFB 수 check 

        

except KeyboardInterrupt:
    sys.exit()
print("All_finished")

# 아래는 stackoverflow에 물어본건데 아래꺼 설치하고 mouse를 upper-left corner로 움직이면 error 내면서 프로그램이 멈춘다.
# import sys
#
# try:
#     # all your code
# except KeyboardInterrupt:
#     sys.exit()
#  git test 용