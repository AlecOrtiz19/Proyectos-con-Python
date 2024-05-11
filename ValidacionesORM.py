import peewee
import ORMpythom as clases




def validar_existencia(usuario, nombre_buscar):
    
    encontrar = False
    
    if  clases.User.select().where(clases.User.nombre == nombre_buscar).exists():
        
        encontrar = True
    
    return encontrar



