import pyautogui as pg


class Control:
    def run(wait, args):
        pg.write(format(args[0], '.6f'))
        pg.PAUSE = wait
        pg.press("tab")
        pg.PAUSE = 0
        pg.write(format(args[1], '.6f'))
        pg.press("tab")
        pg.press("enter")
        pg.press("tab")
        pg.press("space")
        pg.press("tab", presses=9)

    def finish():
        pg.click()
