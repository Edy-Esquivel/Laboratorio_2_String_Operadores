

#Adicional a lo indicado en el Ejercicio 2 que en este Ejercicio 
#es aplicable la notación slices, en este se aplican las subsecuencias en la cadena de caracteres
# escrita en la variable palabra, la cual contiene ESTO ES UN EJEMPLO y al desarrollar la notación 
 #mencionada es posible segmentar en trozos y así poder obtener (para este ejemplo) la palabra ES ESTO UN EJEMPLO, 
 #técnicamente se indican el orden de los fragmentos para que se distribuyan así en la impresión en pantalla, donde se 
 #utiliza desde 0 hasta 5 y 7 devolviendo la combinación de elementos “ES” de 0 a 4 devolviendo el conjunto de elementos 
 #“ESTO” de 8 a 10 “UN” de 11 hasta el final  de la cadena “UN EJEMPLO” por lo que se aplican las subsecuencias de manera simple 
 #para una palabra ordenada e imprimiéndola acorde a cada uno de los fragmentos indicados para la variable.

 
palabra = "ESTO ES UN EJEMPLO"
print (palabra[5:7] + " " + palabra [0:4] + " " + 
palabra[8:10] + " " + palabra[11:] + " ???")
