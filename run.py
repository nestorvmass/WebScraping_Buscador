from tiendas.mercadolibre import MercadoLibre
from excel.excel import Excel

def main():
    mercadolibre = MercadoLibre()
    articulos_mercado = mercadolibre.buscar_producto("Dell 3400")
    libroexcel = Excel()
    # buscar_producto("Dell 3400")
    # articulos_exito = buscar_exito("Dell 3400")
    libroexcel.agregar_lista(articulos_mercado)
    # libroexcel.agregar_lista(articulos_exito)
    libroexcel.guardar_excel()

    

if __name__ == '__main__':
    main()