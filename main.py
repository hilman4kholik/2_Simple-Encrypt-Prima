def enPrima(plaintext):
    key = ['1Z', '2D', '3F', '4C', '4B', '5D', '6G', '7J', '8L', '8W', '9W', '1Q', '4H',
           '5K', '3D', '2F', '1D', '1B', '1A', '2G', '3M', '4D', '6D', '6H', '7F', '7D', '12', '55', '34', '77', '65', '88', '87', '85', '90', '09', '07', '21', '23', '28', '29', '20', '39', '80', '84', '78', 'B1', 'D1', 'C1', 'F1', 'G1', 'R1', 'U1', 'A1', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'B3', 'C3', 'D3', 'F3', 'G3', 'B4', 'C4', 'D4', 'F4', 'G4', 'B5', 'C5']
    alphabet = "[]abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chipertext = ""
    prima = 173
    enkrip = ""
    for ch in plaintext:
        idx = alphabet.find(ch)
        if len(str(idx)) == 2:
            chipertext = chipertext + "1" + str(idx)
        else:
            chipertext = chipertext + str(idx)
    try:
        r = int(chipertext) + prima
        for x in str(r):
            enkrip = enkrip + key[int(x)]
        return str(enkrip)
    except ValueError:
        return "Tidak bisa di enkrip"

if __name__ == "__main__":
    print(enPrima("encryptthis"))
    print(enPrima("encrypt this"))