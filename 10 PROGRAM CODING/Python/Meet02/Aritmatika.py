'''
Aritmatika Python :
1. + ( Penjumlahan )
2. - ( Pengurangan )
3. * ( Perkalian )
4. / ( Pembagian )
5. ** ( Pangkat )
6. % ( Modulus )
7. // ( Floor Division - Hasil bagi)
'''

a = 4
b = 2

#Penjumalahan
Hasil = a + b
print( a, " + ", b, " = ", Hasil)

#Pengurangan
Hasil = a - b
print( a, " - ", b, " = ", Hasil)

#Perkalian
Hasil = a * b
print( a, " * ", b, " = ", Hasil)

#Pembagian
Hasil = a / b
print( a, " / ", b, " = ", Hasil)

#Modulus
Hasil = a % b 
print( a, " % ", b, " = ", Hasil)

#Floor Divison
Hasil = a // b
print( a, " // ", b, " = ", Hasil)

'''
Prioritas Operasi Aritmatika :
1. ()
2. **
3. * / % //
4. + -
'''
x = 4
y = 5
z = 6

Hasil = x * ( y - z )
print( " x * ( y - z ) = ", Hasil)

Hasil = ( x + y ) // ( z - x ) ** x
print( " ( x + y ) // ( z - x ) ** x = ", Hasil)