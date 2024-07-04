from generators.generadorproducto import generardatosinstaladores
import pandas as pd

def analizarDatos():
    datos=generardatosinstaladores()
    tabla=pd.DataFrame(datos,columns=["responsable","edad","zona","experiencia","instalaciones"])
    tabla.to_csv("./data/instaladoresAburraSur.csv",index=False)
analizarDatos()