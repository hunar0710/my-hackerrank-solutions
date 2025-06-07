def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        dec   = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexa  = hex(i)[2:].upper().rjust(width)
        bina  = bin(i)[2:].rjust(width)
        print(dec, octal, hexa, bina)

