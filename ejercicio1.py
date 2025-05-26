#1. La Abarrotera ABSA tiene 4 sucursales en las cuales se realizaron diferentes ventas en los
#meses de Julio a diciembre del año 2022, se le ha solicitado a usted realizar un programa en
#donde pueda capturar la siguiente tabla de datos:

#Estado de cuenta de las Sucursales ABSA en el segundo semestre 2022
#+-------------+--------+--------+-------------+----------+-------------+------------+
#| Tienda/Mes  |  Julio | Agosto | Septiembre | Octubre  | Noviembre   | Diciembre  |
#+-------------+--------+--------+-------------+----------+-------------+------------+
#| ABSA 1      |  50000 |  60000 |      65000 |   62000  |       78000 |      95000 |
#| ABSA 2      |  89000 |  90000 |      98000 |   80000  |       85000 |      90000 |
#| ABSA 3      |  65000 |  72000 |      85000 |   72000  |       83000 |      98000 |
#| ABSA 4      |  92000 |  88000 |      90000 |   76000  |       82000 |      93000 |
#+-------------+--------+--------+-------------+----------+-------------+------------+

# y nos presente los siguientes resultados:
#    a. Venta total por todas las tiendas
#    b. Venta total por tienda
#    c. Tienda que más vendió en los 6 meses
#    d. Tienda que menos vendió


ventas = [
    [50000, 60000, 65000, 62000, 78000, 95000],
    [89000, 90000, 98000, 80000, 85000, 90000],
    [65000, 72000, 85000, 72000, 83000, 95000],
    [92000, 88000, 90000, 76000, 82000, 93000]]

# a. Venta total por todas las tiendas
total_ventas = sum(sum(tienda) for tienda in ventas)
print("a. Gran Total de Ventas de todas las tiendas: ", total_ventas)

# b. Venta total por tienda
print ("b.Total de Ventas por Tiendas: ")
for i, tienda in enumerate(ventas): 
     print(f"   - ABSA {i+1}: {sum(tienda)}")

# c. Tienda que vendió más
ventas_por_tienda = [sum(tienda) for tienda in ventas]
tienda_max = ventas_por_tienda.index(max(ventas_por_tienda)) + 1
print(f"c. Tienda con más ventas un lapso de 6 meses: ABSA {tienda_max}")

# d. Tienda con menos ventas
tienda_min = ventas_por_tienda.index(min(ventas_por_tienda)) + 1
print(f"d. Tienda con menos ventas un lapso de 6 meses: ABSA {tienda_min}")
# Explicación linea por linea:

#ventas = [
   # [50000, 60000, 65000, 62000, 78000, 95000],
   # [89000, 90000, 98000, 80000, 85000, 90000],
   # [65000, 72000, 85000, 72000, 83000, 95000],
   # [92000, 88000, 90000, 76000, 82000, 93000]]

    #ventas = Es el nombre de una variable que contiene toda la informacion de ventas de las 4 tiendas en 6 meses.
    # (=) = Es un operador de asignacion que asigna el valor de la derecha a la variable de la izquierda.
    # [50000, 60000, 65000, 62000, 78000, 95000], = Es una lista que contiene los valores de ventas de la tienda 1 en los meses de julio a diciembre.
    # por eso, hay 4 listas internas, una por cada tienda.


# a. Venta total por todas las tiendas
#total_ventas = sum(sum(tienda) for tienda in ventas)


# (#) = es un comentario 
# total_ventas = variable para guardar el resultado total de todas las tiendas.
# (=) = estoy el resultado de la suma a la variable total_ventas.
# (sum) = es una funcion de python que suma todo los valores de una lista.
# sum(tienda) for tienda in ventas = esto es una comprension de listas.
# for tienda in ventas = es un bucle que recorre cada tienda en la lista de ventas.
# sum(tienda) = para cada tienda, sumo sus ventas de los 6 meses.
# el (sum) de afuera suma los resultados individuales de cada tienda, osea de ahi sale el Gran total de ventas.


# print("a. Gran Total de Ventas de todas las tiendas:", total_ventas)

#print() = Funcion para mostrar resultado en consola , osea imprimir lo que hay dentro de los parentesis.
# "a. Gran total de Ventas de Todas las tiendas: " es el texto que se va a imprimir.
#, total_ventas = es el resultado de la suma de todas las variables de ventas.

#print ("b.Total de Ventas por Tiendas: ")

# muestra un titulo descriptivo de la siguiente seccion.


#for i, tienda in enumerate(ventas):
#    print(f"   - ABSA {i+1}: {sum(tienda)}")

# for es el inicio de un bucle que recorre cada tienda en la lista de ventas.
# enumerate(ventas) = esta funcion me da dos cosas al mismo tiempo:
# i = el indice de la tienda (0, 1, 2, 3) 
# tienda = la lista de ventas de esa tienda.
# print(f"..") = me ayuda a poner variales variables dentro de un texto que imprimire.
# EL ABSA {i+1} : el +1 es para que el indice empiece desde 1 y no desde 0.
# sum(tienda) = suma las ventas de cada tienda.


# ventas_por_tienda = [sum(tienda) for tienda in ventas]
# creo una nueva lista llamada ventas_por_tienda.
# uso comprension de lista nuevamente que se escribe de la siguiente manera: ventas_por_tienda = [sum(tienda) for tienda in ventas]
#para cada tienda en ventas, sumo sus ventas y se agrega a la nueva lista.
# luego ventas_por_tienda tendra algo como esto: [410000, 532000, 472000, 521000].
#luego lo mandas a imprimir con el print(f")


# tienda__max = ventas_por_tienda.index(max(ventas_por_tienda)) + 1

# El max(ventas_por_tiendas) encuentra el valor mas alto de la lista.
# El .index(..) Busca en que posicion de la lista se encuentra el valor maximo.
# El +1 es por que nuevamente, los indices van de 0 a 3, pero se llaman ABSA 1, ABSA 2 etc.
# Luego tienda_max guarda el numero de la tienda que mas vendio.
# Luego mandas a imprimir la tienda que mas vendio en los 6 meses.

# tienda_min = ventas_por_tienda.index(min(ventas_por_tienda)) + 1

# El min(ventas_por_tiendas) encuentra el valor mas bajo de la lista.
# El .index(..) Busca en que posicion de la lista se encuentra el valor minimo.
# El +1 es por que nuevamente, los indices van de 0 a 3, pero se llaman ABSA 1, ABSA 2 etc.
# Luego tienda_min guarda el numero de la tienda que menos vendio.
# Luego mandas a imprimir la tienda que menos vendio en los 6 meses.

# listo.