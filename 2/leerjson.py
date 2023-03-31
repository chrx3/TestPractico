import json




def cargar_datos(ruta):
    with open(ruta, 'r') as contenido:
        datos = contenido.read()

        objeto = json.loads(datos)
        print("Productos con precio mayores a $20")
        print("------------------------------")
        for i in range(0,len(objeto['productos'])):
            if objeto['productos'][i]['precio'] > 20:
                print(objeto['productos'][i]['nombre'])
                print(objeto['productos'][i]['precio'])
                print("------------------------------")
        
        

if __name__=='__main__':
    ruta = 'productos.json'
    cargar_datos(ruta)