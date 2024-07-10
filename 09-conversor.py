temperatura = float (input ("ingrese temperatura"))
escala = input ("es fahrenheit(F) o es Celsius(C)?" ).lower()

if escala == "f":
    celsius = (temperatura -32) * 5/9
    print (celsius)
elif escala == "C":
    fahrenheit = temperatura * 1.8 +32
    print (fahrenheit)
else:
    print ("no procede")