import  requests
from bs4 import BeautifulSoup


def transformar_texto(articulo):
    nombre_articulo = ""
    nombre_articulo = articulo.replace(' ','-')

    return nombre_articulo

def buscar_producto(articulo):

    # url = "https://listado.mercadolibre.com.co/portatil-vostro-dell-3400#D[A:portatil%20vostro%20dell%203400]"
    # nombre_articulo = transformar_texto(articulo)
    url = f"https://listado.mercadolibre.com.co/{transformar_texto(articulo)}"

    r = requests.get(url)
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')

    # articulos = soup.find('ol', class_ ='ui-search-layout ui-search-layout--stack')
    articulos = soup.find_all('li', class_ ='ui-search-layout__item')
    # print(articulos)
    for articulo in articulos:
        nombre = articulo.find('h2', class_='ui-search-item__title').text
        precioreal = articulo.find('span', class_='price-tag-fraction').text
        precio = articulo.find('span', class_='price-tag ui-search-price__part').text
        print(f"Nombre: {nombre.strip()} \tprecio: {precio.strip()}")
