""""
kintamasis1 = 1
kintamasis2 = 2

def funkcija ():
    print(kintamasis1)
    print(kintamasis2)
    print(f'test:{kintamasis1}{kintamasis2}')
    print(f'test{kintamasis1}{kintamasis2}')
    print('test:{}{}'.format{kintamasis2, kintamasis1})

#komentaras

# Dviejų skaičių sudėjimas
def add (kintamasis1, kintamasis2):
    return kintamasis1 + kintamasis2

# Dviejų skaičių atėmimas
def subtract (kintamasis1, kintamasis2):
    return kintamasis1 - kintamasis2

# Dviejų skaičių sudauginimas
def multiply (kintamasis1, kintamasis2):
    return kintamasis1 * kintamasis2

# Dviejų skaičių dalinimas
def divide (kintamasis1, kintamasis2):
    if kintamasis2 ==0:
    return "Dalyba is nulio negalima"
    return kintamasis1 / kintamasis2


# Sukuriama meniu dalis
print ("Pasirinkite operacija.")
print("1.Sudeti")
print("2.Atimti")
print("3.Sudauginti")
print("4.Dalinti")
print("4.Baigti programą")

# Naudotojo įvestis priimama
while True:
pasirinkimas = input("Irasyti pasirinkima(1/2/3/4/5):")

# Tikriname ar pasirinkta iš viena iš penkiu pasirinkčių
if pasirinkimas in('1','2','3','4','5'):
    try:
        num1 = float(input("iveskite pirma skaiciu:"))
        num2 = float(input("iveskite antra skaiciu:"))
        except ValueError:
            print("Klaida. Prasome ivesti skaiciu.")
            continue
            
            if pasirinkimas == '1':
                print (num1, "+", num2, "=", sudeti(num1, num2))

            elif pasirinkimas =='2':
                print (num1, "-", num2, "=", atimti(num1, num2))

            elif pasirinkimas =='3':
                print (num1, "*", num2, "=", sudauginti(num1, num2))

            elif pasirinkimas =='4':
                print (num1, "/", num2, "=", da;inti(num1, num2))

            elif pasirinkimas =='5':
                print ("Programa baigta.")
                break
            else:
                 print("Pasirinkimas neteisingas.")
            
            # Tikriname ar naudotojas nori atlikti kitą operaciją
            kitas_skaiciavimas = input ("Pasirinkite kitą operaciją. (taip/ne):")
            if kitas_skaiciavimas == "ne":
                break
                else:
                    print ("neteisingas pasirinkimas")
                 # Tikriname ar naudotojas nori atlikti kitą operaciją
            kitas_skaiciavimas = input ("Pasirinkite kitą operaciją. (taip/ne):")
            if kitas_skaiciavimas == "ne":
                break
            else:
                    print ("neteisingas pasirinkimas.")                   
"""
from flask import Flask

app = Flask(__name__)

"""
skaicius = 0 # apsirasome kintamaji ( Globalus )
"""

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()



''' 1 susidiegiame Flask
    pip3 install Flask
    pip install Flask
'''
# 1. Flask įdiegimas
# 2. Importuojame

@app.route("/labas")
def sakyk_labas():
    global skaicius
    skaicius = skaicius +1

    return f"Labas {skaicius}"

                  



        
