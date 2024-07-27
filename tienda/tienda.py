from producto import Producto

# CLASS Y DEF
class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.nombre = nombre
        self.costo_delivery = costo_delivery
        self.productos = []

    def ingresar_producto(self, producto):
        for p in self.productos:
            if p == producto:
                p.stock += producto.stock
                return
        self.productos.append(producto)
    
    def listar_productos(self):
        return "\n".join([str(p) for p in self.productos]) #REPASAR
    

# Para realizar una venta, se debe solicitar el nombre del producto que se desea vender 
# y la cantidad requerida.     
    def realizar_venta(self, nombre_producto, cantidad):
        for p in self.productos:
            if p.nombre == nombre_producto:
                if p.stock >= cantidad:
                    p.stock -= cantidad
                    return f'Venta realizada: {cantidad} unidades de {nombre_producto}'
                else:
                    disponible = p.stock
                    p.stock = 0
                    return f'Venta realizada parcialmente: {disponible} unidades de {nombre_producto}'
        return f'Producto {nombre_producto} no encontrado'

# NOTA: Los productos de las tiendas de tipo “Restaurante” siempre tienen stock igual 
# a 0, ya que el producto solo se fabrica al momento de que se realiza una venta. Es 
# decir, aunque se especifique un valor de stock, los productos de estas tiendas se 
# crean con stock 0 y este no se modifica si se añade nuevamente el        
# mismo producto a la lista de productos existentes de la tienda.

class Restaurante(Tienda):
    def ingresar_producto(self, producto):
        producto.stock = 0
        super().ingresar_producto(producto)

    def listar_productos(self):
        return "\n".join([f'{p.nombre} - ${p.precio}' for p in self.productos])
    
    def realizar_venta(self, nombre_producto, cantidad):
        for p in self.productos:
            if p.nombre == nombre_producto:
                return f'Venta realizada: {cantidad} unidades de {nombre_producto}'
        return f'Producto {nombre_producto} no encontrado'



class Supermercado(Tienda):
    def listar_productos(self):
        productos_listados = []
        for p in self.productos:
            if p.stock < 10:
                productos_listados.append(f'{p.nombre} - ${p.precio} - Pocos productos disponibles')
            else:
                productos_listados.append(f'{p.nombre} - ${p.precio} - Stock: {p.stock}')
        return "\n".join(productos_listados)


class Farmacia(Tienda):
    def listar_productos(self):
        productos_listados = []
        for p in self.productos:
            if p.precio > 15000:
                productos_listados.append(f'{p.nombre} - ${p.precio} - Envío gratis al solicitar este producto')
            else:
                productos_listados.append(f'{p.nombre} - ${p.precio}')
        return "\n".join(productos_listados)
    
    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad > 3:
            return f'No se puede vender más de 3 unidades por producto en la Farmacia'
        return super().realizar_venta(nombre_producto, cantidad)


























# class Supermercado(Tienda):
#     def listar_productos(self):
#         productos_listados = []
#         for p in self.productos:
#             if p.stock < 10:
#                 productos_listados.append(f'{p.nombre} - ${p.precio} - Pocos productos disponibles')
#             else:
#                 productos_listados.append(f'{p.nombre} - ${p.precio} - Stock: {p.stock}')
#         return "\n".join(productos_listados)