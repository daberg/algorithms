# Basic hanoi recursive solving

def move(src, dst):
    print("Move " + str(src) + " to " + str(dst))

def hanoi(n, src, dst, aux):

    if n == 1:
        move(src, dst)
        
    else:
        hanoi(n - 1, src, aux, dst)
        move(src, dst)
        hanoi(n - 1, aux, dst, src)

hanoi(6, 0, 1, 2)

