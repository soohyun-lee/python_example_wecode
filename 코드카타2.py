# reverse 함수 안에 인자를 뒤집어서 return

def reverse(x):
    if int(x) < 0:
        k = abs(int(x))
        k = int(str(k)[::-1])
        return -k
    if int(x) >= 0:
        return int(str(x)[::-1])