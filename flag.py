from CSI import *


def draw_line(white1, blue, white2):
    white1_part = f"{CSI}48;5;7m{' '*white1}{RESET}"
    blue_part = f"{CSI}48;5;4m{' '*blue}{RESET}"
    white2_part = f"{CSI}48;5;7m{' '*white2}{RESET}"
    line = f"{white1_part}{blue_part}{white2_part}"
    return line

def draw_flag(size=0):
    while size<11:
        if size<3:
            print(draw_line(5,3,10))
            size+=1
        elif 7>size>3:
            print(draw_line(0,18,0))
            size+=1
        else:
            print(draw_line(5,3,10))
            size+=1




if __name__ == "__main__":
    print(draw_flag(0))

























