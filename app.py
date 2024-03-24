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
def sudetis (skaicius1, skaicius2):
    return skaicius1 + skaicius2

# Dviejų skaičių atėmimas
def atimtis (skaicius1, skaicius2):
    return skaicius1 - skaicius2

# Dviejų skaičių sudauginimas
def daugyba (skaicius1, skaicius2):
    return skaicius1 * skaicius2

# Dviejų skaičių dalinimas
def dalyba (skaicius1, skaicius2):
    if skaicius2 ==0:
    return "Dalyba is nulio negalima"
    return skaicius1 / skaicius2


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
                print (skaicius1, "+", skaicius2, "=", sudeti(skaicius1, skaicius2))

            elif pasirinkimas =='2':
                print (skaicius1, "-", skaicius2, "=", atimti(skaicius1, skaicius2))

            elif pasirinkimas =='3':
                print (skaicius1, "*", skaicius2, "=", sudauginti(skaicius1, skaicius2))

            elif pasirinkimas =='4':
                print (skaicius1, "/", skaicius2, "=", dalinti(skaicius1, skaicius2))

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

from flask import Flask, request, render_template
import math

app = Flask(__name__)
history = []


def sudetis(skaicius1, skaicius2):
    return skaicius1 + skaicius2


def atimtis(skaicius1, skaicius2):
    return skaicius1 - skaicius2


def daugyba(skaicius1, skaicius2):
    return skaicius1 * skaicius2


def dalyba(skaicius1, skaicius2):
    if skaicius2 == 0:
        return "Dalyba iš nulio negalima"
    else:
        return skaicius1 / skaicius2


@app.route("/", methods=['GET', 'POST'])
def calculator():
    result_html = ""
    expression = request.form.get('expression', '')
    if request.method == 'POST':
        try:
            result = eval(expression)
            result_html = "<h2>Rezultatas: {}</h2>".format(result)
            history.append(expression + " = " + str(result))
        except:
            result_html = "<h2>Klaida: Klaida</h2>"

    history_html = "<h2>Veiksmų istorija:</h2><ul>"
    for item in history:
        history_html += "<li>{}</li>".format(item)
    history_html += "</ul>"

    return render_template('calculator.html', expression=expression, result_html=result_html, history_html=history_html)


if __name__ == '__main__':
    app.run(debug=True)
 

