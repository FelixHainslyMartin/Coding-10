# Function / Method : Blok code yang berisi task tertentu, yang dapat digunakan berulang-ulang.
#Struktur Function:
#def FunctionalName():
#   bodyFunction
def heii():
    print( "Heiii kelas 10 coding" ) 
    print( "Belajar di hari rabu" ) 
    print( "Heiii kelas 10 coding" ) 
    print( "Heiii kelas 10 coding" ) 
heii()
heii()
def batas():
    print( "-"*25 )
batas()
#Function yang memiliki argument 
#struktur:
#def FunctionName( argument ):
#   bodyFunction
def bahasa_asing( ba ):
    print( f"Belajar di bahasa asing ( { ba } )")
bahasa_asing( "coding" )
batas()
def member_coding( siswa ):
    dt_siswa = siswa.copy()
    no = 1
    for i in dt_siswa:
        print ( f" { no }, { i } " )
        no += 1
dt_list = [ "felix", "albert", "vino" ]
member_coding( dt_list )
batas()
#multi argument:
def siswa( nama, kelas, ba ):
    print( f"nama saya { nama } di kelas { kelas } belajar di { ba }" )
siswa ( "albert", "x.1", "coding" )
batas()
def plus3 ( num_1, num_2, num_3 ):
    print ( f" {num_1} + { num_2 } + { num_3 } + { num_1+num_2+num_3 } ")
plus3( 1, 2, 3 )
batas()
# function yang memiliki return / kembalian
def pangkat( angka, pangkat ):
    hasil = angka ** pangkat
    return hasil
print( f" hasil pangkat = { pangkat( 4, 2 ) + 6 }")
batas()
def aritmatika( num_1, num_2 ):
    tambah = num_1 + num_2
    kurang = num_1 - num_2
    kali = num_1 * num_2
    


