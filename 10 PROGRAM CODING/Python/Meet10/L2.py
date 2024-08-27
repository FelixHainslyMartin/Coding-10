num = int ( input(" Masukkan nilai 10 - 15 atau nilai 20 - 25 atau 35 - 40 :") )

a = num > 10 and num < 15
b = num > 20 and num < 25
c = num > 35 and num < 40

while not( a or b or c) :
    num = int ( (input(" Masukkan nilai 10 - 15 atau nilai 20 - 25 atau 35 - 40")) )
else:
    print( "True.." )