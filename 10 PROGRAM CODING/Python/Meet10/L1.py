num = int( (input( "Masukkan nilai ganjil diatas 20 : ")) )

while (num % 2 == 0) or ( num < 20 ) :
    #FALSE : GENAP - dibawah 20 
    num = int( (input( "Masukkan nilai ganjil diatas 20 : ")) )
    print( " Salah..." )
else:
    print( " Benar...")
