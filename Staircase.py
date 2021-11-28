def staircase(n):
    for i in range(1,n+1):
        print('{:>{}}'.format(('#'*i),n))


if __name__ == '__main__':
    n = input("enter n:").strip()
    staircase(int(n))