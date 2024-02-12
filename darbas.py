kintamasis = 1
kintamasis = 2

def funkcija ():
    print(kintamasis)
    print(kintamasis2)
    print(f'test:{kintamasis}{kintamasis2}')
    print(f'test{kintamasis}{kintamasis2}')
    print('test:{}{}'.format{kintamasis2, kintamasis})

#komentaras


def add (kintamasis1, kintamasis2):
    return kintamasis1 + kintamasis2

def subtract (kintamasis1, kintamasis2):
    return kintamasis1 - kintamasis2

def multiply (kintamasis1, kintamasis2):
    return kintamasis1 * kintamasis2

def divide (kintamasis1, kintamasis2):
    return kintamasis1 / kintamasis2

print ("Pasirinkite operacija.")
print("1.Sudeti")
print("2.Atimti")
print("3.Padauginti")
print("4.Dalinti")

While True:
pasirinkimas = input("Irasyti pasirinkima(1/2/3/4):")

if choice in('1','2','3','4'):
    try:
        num1 = float(input("iveskite pirma skaiciu:"))
        num2 = float(input("iveskite antra skaiciu:"))
        except ValueError:
            print("Klaida. Prasome ivesti skaiciu.")
            cintinue
            
            if choice == '1':
                print (num1, "+", num2, "=", add(num1, num2))
