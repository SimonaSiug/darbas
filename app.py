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
def sudetis (kintamasis1, kintamasis2):
    return kintamasis1 + kintamasis2

# Dviejų skaičių atėmimas
def atimtis (kintamasis1, kintamasis2):
    return kintamasis1 - kintamasis2

# Dviejų skaičių sudauginimas
def daugyba (kintamasis1, kintamasis2):
    return kintamasis1 * kintamasis2

# Dviejų skaičių dalinimas
def dalyba (kintamasis1, kintamasis2):
    if kintamasis2 ==0:
    return "Dalyba is nulio negalima"
    return kintamasis1 / kintamasis2


# Sukuriama meniu dalis
print ("Pasirinkite operacija.")
print("1.Sudetis")
print("2.Atimtis")
print("3.Daugyba")
print("4.Dalyba")
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
from flask import Flask, request

app = Flask(__name__)






skaicius = 0 # apsirasome kintamaji ( Globalus )

def sudetis (kintamasis1, kintamasis2):
    return kintamasis1 + kintamasis2


@app.route("/") # Route 1
def hello_world():

    return f"""
                <from action="/skaicius">
                    <label for="test">skaicius 1</label><br>
                        <input type="text" id"test" name="test" value"0"><br>

                    </br></br>

                    <label for="test2">skaicius 2</label><br>
                        <input type="text" id"test2" name="test2" value"0"><br><br>

                    </br></br>

                    <label for="[[__ID__]]">skaicius 2</label><br>
                        <input type="text" id"[[__ID__]]" name="[[__ID__]]" value"0"><br><br>

                    <input type="submit" value"Submit">
                    </form>
            """

@app.route("/labas") # Route 2
def sakyk_labas():
    global skaicius ## Naudojam globala kintamaji
    skaicius = skaicius +1 ## Atidarius programa pridedam vieneta
    skaicius = 10
    return f"Labas {skaicius}"
    
@app.route("/skaicius") # Route 3
def skaiciavimo():
    # UZKLAUSA. ARGUMENTAVIMAS. METODAI ()
   skaicius = request.args.get("test") ## Pasiima argumenta is URL pvz.: /skaicius?test=200
   skaicius2 = request.args.get("test2")

   suma = sudetis(int(skaicius2),(skaicius))
   return f"Tavo ivestas skaicius: {suma}"

if __name__ == "__main__":
    app.run()

##http://127.0.0.1:5000
##http://localhost:5000

''' 1 susidiegiame Flask
    pip3 install Flask
    pip install Flask
'''
# 1. Flask įdiegimas
# 2. Importuojame



                  



        
