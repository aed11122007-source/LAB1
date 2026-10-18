from CSI import *

CSI = '\x1b['
ZERO = f'{CSI}1G'
ERASE = f'{CSI}2K'
RESET = f'{CSI}0m'

def draw_line(offset, filled, color):
    offset_part = f"{CSI}48;5;7m{' '*offset}{RESET}"
    filled_part = f"{CSI}48;5;{color}m{' '*filled}{RESET}" 
    line=f'{offset_part}{filled_part}{offset_part}\
{offset_part}{filled_part}{offset_part}'
    return line


def draw_uzor(R,color):
    y=R
    while y >= -R:
        x = int((R**2 - y**2)**0.5)
        print(draw_line(R-x, x*2, color))
        y-=1
  


if __name__ == "__main__":
    print(draw_uzor(7,0))

















