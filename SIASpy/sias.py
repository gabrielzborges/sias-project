import serial
from firebase import firebase

fb = firebase.FirebaseApplication('firebaseURL',None)


# ---Mapeando leveis de umidade ---
U1 = 169   #exarcado
U2 = 340
U3 = 511
U4 = 682
U5 = 853  #totalmente seco

# ---Mapeado leveis de luminosidade ---
L1 = 250  #Escuro
L2 = 530
L3 = 950  #muito claro

# ---Mapeado leveis de temperatura ---
T1 = 0  #congelente
T2 = 5  #muito frio
T3 = 13 #temperado (frio mas bom para muitas sementes)
T4 = 22 #tropical  (quente mas bom para muitas sementes)
T5 = 36 #arido (muito quente)


# --------- TEMPERATURA ----------------------------------------
def temperaturaLvl(temp, level1, level2, level3, level4, level5):
    if temp > 0 and temp < level1:  #level 0 de temperatura: semente congela   (-inf a 0)
       print("Status: Semente vai congelar")
    elif temp > level1 and temp < level2: #level 1 de temperatura: muito frio   (0 a 5)
       print("Status: Semente vai morrer de frio")
    elif temp > level2 and temp < level3:  #level 2 de temperatura: umidade media   (5 a 13)
       print("Status: Pode estar frio")
    elif temp > level3 and temp < level4:  #level 3 de temperatura: umidade baixa   (13 a 22)
       print("Status: Temperado")
    elif temp > level4 and temp < level5:  #level 4 de temperatura: umidade muito baixa   (22 a 36)
       print("Status: Tropical")
    else:                                                     #level 5 de temperatura: solo seco   (36 a inf)
       print("Status: Semente vai morrer de calor")

def temperatura_whatMyLvl(temp, level1, level2, level3, level4, level5):
    if temp > 0 and temp < level1:  #level 0 de temperatura: semente congela   (-inf a 0)
       return 0
    elif temp > level1 and temp < level2: #level 1 de temperatura: muito frio   (0 a 5)
       return 1
    elif temp > level2 and temp < level3:  #level 2 de temperatura: umidade media   (5 a 13)
       return 2
    elif temp > level3 and temp < level4:  #level 3 de temperatura: umidade baixa   (13 a 22)
       return 3
    elif temp > level4 and temp < level5:  #level 4 de temperatura: umidade muito baixa   (22 a 36)
       return 4
    else:                                                     #level 5 de temperatura: solo seco   (36 a inf)
       return 5

#se retorno +: temp fria
#se retorno 0: temp ok
#se retorno -: temp quente
def temperatura_LvlAway(tempIdeaLvl, tempActual, level1, level2, level3, level4, level5):
    if tempActual > 0 and tempActual < level1:  #level 0 de temperatura: semente congela   (-inf a 0)
       return tempIdeaLvl - 0
    elif tempActual > level1 and tempActual < level2: #level 1 de temperatura: muito frio   (0 a 5)
       return tempIdeaLvl - 1
    elif tempActual > level2 and tempActual < level3:  #level 2 de temperatura: umidade media   (5 a 13)
       return tempIdeaLvl - 2
    elif tempActual > level3 and tempActual < level4:  #level 3 de temperatura: umidade baixa   (13 a 22)
       return tempIdeaLvl - 3
    elif tempActual > level4 and tempActual < level5:  #level 4 de temperatura: umidade muito baixa   (22 a 36)
       return tempIdeaLvl - 4
    else:                                                     #level 5 de temperatura: solo seco   (36 a inf)
       return tempIdeaLvl - 5

def temperatura_processLvlAway(lvlsAway):
    if lvlsAway > 0:
        if lvlsAway == 5:
            return "A semente vai congelar"
        elif lvlsAway == 4:
            return "Esta muito frio"
        elif lvlsAway == 3:
            return "Esta frio"
        elif lvlsAway == 2:
            return "Esta um pouco frio"
        elif lvlsAway == 1:
            return "Temperatura um pouco abaixo do ideal"
    elif lvlsAway < 0:
        if lvlsAway == -5:
            return "A semente vai derreter"
        elif lvlsAway == -4:
            return "Esta muito cozinhar"
        elif lvlsAway == -3:
            return "Esta muito quente"
        elif lvlsAway == -2:
            return "Esta quente"
        elif lvlsAway == -1:
            return "Temperatura um pouco acima do ideal"
    else:
        return 'Temperatura Ok'


# --------- LUMINOSIDADE -----------------------------------
def luminosidadeLvl(luz, level1, level2, level3):
    if luz < level1:  #level 0 de luminosidade: escuro
        return "Escuro"
    elif luz > level1 and luz < level2 : #level 1 de luminosidade: sombra
        return "Sombra"
    elif luz > level2 and luz < level3:  #level 2 de luminosidade: claro
        return "Claro"
    else:                                   #level 3 de luminosidade: muito claro
        return "Muito Claro"


# -------- UMIDADE --------------
def umidadeLvl(umidade, level1, level2, level3, level4, level5):
    if umidade > 0 and umidade < level1:  #level 0 de umidade: solo totalmente umido
        print("Status: Solo totalmente umido")
    elif umidade > level1 and umidade < level2: #level 1 de umidade: alta umidade
        print("Status: Solo com umidade alta")
    elif umidade > level2 and umidade < level3:  #level 2 de umidade: umidade media
        print("Status: Solo com umidade media")
    elif umidade > level3 and umidade < level4:  #level 3 de umidade: umidade baixa
        print("Status: Solo com umidade baixa")
    elif umidade > level4 and umidade < level5:  #level 4 de umidade: umidade muito baixa
        print("Status: Solo com umidade muito baixa")
    else:                                                     #level 5 de umidade: solo seco
        print("Status: Solo totalmente seco")


def umidade_whatMyLvl(umidade, level1, level2, level3, level4, level5):
    if umidade > 0 and umidade < level1:  #level 0 de umidade: solo totalmente umido
        return 0
    elif umidade > level1 and umidade < level2: #level 1 de umidade: alta umidade
        return 1
    elif umidade > level2 and umidade < level3:  #level 2 de umidade: umidade media
        return 2
    elif umidade > level3 and umidade < level4:  #level 3 de umidade: umidade baixa
        return 3
    elif umidade > level4 and umidade < level5:  #level 4 de umidade: umidade muito baixa
        return 4
    else:                                                     #level 5 de umidade: solo seco
        return 5

#se retorno +: umidade alta
#se retorno 0: umidade ok
#se retorno -: umidade baixa
#ve em qual level se encaixa a umidade atual e subtrai da umidade ideal
def umidade_LvlAway(umidadeIdeaLvl, umidadeActual, level1, level2, level3, level4, level5):
    if umidadeActual > 0 and umidadeActual < level1:  #level 0 de umidade: solo totalmente umido
        return umidadeIdeaLvl - 0
    elif umidadeActual > level1 and umidadeActual < level2: #level 1 de umidade: alta umidade
        return umidadeIdeaLvl - 1
    elif umidadeActual > level2 and umidadeActual < level3:  #level 2 de umidade: umidade media
        return umidadeIdeaLvl - 2
    elif umidadeActual > level3 and umidadeActual < level4:  #level 3 de umidade: umidade baixa
        return umidadeIdeaLvl - 3
    elif umidadeActual > level4 and umidadeActual < level5:  #level 4 de umidade: umidade muito baixa
        return umidadeIdeaLvl - 4
    else:                                                     #level 5 de umidade: solo seco
        return umidadeIdeaLvl - 5

def umidade_processLvlAway(lvlsAway):
    if lvlsAway > 0:
        if lvlsAway == 5:
            return "A semente vai afogar"
        elif lvlsAway == 4:
            return "Esta totalmente enxarcado"
        elif lvlsAway == 3:
            return "Esta enxarcado"
        elif lvlsAway == 2:
            return "Esta muito umido"
        elif lvlsAway == 1:
            return "Esta umido"
    elif lvlsAway < 0:
        if lvlsAway == -5:
            return "Terra esta arida"
        elif lvlsAway == -4:
            return "Esta totalmente seco"
        elif lvlsAway == -3:
            return "Esta muito muito seco"
        elif lvlsAway == -2:
            return "Esta muito seco"
        elif lvlsAway == -1:
            return "Esta seco"
    else:
        return 'Umidade Ok'

#----------- FIREBASE ACTIONS -----------------
def getTemperaturaData(temperaturaField):
    value = temperaturaField[14:temperaturaField.find(';'):1].rstrip()
    return value

def getLuminosidadeData(LuminosidadeField):
    value = LuminosidadeField[15:LuminosidadeField.find(';'):1].rstrip()
    return value

def getUmidadeData(umidadeField):
    value = umidadeField[9:umidadeField.find(';'):1].rstrip()
    return value



def postTemperatura(value, status):
    fb.patch('/Estado/Temperatura', {'Status': status, 'Value': value})

def postLuminosidade(value, status):
    fb.patch('/Estado/Luminosidade', {'Status': status, 'Value': value})

def postUmidade(value, status):
    fb.patch('/Estado/Umidade', {'Status': status, 'Value': value})


# -------- STATE CONTROL ----------------------
def stateChanged(actual, last):
    changed = False
    mudanca = [False, False, False]    #aonde mudar altera nessa lista de 0 -> 1
    for i in range(3):
        if actual[i] != last[i]:
            mudanca[i] = True
            changed = True
    return changed, mudanca

def getState(umidade, temperatura, luminosidade):
    #calcula status de temperatura
    t_lvlAway = temperatura_LvlAway(temperatura_necessaria_lvl, float(temperatura), T1, T2, T3,T4, T5)
    t_status = temperatura_processLvlAway(t_lvlAway)
    #calcula status de umidade
    u_lvlAway = umidade_LvlAway(umidade_necessaria_lvl, int(umidade), U1, U2, U3, U4, U5)
    u_status = umidade_processLvlAway(u_lvlAway)
    #calcula status de luminosidade
    l_status = luminosidadeLvl(int(luminosidade), L1, L2, L3)
    return t_status, u_status, l_status

def postChanges(change, mudou, lastState, temperatura, luminosidade, umidade, line):
    t_status, u_status, l_status = getState(umidade, temperatura, luminosidade)
    actualState = [t_status, l_status, u_status]
    change, mudou = stateChanged(actualState, lastState)

    if change:
        if mudou[0]:
            postTemperatura(temperatura, actualState[0])
        if mudou[1]:
            postLuminosidade(luminosidade, actualState[1])
        if mudou[2]:
            postUmidade(umidade, actualState[2])
        return actualState
    return lastState


# -------------------- MAIN ------------------------------------------
ser = serial.Serial('/dev/ttyACM0', 9600)

seedSelected = fb.get('/SementeSelecionada', None)
print(seedSelected)
umidade_necessaria = int(seedSelected['umidadeSolo'])
umidade_necessaria_lvl = umidade_whatMyLvl(umidade_necessaria, U1, U2, U3, U4, U5)
temperatura_necessaria = float(seedSelected['temperaturaIdeal'])
temperatura_necessaria_lvl = temperatura_whatMyLvl(temperatura_necessaria, T1, T2, T3, T4, T5)
print('Umidade da semente selecionada: ' + str(umidade_necessaria))
print('Temperatura da semente selecionada: ' + str(temperatura_necessaria))

n = ""
lastState = ['', '', '']
change = False
mudou = [False, False, False]

while True:
    line = ser.readline().decode('ascii')
    print(line)
    fields = line.split('-')
    if len(fields) > 1 and ('Umidade' in fields[0]) and ('Temperatura' in fields[1]) and ('Luminosidade' in fields[2]):
        umidade = getUmidadeData(fields[0])
        temperatura = getTemperaturaData(fields[1])
        luminosidade = getLuminosidadeData(fields[2])
        lastState = postChanges(change, mudou, lastState, temperatura, luminosidade, umidade, line)
