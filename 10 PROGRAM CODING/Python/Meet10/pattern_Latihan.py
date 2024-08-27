print (" Belah Ketupat : ")

i = 0
space = 9
while True:
    if i ==20:
        break
    elif i % 2 :
        print(f" "* space, "+"*i)
        space -= 1
    i += 1
i = 18
space = 1
while True:
    if i ==0:
        break
    elif i % 2 :
        print(f" "* space, "+"*i)
        space += 1
    i -= 1

print (" Kupu-kupu : ")

for i in range(10):
    x = "+" * i
    print(f"{x:<9}{x:>9}")
for i in range(9):
    x = "+" * (9 - i)
    print(f"{x:<9}{x:>9}")
