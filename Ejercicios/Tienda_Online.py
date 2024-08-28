print('**** Sistama Tienda Online****')
nombre_Producto=str(input("ingrese el nombre del producto:"))
precio=int(input("Ingrese el precio:"))
cantidad_inventario= int(input("ingreseo la cantidad en inventario que se tiene: "))

if cantidad_inventario >=1:
    disponible=True
if cantidad_inventario <=0:
    disponible=False


print("producto: ",nombre_Producto)
print("El precio es:", precio)
print("la cantidad es de:", cantidad_inventario)
print("la disponibilidad:", disponible)

