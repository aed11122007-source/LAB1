from CSI import*

CSI = '\x1b['
ZERO = f'{CSI}1G'
ERASE = f'{CSI}2K'
RESET = f'{CSI}0m'


import time

def draw_line(offset, len, rust):
    offset_part = f"{' '*offset}"
    strela_part = f"{'-'*len}{'>'}"
    rust_part = f"{' '*rust}"
    line = f"{offset_part}{strela_part}{rust_part}{'|'}"
    return line

def draw_anim(kol_cadrs):
    rus=kol_cadrs
    offs=0 
    while rus!=-1:
        print(f"{ZERO}{ERASE}{ draw_line(offs,5,rus)}",
              end='',
              flush = True)
        if rus != 0:
            rus -= 1
            offs += 1
        else:
            rus = kol_cadrs
            offs = 0
        time.sleep(0.1)

 
if __name__ == '__main__':
    print(draw_anim(4))








