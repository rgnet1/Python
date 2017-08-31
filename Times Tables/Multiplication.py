w, h = 11, 11;
print("HI\n")
math = [[1 for x in range(w)] for y in range(h)]
for r in range (1,10):
    for c in range(1,10):
        math[r][c] = r * c
        print(math[r][c], end =" ")
    print("\n")
