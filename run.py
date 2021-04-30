import  requests
from bs4 import BeautifulSoup

def main():
    url = "https://listado.mercadolibre.com.co/portatil-vostro-dell-3400#D[A:portatil%20vostro%20dell%203400]"

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
        
        print(f"Nombre: {nombre} \tprecio: {precio}")


    # for articulo in articulos.find_all("div"):
    #     # precios = articulo.find('spam',) 
    #     print(articulo)
    #     # contenido = articulo.find_all('h2')
    #     # precios = articulo.find_all('div')
    #     # for titulo in contenido:
    #     #     print(titulo)


if __name__ == '__main__':
    main()