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
from flask import Flask, request

app = Flask(__name__)



skaicius = 0 # apsirasome kintamaji ( Globalus )
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
        print ("Dalyba is nulio negalima")
    else:
        return skaicius1 / skaicius2

@app.route("/") # Route 1
def hello_world():

    return f"""
             <from action="/skaicius">
                    <label for="test">skaicius 1</label><br>
                        <input type="text" id="test" name="test" value="0"><br>
                         </br></br>

                    <label for="operacija">Operacija:</label>
                    <select id= "operacija"name="operacija">
                        <option 
                            value="sudetis">Sudetis</option><option
                            value="atimtis">Atimtis</option><option
                            value="daugyba">Daugyba</option><option
                            value="dalyba">Dalyba
                        </option>
                    </select><br><br>
            
        
                    <label for="test2">skaicius 2</label><br>
                        <input type="text" id="test2" name="test2" value="0"><br><br>
                         </br></br>

                    <input type="submit" value="Submit">
                </form>
            """
"""
@app.route("/labas") # Route 2
def sakyk_labas():
    global skaicius ## Naudojam globala kintamaji
    skaicius = skaicius +1 ## Atidarius programa pridedam vieneta
    skaicius = 10
    return f"Labas {skaicius}"
    
@app.route("/skaicius") # Route 3
def skaiciavimo():
    try:
       # UZKLAUSA. ARGUMENTAVIMAS. METODAI ()
        skaicius1 = int(request.args.get("test"))## Pasiima argumenta is URL pvz.: /skaicius?test=200
        skaicius2 = int(request.args.get("test2"))
        operacija = int(request.args.get("operacija"))

        if operacija == "sudetis":
            result = sudetis(skaicius1, skaicius2)
        elif operacija == "atimtis":
            result = atimtis(skaicius1, skaicius2)

        elif operacija == "daugyba":
            result = daugyba(skaicius1, skaicius2)

        elif operacija == "dalyba":
            result = dalyba(skaicius1, skaicius2)
        
        return f"Rezultatas: {result}" 
    except ValueError:
        return f"Įveskite skaiciu" 
    
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
"""
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result_html = ""
    expression = request.form.get('expression', '')
    if request.method == 'POST':
        try:
            result = eval(expression)
            result_html = "<h2>Result: {}</h2>".format(result)
        except:
            result_html = "<h2>Error: Error</h2>"

    calculator_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Skaičiuotuvas</title>
    </head>
    <body>
        <h1>Skaičiuotuvas</h1>
        <form action="/" method="post">
            <input type="text" name="expression" value="{}">
            <br>
            <button type="button" onclick="button_click('7')">7</button>
            <button type="button" onclick="button_click('8')">8</button>
            <button type="button" onclick="button_click('9')">9</button>
            <button type="button" onclick="button_click('/')">/</button>
            <br>
            <button type="button" onclick="button_click('4')">4</button>
            <button type="button" onclick="button_click('5')">5</button>
            <button type="button" onclick="button_click('6')">6</button>
            <button type="button" onclick="button_click('*')">*</button>
            <br>
            <button type="button" onclick="button_click('1')">1</button>
            <button type="button" onclick="button_click('2')">2</button>
            <button type="button" onclick="button_click('3')">3</button>
            <button type="button" onclick="button_click('-')">-</button>
            <br>
            <button type="button" onclick="button_click('0')">0</button>
            <button type="button" onclick="button_click('.')">.</button>
            <button type="submit">=</button>
            <button type="button" onclick="button_click('+')">+</button>
            <br>
            <button type="reset">C</button>
        </form>

        {}
        
        <script>
            function button_click(symbol) {{
                var expression_field = document.getElementsByName("expression")[0];
                expression_field.value += symbol;
            }}
        </script>
    </body>
    </html>
    """.format(expression, result_html)

    return calculator_html

if __name__ == '__main__':
    app.run(debug=True)
