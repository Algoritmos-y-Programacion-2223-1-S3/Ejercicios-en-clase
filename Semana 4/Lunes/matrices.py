def main():
    a = [
        (1, 2, 3),
        (4, 5, 6)
        ]
    b = [
        (-1, 0),
        (0, 1),
        (1, 1)
        ]
    aux = 0
    for i in range(len(a)):
        for j in range (len(a[i])):
            for k in range(b):
                aux += a[i][j]




main()