#PRIMERA PARTE: ESCOGER SI ES FIN DE SEMANA 
n=0
fecha=''
tb=5
costtotal=0

fecha=input("La boleta es para fin de semana?(si o no)")
n=int(input('Ingrese la cantidad de boletas que va comprar: ')) 
if fecha=='si':
  costtotal=tb*1.20
else:
  costtotal=tb
  
#SEGUNDA PARTE: BOLETAS PALCO (Proceso segun elección palco)
palco=input("Ingrese A, B, C, segun el palco que desee: ")
if palco=='A':
  costtotal+=tb*.1
elif palco=='B':
  costtotal+=tb*.05

#TERCERA PARTE: DESCUENTO POR BOLETAS (Proceso de descuento por cantidad de boletas)
if n>=4 and n<=10:
  costtotal=costtotal*.9
elif n>=10 and n<=20:
    costtotal=costtotal*.85
elif n>=21 and n>25:
  costtotal=costtotal*.80
print("El costo total a pagar es de: ", costtotal*n)
