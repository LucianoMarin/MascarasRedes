import msvcrt

def calcularElevacion(host):
    elevacion=2
    cont=0
    while (elevacion**cont-2)<int(host):
        cont=cont+1
    
    return cont



def prefijo(elevacion):
    maxBytes=32
    prefijo=0
    prefijo=maxBytes-elevacion

    return prefijo


def cadenaBits(prefijo):
    cadena=[]
    for i in range(32):
        
        if(i<prefijo):
            cadena.append(1);
          
        else:
            cadena.append(0);
           
        
                  
    return cadena;


def mascaraRed(cadena):
    valor=2
    pO=0
    sO=0
    tO=0
    cO=0
    for i in range (len(cadena)):
        if(i<8):
            if(cadena[i]==1):
                 pO+=valor**(7-i)
                 #print("1.-",pO)
        if(i>=8 and i<16):
             valor=2
             if(cadena[i]==1):
                sO+=valor**(15-i)
                #print("2.- ",sO)
        if(i>=16 and i<24):
             valor=2
             if(cadena[i]==1):
                tO+=valor**(23-i)
                #print("3.- ",tO)
        if(i>=24 and i<32):
             valor=2
             if(cadena[i]==1):
                cO+=valor**(32-(i+1))
                #print("4.- ",cO-1)

        
    
    print(pO,sO,tO,cO,sep=".")
        
       

                
            
       
 
            
Ver=True

while Ver:
    print('CALCULADORA DE MASCARA: ')
    host=input('INGRESE CANTIDAD DE HOST PARA SU RED: \n',)
    while str.isalpha(host) or int(host)<=0:
        print('INGRESE UN VALOR MAYOR A 0')
        host=input('INGRESE CANTIDAD DE HOST PARA SU RED: \n',)
    print('')
    print('')
    print('PREFIJO: ')
    elevacion=calcularElevacion(host)
    pf=prefijo(elevacion)
    print("/",prefijo(elevacion))

    print('')
    print('MASCARA RED: ')
    mascaraRed(cadenaBits(pf))


    print('')
    print('FORMATO BITS')
    for i in cadenaBits(pf):
        print(i, end="")

    print('')
    print('')
    print('DESEA CALCULAR MAS HOST? (CUALQUIER INGRESO EXCEPTO "SI" CIERRA EL PROGRAMA)')
    respuesta=input()
    if respuesta.upper()=="SI":
       Ver==True
    else:
        print('')
        print('FINALIZO EL PROGRAMA')
        break

    print('')
    


msvcrt.getch()


