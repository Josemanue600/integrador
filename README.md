El programa hash.py es una herramienta de gestión y evaluación de seguridad de contraseñas.

Toma una lista de contraseñas ("archivos_limpios.txt"), las clasifica por longitud donde si su numero de carapteres es menor a 8 las envia aun archivo llamado "sin_seguridad.txt"
en caso de tener numero de carapteres mayores o iguales a 8 la encripta (hashea) para enviarlas al archivo "archivos_encriptados.txt"
 Ofrece un menú interactivo para ejecutar estas funciones, ver recomendaciones para contraseñas guardadas en el archivo "sin_seguridad.txt
definir un usuario a cada contraseña por medio de "archivos_limpios.txt", ver las cantidades de contraseñas enviadas a cada archivo y buscar/comparar contraseñas.

se importo (hashlib)	Se usa para encriptar (hashear) las contraseñas consideradas seguras utilizando el algoritmo SHA-256 o hashear  todas las contraseñas de "archivos_limpios.txt"
para la funcion def ver usuarios_y_sus_contraseñas_ya_encriptadas()


se importo (time)	Se usa para medir el tiempo que tarda la función comparar() en encontrar una contraseña solicitada en la lista que tiene los archivos
"sin_seguridad.txt" y archivos_encriptados.txt" por medio de un input


funciones

hashear()
Propósito: Lee contraseñas del archivo archivos_limpios.txt" y las clasifica.

Mecánica: Si la longitud es menor a 8, se escribe en "sin_seguridad.txt". Si es >= 8, se encripta con SHA-256 y se escribe en "archivos_encriptados.txt"





ver_usuario_y_su_contraseña_ya_encriptada()
Propósito: Muestra un diccionario en la terminal con un número de usuario correlativo y su contraseña hasheada

mecanica: asigna a cada contraseña un usuario en numero empezando desde el 0 mediante usuarios_totales = 0  en cual ira aumentado en 1 hasta que no exista contraseña 
a la que asignarle un usuario




ver_cantidad_de_contraseñas_encriptadas()
Propósito: Muestra el contador  de contraseñas que fueron enviadas a "archivos_encriptados.txt"

mecanica: por cada contraseña enviada a "archivos_encriptados.txt" cantidad_encriptadas aumentara 1

ver_cantidad_de_contraseñas_que_no_fueron_encriptadas()
Propósito: Muestra el contador de contraseñas que fueron enviadas a "sin_seguridad.txt"

mecanica: por cada contraseña envia a "sin_seguridad.txt " cantidad_sin_seguridad aumentara 1




recomendaciones_para_contraseñas_no_encriptadas()
Propósito: Lee las contraseñas de "sin_seguridad.txt" y ofrece recomendaciones básicas.

mecanica: basada en if, para cada contraseña a la cual si le falte ciertas cosas dara recomendaciones solo para lo faltante como 
 el que la contraseña tenga más de 8 caracteres, e incluir números y caracteres especiales.




comparar()
Propósito: Pide una contraseña al usuario y busca si existe en la lista de contraseñas inseguras o si su hash coincide con alguno en la lista de contraseñas encriptadas.

Mecánica: reporta el tiempo que tardó en encontrar la contraseña. El resultado de la búsqueda se guarda en "busqueda.txt" como un historial incluso si esta no existe
en ningun archivo

todas estas funciones se dan mediante un bucle while  a traves de input llamado accion donde mientras accion != "salir" este seguira corriendo,
para poder acceder a cada funcion se debe ingresar un string de numero en un rango de 1 a 6
en caso de ingresar salir el bucle termina e imprime en terminal "fue un honor servirte"
