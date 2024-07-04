import random

def generardatosproductos():
    productos=["musica","tv","app","pc","cel","tablets","accesorios"]
    datos=[]
    for producto in productos:
        categoria=random.choice(["plus","mega","basic"])
        productoarreglo=[producto,categoria]
        datos.append(productoarreglo)
    return datos 
