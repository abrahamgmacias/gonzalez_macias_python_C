from datetime import date

# Funciones
def formatNameUpper(fullName): 
    return (fullName[0] + " " + fullName[1] + " " + fullName[2]).upper()

def formatNameLower(fullName):
    return (fullName[0] + " " + fullName[1] + " " + fullName[2]).lower()

def formatDate(year, dayAndMonth):
    newDayAndMonth = dayAndMonth.split("-")
    return year + "-" + newDayAndMonth[0] + "-" + newDayAndMonth[1]

def getAge(year, dayAndMonth):
    month, day = [int(x) for x in dayAndMonth.split("-")]
    currentDate = date.today()
    return currentDate.year - int(year) - ((currentDate.month, currentDate.day) < (month, day))

def getFullnameLength(fullName):
    return len(''.join(fullName))

def getVocalsInFullname(fullName):
    compressedFullName, count = "".join(fullName), 0
    for letter in compressedFullName.lower():
        if letter in "aeiou":
            count += 1
    return count

def getRequestedAge(age):
    return age + 10

# Definir variables
answerText, answers, fullName = "Respuesta: ", [], []
questionsText = [
    f"¿Cuál es tu nombre(s)?\n {answerText}",
    f"¿Cuál es tu primer apellido?\n{answerText}",
    f"¿Cuál es tu segundo apellido?\n{answerText}",
    f"¿En qué año naciste?\n{answerText}",
    f'¿En qué mes y día naciste? (en el siguiente formato "mm-dd")\n{answerText}'
]

# Inputs
for q in questionsText:
    currentAnswer = input(q) 
    answers.append(currentAnswer)
    if (len(answers) <= 3):
        fullName.append(currentAnswer)
    
edad = getAge(answers[3], answers[4])

# Imprimir respuestas
print(f"Este es tu nombre completo en mayúsculas {formatNameUpper(fullName)}\n")
print(f"Este es tu nombre completo en minúsculas {formatNameLower(fullName)}\n")
print(f"Esta es tu fecha de nacimiento “{formatDate(answers[3], answers[4])}”\n")
print(f"Esta es tu edad {edad}\n")
print(f"Tu nombre completo tiene {getVocalsInFullname(fullName)} vocales\n")
print(f"Tu nombre completo tiene {getFullnameLength(fullName)} letras\n")
print(f"Tu edad en 10 años será {edad+10}\n")
print(f"La media de tu edad actual y tu edad en 20 años es {getRequestedAge(edad)}")


