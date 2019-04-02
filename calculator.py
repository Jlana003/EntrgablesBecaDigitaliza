import sys

def pedirDato(msg):
    try:
        num = float(input(msg).replace(",", "."))
    except ValueError:
        sys.exit("El valor introducido no es un número")
    except Exception as e:
        sys.exit("Error: "+e.__str__())
    return num

def sumar(a,b):
    print (str(a)+"+"+str(b)+"="+str(a+b))
def restar(a, b):
        print(str(a) + "-" + str(b) + "=" + str(a - b))
def multiplicar(a,b):
    print (str(a)+"*"+str(b)+"="+str(a*b))
def dividir(a,b):
    try:
        print (str(a)+"/"+str(b)+"="+str(a/b))
    except ZeroDivisionError:
        print("No se puede realizar une división entre 0")
def exponencial(a,b):
    print (str(a)+"^"+str(b)+"="+str(a**b))

opt=-1
opciones={1:"Suma",2:"Resta",3:"Multiplicación",4:"División",5:"Exponencial",0:"Salir"}

#Recoger datos
i=pedirDato("Introduce el primer valor: ")
j=pedirDato("Introduce el segundo valor: ")


#Solicitar la operación y realizarla
while opt!=0:
    print ("Escoge la operación:")
    for key in opciones.keys():
        print(str(key)+".-"+opciones[key])
    try:
        opt=int(input())
    except:
        print("Esa opción no está contemplada")
        continue
    if opt not in opciones.keys():
        print ("Esa opción no está contemplada")
        continue
    print(opciones[opt].upper())
    if opt==1:
        sumar(i,j)
    elif opt == 2:
        restar(i,j)
    elif opt==3:
        multiplicar(i,j)
    elif opt == 4:
        dividir(i,j)
    elif opt == 5:
        exponencial(i,j)
else:
    print ("Fin de la ejecución")