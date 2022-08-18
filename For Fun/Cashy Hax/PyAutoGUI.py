# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 00:45:25 2019

@author: Kellard and Kerwin
"""
import pyautogui
import time
import pandas as pd

def error_handler():
    pyautogui.moveTo(525,930,0.5)
    pyautogui.click()
    pyautogui.moveTo(550,860,2)
    pyautogui.click()
    pyautogui.moveTo(550,720,2)
    pyautogui.click()
    time.sleep(20)
    pyautogui.moveTo(1150,840,1)
    pyautogui.click()
    pyautogui.moveTo(770,840,6)
    pyautogui.click()
    time.sleep(20)

def solve_next():
    pyautogui.moveTo(650,840,0.1)
    pyautogui.click()
    pyautogui.scroll(-2)
    pyautogui.moveTo(965,845,0.1)
    pyautogui.click()

def print_answer():
    pyautogui.moveTo(965,935,0.1)
    pyautogui.click()
    pyautogui.typewrite(sagot)
    pyautogui.typewrite(['enter'])

def copy_answer():
    pyautogui.moveTo(1000,840,0.1)
    pyautogui.click()
    pyautogui.scroll(-2)
    pyautogui.moveTo(652,840,0.1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.dragTo(767,840,0.6)
    pyautogui.hotkey('ctrl','c')

def special_copy():
    pyautogui.moveTo(1000,840,0.1)
    pyautogui.click()
    pyautogui.scroll(-2)
    pyautogui.moveTo(652,840,0.1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.dragTo(722,840,0.6)
    pyautogui.hotkey('ctrl','c')
    text = pd.read_clipboard()
    answer = int(text.columns[0])*int(text.columns[2])
    sagot = list(str(answer))
    return sagot, answer
#initialize program
time.sleep(2)
pre_answer = 0
repeat = 0

while True:
    try:
        ''' COPYING THE ANSWER '''
        copy_answer()
        text = pd.read_clipboard()
        try:
            answer = int(text.columns[0])*int(text.columns[2])
            sagot = list(str(answer))
        except:
            if text.columns[0] == 'What':
                try:
                    sagot, answer = special_copy()
                except:
                    print("Dito nag-error sa una")
                    error_handler()
            else:
                repeat+=1
                if repeat == 3:
                    print(repeat)
                    print("Dito nag-error sa pangalawa")
                    repeat = 0
                    error_handler()
                else:
                    time.sleep(3)
                    continue

        if not pre_answer == answer:
            #sets some stuff
            repeat = 0
            pre_answer = answer
            ''' PASTING THE ANSWER '''
            print_answer()
            time.sleep(15)

            ''' CLICK SOLVE NEXT '''
            solve_next()
            time.sleep(15)

        else:
            print(repeat)
            repeat+=1
            time.sleep(2)
            if repeat==3:
                print("Dito nag-error sa pangatlo")
                repeat = 0
                error_handler()
            else:
#                solve_next()
                time.sleep(8) 
    except:
        print("Dito nag-error sa pang-apat")