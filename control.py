import pyautogui as pg
class Control:
    def run(wait,args):
        pg.write(format(args[0],'.6f'),interval=0.01)
        pg.PAUSE=wait+0.01
        pg.press("tab")
        pg.PAUSE=0.01
        pg.write(format(args[1],'.6f'),interval=0.01)
        pg.press("tab")
        pg.press("enter")
        pg.press("tab")
        pg.press("space")
        pg.press("tab",presses=9)
    def finish():
        pg.click()
