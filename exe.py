import pyautogui
import re

pyautogui.FAILSAFE = False

monisize=str(pyautogui.size())
type(pyautogui.size())
result = re.compile(r"\d+").findall(monisize)
moniwid=int(result[0])
monileng=int(result[1])
print("monitor size =",moniwid,",",monileng)


def xyz(x,y,z):
    #print("X=",x)
    #print("Y=",y)
    #print("Z=",z)
    global CoordX
    global CoordY
    global CoordZ
    CoordX = x
    CoordY = y
    CoordZ = z
    if 30 <= z and z <= 120:
        pyautogui.moveTo(moniwid-((moniwid/2)+((x*50/z)*(moniwid/50))),monileng-((monileng/2)+(((y+1)*50/z)*(monileng/28))))
        return

def click():
    #print(CoordZ)

    if 30 <= CoordZ and CoordZ <= 120:
        pyautogui.click()
    return
