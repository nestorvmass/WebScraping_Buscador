from MercadoLibre.mercadolibre import buscar_producto
from Tienda_Exito.exito import buscar_producto as buscarenexito
def main():
    # buscar_producto("Dell 3400")
    articulos_exito = buscarenexito("Dell 3400")
    print(articulos_exito)


if __name__ == '__main__':
    main()