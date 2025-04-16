numero=int("25")

numero2=20
resultado= numero + numero2
print(resultado)

###################

nombre="richard hernandez"
edad= "24"
estatura="enano"
print(nombre + " "+edad +" "+ estatura)
añon= 2000
añoa= 2025
cedad= añoa - añon
print("tu edad actual es: "+ str(cedad))

#####################

precio=5000
prfinal=5000-(5000*0.15)
print("El precio final es: "+ str(prfinal))

edad_en_meses=int(edad)*12
edad_en_sem=int(edad)*12*4
edad_en_dias=int(edad)*12*4*7
edad_en_horas=int(edad)*12*4*7*24

######################

nota1=input("Ingrese la nota 1: ")
nota2=input("Ingrese la nota 2: ")
nota3=input("Ingrese la nota 3: ")

promedio= (float(nota1)+float(nota2)+float(nota3))/3

if promedio >= 4.0:
    print("El estado es aprobado, la nota es "+str(promedio))
else:
    print("El estado es reprobado, la nota final es: "+str(promedio))

