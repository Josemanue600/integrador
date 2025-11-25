# importamos el programa para hashear o encriptar
import hashlib
import time

# con usuarios totales vamos a ir aumento el numero de usuario que se encuentra en el diccionario de persona
usuarios_totales = 0

# cada contraseña que sea mandada a sin_seguridad.txt aumentara este contador
cantidad_sin_seguridad = 0

#cada contraseña que se enviada a archivos_encriptados.txt aumentara este contador
cantidad_encriptadas = 0


# creamos una funcion en donde se  mostrara en terminal el numero de usuario y su contraseña encriptada 
def hashear():

#con el with open vamos a abrir 3 carpetas, archivos limpios.txt en donde "r" es para que lea la carpeta y 
#archivos encriptados.txt con "w" para que escriba las contraseñas ya encriptadas que si tiene una longitud mayor a 8 
#y sin seguridad.txt con "w"para que escriba las contraseñas con lontigitud menor a 8

    with open("archivos_limpios.txt", "r")as archivos, open("archivos_encriptados.txt","w") as encriptados, open("sin_seguridad.txt","w")as sin_seguridad:
        for linea in archivos:
            global cantidad_encriptadas  #llamamos_a_cantidad_de_encriptadas

            global cantidad_sin_seguridad    #llamamos a cantidad_sin_encriptar

            longitud = 8                     #"definimos nuestra longitud para saber si las contraseñas se iran a sin_seguridad.txt 
                                             #o a archivos_encrptados.txt
             
            nueva_linea = linea.strip() #evitamos saltos de linea
            encriptar =hashlib.sha256(nueva_linea.encode()).hexdigest() # encriptamos  las contraseñas
            
            if len(nueva_linea) < longitud: # si la cantidad de caracteres es menor que longitud la envia a sin_seguridad.txt
               sin_seguridad.write(nueva_linea + "\n")
               cantidad_sin_seguridad +=1 # el responsable de aumentar el contador cantidad_sin_seguridad
            else: 
               encriptados.write(encriptar+"\n") #si los caracteres son mayores a longitud la enviara a archivos_encriptados.txt ya
                                                 # hasheada
               encriptados.write("_"*30 +"\n") #agregamos espacios entre cada hash para mejor lectura
               cantidad_encriptadas +=1 #el responsable de aumentar el contador cantidad_encriptadas

        print("proceso exitoso")# una vez que todas las contraseñas hayan sido enviadas a su respectivo archivo imprimira esto


              

#funcion para ver el numero de usuarios y sus contraseñas ya hasheadas
def ver_usuario_y_su_contraseña_ya_encriptada():

    #abrimos el archivo_limpios.txt con r para leerlo y le accipnamos archivo como valor
    with open("archivos_limpios.txt", "r")as archivos:

        for linea in archivos: # agregamos un for para apoyarno en saber que queremos que la impresion sea linea por linea
            global usuarios_totales  # llamamos a usuarios_totales 
            nueva_linea = linea.strip() #evitamos saltos
            encriptar =hashlib.sha256(nueva_linea.encode()).hexdigest() #hasheamos
        
            persona = {                           #creamos nuestro diccionario
                "usuario": usuarios_totales,
                "contraseña": encriptar,
            }
    
            print(persona)
            print("_"*30)
            usuarios_totales += 1 #aumentamos el numero de usuarios

                          

#funcion para ver la cantidad de contraseñas encriptadas
def ver_cantidad_de_contraseñas_encriptadas():
    global cantidad_encriptadas  #llamamos a cantidad_encriptadas que se aumentaba en la funcion hashear
    print("*" * 60)
    print("la cantidad de contraseñas encriptadas es de: ",cantidad_encriptadas,"\n"
          "\n"
          "")
    print("*" * 60)

#funcion para ver la cantidad de contraseñas sin encriptar
def ver_cantidad_de_contraseñas_que_no_fueron_encriptadas():
    global cantidad_sin_seguridad #llamamos a cantidad_sin_seguridad que se aumentaba en la funcion hashear
    print("*" * 60)
    print("la cantidad de contraseñas que nisiquieras nos tomaremos el tiempo\n"
          "de encriptar es de",cantidad_sin_seguridad,"\n"
          "\n"
          "")
    print("*" * 60)
    
#funcion para recomendar, para las contraseñas enviadas al archivo sin seguridad
def recomendaciones_para_contraseñas_no_encriptadas():
    #abrimos el archivo sin_seguridad.txt con r para leer y se asipnamos sin_seguridad como valor
    with open("sin_seguridad.txt","r")as sin_seguridad:
        for recomendaciones in sin_seguridad:  #dado que la funcion es para recomendaciones cambiamos el valor de sin_segurdad
                                               # por recomendaciones para tener un mejor apoyo visual
            longitud = 8
            numeros = "0","1","2","3","4","5","6","7","8","9"
            caracteres_especiales = "@","!","#","$","%","&","/","(",")","="
            recomendacion = recomendaciones.strip()        #evitamos saltos

            if len(recomendacion)< longitud:                #verificamos si el numero de caracteres es menor que longitud
                print( recomendaciones, "tuvo una longitud < 8","\n" # si los caracteres de la contraseña son menores a longitud imprime esto
                      "se recomienda alagarla hasta superar los 8 caracteres")
            if not (any(c in numeros for c in recomendaciones)): # si la contraseña no tiene numero imprimira esto
                print(recomendaciones,"no cuanta con ningun numero","\n"
                      "se recomienda el uso de numero para una mayor seguridad")
            if not(any(c in caracteres_especiales for c in recomendaciones)):# si la contraseña no tiene caracteres especiales imprime esto
                print(recomendaciones," no cuenta con caracteres especiales\n"
                      "se recomendamos agregarlo para mayor seguridad")
            print("_"*60)#limita cuando acaban las recomendacciones para cada contraseña y sea facil de leer
    
#funcion para comparar en base a un input
def comparar():
    comparacion = input("ingrese la contraseña a comparar: ")
    nueva_comparacion =comparacion.strip() #quitamos espacios
    encriptar =hashlib.sha256(nueva_comparacion.encode()).hexdigest() #hasheamos

    #abrimos los archivos sin_seguridad.txt y archivos_encriptados.txt, ambos en modo lectura
    with open("sin_seguridad.txt","r")as sin_seguridad, open("archivos_encriptados.txt","r")as encriptados,open("busqueda.txt","a")as buscado:
        
        
        lineas_sin_seguridad =[linea.strip()for linea in sin_seguridad] #guardamos en una lista cada contraseña de sin-seguridad.txt
        lineas_encriptadas = [linea.strip()for linea in encriptados] #guardamos en una lista cada contraseña de archivos_encriptados.txt

        contraseñas =[lineas_encriptadas,lineas_sin_seguridad] 
        odjetivo = nueva_comparacion
        tiempo_inicio = time.time()
        for tiempo in contraseñas:
            if tiempo == odjetivo:
                break

        tiempo_fin = time.time()
        tiempo_encontrar_contraseña = tiempo_fin - tiempo_inicio
        

            
        if any(nueva_comparacion == inseguro for inseguro in lineas_sin_seguridad): #si lo ingresado en el input es igual a la contraseña
                buscado.write(f"{"*"*150}\n")
                buscado.write(f"{nueva_comparacion}, fue encontrada en el archivo sin_seguridad.txt, su tiempo para encontrar la contraseña fue de {tiempo_encontrar_contraseña* 1_000_000:.2f} segundos \n")  
                print("*"*60)                                                                    #guardada en sin_seguridad.txt imprime esto
                print(comparacion,"se encuentra en el archivo sin_seguridad.txt\n")
                print(f"su tiempo que tardo en econtrarse se fue de  {tiempo_encontrar_contraseña * 1_000_000:.2f}segundos\n")
                print("*"*60)  
        elif any(encriptar == seguro for seguro in lineas_encriptadas): #si lo ingresado en el input es igual a la contraseña guardada
                                                                        #en archivos_encriptados.txt imprime esto
                buscado.write(f"{"*"*150}\n")
                buscado.write(f"{nueva_comparacion}, fue encontrada en el archivo archivos_encriptados.txt, su tiempo para encontrar la contraseña fue de {tiempo_encontrar_contraseña* 1_000_000:.2f} segundos\n")   
                print("*"*60)                                                     
                print("hash",encriptar," encontrado con exito en archivos_encriptados.txt\n"
                  "\n")
                print(f"su tiempo que tardo en econtrarse se fue de  {tiempo_encontrar_contraseña * 1_000_000:.2f} segundos")
                print("*"*60)  
        else:
            buscado.write(f"{"*"*150}\n")
            buscado.write(f"{nueva_comparacion}, no existe en la base de datos actualmente\n")
            print("*"*60)  
            print("la base de datos no tiene lo solicitado\n" 
            "")# en caso de no estar en ninguna lista imprime esto
            print("*"*60)  
    
            


    

#donde empieza todo, de aqui se llamara a cada funcion dependiendo el numero ingresado
accion = input("que quieres hacer?:\n"
               "hashear [1] \n"
               "ver usuario y su contraseña ya encriptada [2] \n"
               "ver cantidad de contraseñas encriptadas [3] \n"
               "ver cantidd de contraseñas que no fueron encriptadas [4] \n"
               "recomendaciones para contraseñas no encriptadas [5] \n"
               "comparar [6]\n"
               "salir\n")

while accion != "salir":#mientras lo ingresado en el input es diferente de salir el programa continua
    if accion == "1":
        hashear()
    elif accion == "2":
        ver_usuario_y_su_contraseña_ya_encriptada()
    elif accion == "3":
        ver_cantidad_de_contraseñas_encriptadas()
    elif accion == "4":
        ver_cantidad_de_contraseñas_que_no_fueron_encriptadas()
    elif accion == "5":
        recomendaciones_para_contraseñas_no_encriptadas()
    elif accion == "6":
        comparar()
    else:
        print("accion no valida")
    accion = input("que mas deseas hacer?:\n"        #una vez termine lo que hace cada funcion se repite un ciclo 
               "hashear [1] \n"
               "ver usuario y su contraseña ya encriptada [2] \n"
               "ver cantidad de contraseñas encriptadas [3] \n"
               "ver cantidd de contraseñas que no fueron encriptadas [4] \n"
               "recomendaciones para contraseñas no encriptadas [5 ]\n"
               "comparar [6] \n"
               "salir\n")
print("fue un honor servirte")# en caso de escribir salir el accion el programa finalisa
