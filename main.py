#imports
import random

#arrays

q0 = [
'ID',
'Můžete uvést, kolikrát jste reklamoval/a nakoupené zboží nebo službu za poslední dva roky?',
'Jaká musí být minimální hodnota reklamovaného zboží, abyste přistoupil/a k reklamaci?',
'Které zboží nejčastěji reklamujete?',
'Kterou službu nejčastěji reklamujete?',
'Kde hledáte pomoc, pokud chcete zjistit informace o reklamacích?',
'Byla v případě Vašich reklamací vždy dodržena zákonná lhůta 30 dní pro vyřízení reklamace?',
'Čemu dáváte při  reklamaci přednost?',
'Spokojenost s postupem reklamací',
'Ochrana spotřebitelů',
'Vaše pohlaví',
'Váš věk',
'Vaše nejvyšší ukončené vzdělání',
'Jaký směr Vašeho vzdělání převažuje?',
'Jaký je ve Vaší domácnosti příjem (čistý) na 1 osobu /měsíc?'
]
q1 = ['Nikdy','Jednou','Dvakrát','Třikrát','Více jak čtyřikrát']
q2 = ['Na částce nezáleží','100CZK','200CZK','500CZK','1000CZK','2000CZK','Zboží zásadně nereklamuji']
q3 = ['Potraviny','Oděvy','Obuv','Nábytek','Domácí spotřebiče','Zboží spojené s informačními technologiemi','Bicykl','Automobil']
q4 = ['Dodávku elektřiny','Dodávku plynu','Dodávku vody','Telefonní služby','Zdravotní služby','Sociální služby','Finanční služby','Opravárenské služby']
q5 = ['Internet','Tisk','Zkušenosti blízkých','Právní předpisy']
q6 = ['Ano','Ne']
q7 = ['Vrácení peněz','Výměně zboží za nové','Opravě zboží','Výměně za jiné zboží']
q8 = [1,2,3,4,5] #loopnout pro 6-7 otázek, bias dle otázky
q10 = ['Muž','Žena']
q11 = ['18-24 let', '25-34 let','35-49 let','50-65 let','66 a více let']
q12 = ['Základní','Výuční list','Středoškolské s maturitou','Vysokoškolské']
q13 = ['Ekonomické','Technické','Humanitární','Přírodovědné']
q14 = ['do 5000CZK','5001-10000CZK','10001-20000CZK','20001CZK a více']

#funkce

def get_three(q):
    choices = random.sample(q, 3)
    if len(choices) > len(set(choices)): #zjišťuje redundanci v arrayi
        #return 'nigga' #debug
        return 'ERR001 - RANDOMIZER FUCKED UP' #ošetřené, nemůže se stát --> legacy
    else:
        return choices

def qtable(q, num_q, add):  #q - id listu, num_q - počet otázek, add - full bias otázka
    values = []
    x = 1
    while x <= num_q:
        values.append(random.choice(q))
        x += 1
    if add > 0: #bias - pouze int menší než číslo add
        add_val = []
        xx = 1
        while xx <= add:
            add_val.append(xx)
            xx += 1
        values.append(random.choice(add_val))
    else:
        pass #nerob nic
    return values

#program

#přidat možnost vytvoření nového souboru a zápisu do něj

#init
outfile = "output.txt"

print('Vítejte v generátoru dotazníkových výsledků')
print('Pro pokračování vyberte z následujích možností: \n Stiskem klávesy 1 pokračujte v defaultním režimu \n Stiskem klávesy 2 pokračujte zadáním vlastního výstupu \n 3 pro debug')
userinput = input()

if userinput == '1': #defaultní nastavení dle základních parametrů pro dotazník A4MRK
    pass
elif userinput == '2': #tvorba vlastního souboru --> přidat logiku, možnost přidání vlastních otázek a odpovědí přes dialog
    print('Zadejte vlastní název výstupního souboru')
    outfile = input()
else:
    print('allah') #debug

with open(outfile,'a') as f:
    for y in range(len(q0)):
        f.write(q0[y] + ';') #hlavičky sloupců
    i = 1
    print('\n', file=f)
    while i <= 50:
        print(i, ';', random.choice(q1), ';', random.choice(q2), ';', get_three(q3), ';', get_three(q4), ';', random.choice(q5), ';', random.choice(q6), ';', random.choice(q7), ';', 
        qtable(q8, 5, 3), ';', qtable(q8, 7, 0), ';', random.choice(q10), ';', random.choice(q11), ';', random.choice(q12), ';', random.choice(q13), ';', random.choice(q14), file=f)
        i+=1
    #print(q1, file=f) #debug

#input("allah") #debug
input('Odpovědi vygenerovány do výstupního souboru, potvrďte jakoukoliv klávesou')
