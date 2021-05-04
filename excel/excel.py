import openpyxl
class Excel:

   wb = openpyxl.Workbook()
   hoja = wb.active
   def __init__(self):
      self.hoja.append(('Nombre', 'Precio'))
   
   def agregar_lista(self, listaproductos):
      self.producto = listaproductos

      for producto in listaproductos:
         self.hoja.append(producto)


   def guardar_excel(self):
      self.wb.save('productos1.xlsx')