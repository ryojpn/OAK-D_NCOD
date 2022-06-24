import pyautogui
import re

print("解像度を出力します。")
print("------------------------------------")
s=str(pyautogui.size())
type(pyautogui.size())
result = re.compile(r"\d+").findall(s)
print(result[0])
print(result[1])
print("------------------------------------")