import math,random
def calcular_area_circulo(radio):if radio>0:return math.pi*radio**2 else:print("El radio debe ser positivo");return None
def generar_lista_aleatoria(tamano,minimo,maximo):lista=[];for i in range(tamano):lista.append(random.randint(minimo,maximo));return lista
def procesar_datos(lista):suma=0;producto=1;for num in lista:suma+=num;producto*=num;print(f"Suma: {suma}, Producto: {producto}") if len(lista)>0:promedio=suma/len(lista);print(f"Promedio: {promedio}")else:print("La lista está vacía")
radio_circulo=5
print("Área del círculo:",calcular_area_circulo(radio_circulo))
datos=generar_lista_aleatoria(10,1,100)
print("Lista generada:",datos)
procesar_datos(datos)
