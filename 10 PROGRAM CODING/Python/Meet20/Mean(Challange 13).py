print( f""*10, "NILAI MEAN", ""*10)

import os

def mean(*args):
    total = sum(args)
    banyak = len(args)
    if banyak == 0:
        return 0
    return total / banyak

def main():
    numbers = []
    while True:
        num_input = input("Masukkan angka : ")
        if num_input.replace('.', '', 1).isdigit(): 
            num = int(num_input)
            numbers.append(num)
        
        lanjut = input("Lanjut(y/n): ")
        if lanjut.lower() != 'y':
            break
        os.system('cls' if os.name == 'nt' else 'clear')
        print( f""*10, "NILAI MEAN", ""*10)
    if numbers:
        avg = mean(*numbers)
        os.system('cls' if os.name == 'nt' else 'clear')
        print( f""*10, "NILAI MEAN", ""*10)
        print(f"Hasil mean dari data: {numbers} = {avg:.2f}")

main()
