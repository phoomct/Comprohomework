""" caesarCipher """
def main():
    """ Write an encoder/decoder program based on the idea of shifting each
    character to the right hand side (for encoder)
    with a fixed number or key value where the order of characters is upper case, space and
    lower case characters.
    The program will do the shifting in circular fashion: meaning, the next character after
    the last one 'z' is the first character 'A' as '...xyzABC...XYZ abc...'
    For example, with the input message 'ABCDabcd' and key = 5, we will get the encoded message as
    'FGHIfghi'. Moreover, for decoding, we will use the negative of the key such as
    the input message 'SAAplXGow'
    and key = -12, we will get the encoded message as 'Good Luck'"""
    character = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"
    chara = input()
    passs = int(input())
    for i in range(len(chara)):
        charaa = character.find(chara[i])
        skip = charaa + passs
        caesarcipher = skip % 53
        print(character[caesarcipher], end="")
main()
