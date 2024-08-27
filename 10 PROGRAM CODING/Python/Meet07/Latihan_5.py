print( "<<< \t\t   TITIK KOORDINAT   \t\t >>>")

x = int ( input ( "Masukkan nilai x : " ) )
y = int ( input ( "Masukkan nilai y : ") )

if x > 0 and y > 0:
    print("kuadran 1")
elif x < 0 and y > 0:
    print("kuadran 2")
elif x < 0 and y < 0:
    print("kuadran 3")
elif x > 0 and y < 0:
    print("kuadran 4")
else:
    print("Titik Tengah")

