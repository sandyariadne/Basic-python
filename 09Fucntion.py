
def sayhi():
    print("Hallo co")

sayhi()


def sayyu(name, age):
    print("Yuhuu " + name + ", you are " + str(age))

sayyu("Coy", 12)
sayyu("cuy", 14)

def tambah(i1, i2):
    result = i1 + i2
    result2 = result * result
    return result, result2
coba = tambah(4,1)
print(str(coba))
print(tambah(4,1))
def balok(p, l, t):
    luas = p * l
    volume = p * l * t
    print("luas = " + str(luas))
    print("volume = " + str(volume))
balok(2, 2, 2)

def angka (angka1):
        if int(angka1)%2 == 0:
            return str(angka1) + "is even number"
        else:
            oddnumber = str(angka1) + "is odd number"
            return  oddnumber
print(angka(3))


