# 3 cara untuk membuat format string :
# 1. Format ( % )
# 2. Format String
# 3. f.String

umur = 17 # tp : Integer ( i/d )
nama = " Budi " # tp : String ( s )
ukuran_sepatu = 41.5 # tp : Float ( f )
# Dengan Format %
print( " Hei nama saya %s umur saya %d dan memliki ukuran sepatu %0.2f " %( nama, umur, ukuran_sepatu) )

print( "-"*15, ">Format String")
print("1.Array : Hei nama saya {0} umur saya {1} dan memiliki ukuran sepatu {2}" ,format( nama, umur, ukuran_sepatu) )

print("2.Inisial : Hei nama saya {nm} umur saya {u} dan memiliki ukuran sepatu {us}" ,format( nm = nama, u = umur, us = ukuran_sepatu) )

print( "-"*15, ">f.String")
print( f"Dengan f.String : Hei nama saya {nama} umur saya {umur} dan ukuran sepatu {ukuran_sepatu} ")