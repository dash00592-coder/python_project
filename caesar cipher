print("welcome to caesar cipher")
print ('''  ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗     ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
 ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗   ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
 ██║     ███████║█████╗  ███████╗███████║██████╔╝   ██║     ██║██████╔╝███████║█████╗  ██████╔╝
 ██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗   ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
 ╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║██╗╚██████╗██║██║     ██║  ██║███████╗██║  ██║
  ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ''')


uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode():
    string = input("enter the text ")
    str_list = list(string)
    move = int(input("enter the number to shift"))
    encrypt = []
    for i in str_list:
        if i in lowercase_letters:
            z = lowercase_letters.index(i)
            net_shift = z + move
            if net_shift >= 26:
                net_shift = z + move - 26
            else:
                net_shift = z + move
            encrypt.append(lowercase_letters[net_shift])
        elif i in uppercase_letters:
            z_1 = uppercase_letters.index(i)
            net_shift_1 = z_1 + move
            if net_shift_1 >= 26:
                net_shift_1 = z_1 + move - 26
            else:
                net_shift_1 = z_1 + move
            encrypt.append(uppercase_letters[net_shift_1])
        else:
            encrypt.append(i)   
    print("Encrypted text:", "".join(encrypt))


def decode():
    string = input("enter the text ")
    str_list = list(string)
    move = int(input("enter the number to shift"))
    decrypt = []
    for i in str_list:
        if i in lowercase_letters:
            z = lowercase_letters.index(i)
            net_shift = z - move
            if net_shift < 0:
                net_shift = 26 + (z - move)
            else:
                net_shift = z - move
            decrypt.append(lowercase_letters[net_shift])
        elif i in uppercase_letters:
            z_1 = uppercase_letters.index(i)
            net_shift_1 = z_1 - move
            if net_shift_1 < 0:
                net_shift_1 = 26 + (z_1 - move)
            else:
                net_shift_1 = z_1 - move
            decrypt.append(uppercase_letters[net_shift_1])
        else:
            decrypt.append(i)   # preserve spaces, punctuation, numbers
    print("Decrypted text :", "".join(decrypt))


choice = input("select encode or decode ").lower()
if choice == "encode":
    encode()
elif choice == "decode":
    decode()
else:
    print("type a valid option")
