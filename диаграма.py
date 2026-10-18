from CSI import*


f=open("C:/Users/arser/Desktop/sequence.txt")
a=[float(i) for i in f]
minus=[q for q in a if -5>=q>=-10]
plus=[p for p in a if 10>=p>=5]


def draw_line(protc, color):
    line= f"{CSI}48;5;{color}m{' '*protc}{RESET}"
    return line

def draw_diagramma(kol1, kol2):
    print(str(round((kol1/(kol1+kol2)*100),2)) + str('%'),\
           draw_line(kol1,5), kol1)
    print(' ')
    print(str(round((kol2/(kol1+kol2)*100),2)) + str('%'),\
           draw_line(kol2,4), kol2)



if __name__ == "__main__":
    print(draw_diagramma(len(minus), len(plus)))
    