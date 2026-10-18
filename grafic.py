from CSI import *

def draw_line(offset, grafic):
    offset_part = (f"{' '}*offset")
    y_part = (f"{'|'}")
    x_part = (f"{'0___1___2___3___4___5___6___7___8___9___10______'}")
    grafic_part = (f"{'*'}*grafic")

    line = f"{y_part}{input}{offset_part}{grafic_part}{offset_part}"
    return line


'''y=x/2'''
def draw_grafic(kol_y): 
    y=kol_y*4
    print('^ y')
    while y!=-0:
        x=y*2
        if y%4==0:
            print(f"{'|'}{y//4}{' '*(x-2)}{'+'}")
        else:
            print(f"{'|'}{' '*(x-1)}{'+'}")
        y -= 1
        
        if y==0:
            print(f"{'0___1___2___3___4___5___6___7___8___9___10_____>x'}")






if __name__ == "__main__":
     print(draw_grafic(3))












