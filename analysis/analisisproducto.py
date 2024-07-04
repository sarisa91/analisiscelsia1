from generators.generadorproducto import generardatosproductos
import pandas as pd

def analizarDatos():
    datos=generardatosproductos()
    tabla=pd.DataFrame(datos,columns=["Tipo Producto","categoria"])
    tabla.to_csv("./data/tablaproductos.csv",index=False)
analizarDatos()