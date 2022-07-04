import pandas as pd
import statistics

class Main:
    def __init__(self):
        '''Nos aseguramos de que las columnas de los meses sean 12
    
    Atributos
    ------------
    Meses: las distintas columnas del archivo que se dividen en meses.
    dic_gasto: creamos un diccionario vacío para almacenar los gastos de cada mes
    dic_ahorros: creamos un diccionario vacío para almacenar los ahorros de cada mes
    
    Metodos
    --------
    gasto_total():
        Funcion para saber el gasto total

    get_key(my_dict, val):
        Funcion para obtener la llave de un diccionario a partir de su valor

    ingresos_total():
        Funcion para saber el gasto total

    mas_ahorrado():
        Funcion que retorna el mes que mßs dinero se ha ahorrado

    mas_gastado():
        Funcion que retorna el mes que mßs dinero se ha gastado

    media():
        Funcion para obtener la media de los gastos


    '''


'''Comprobamos que el fichero existe'''
try:
    db = pd.read_csv("finanzas2020[1].csv", delimiter='\t')
    
    
    meses=db.columns
    assert(len(meses)==12)
    dict_gastos={}
    dict_ahorros={}
except IOError:
    print("Fichero No Existe")
except Exception as error:
    print(error)


def get_key(my_dict, val):
    '''
    Funcion para obtener la llave de un diccionario a partir de su valor
    '''
    for key, value in my_dict.items():
        if val == value:
            return key
    return "Not key found"  


def mas_gastado():
    '''Funcion que retorna el mes que más dinero se ha gastado'''

    for mes in meses:
        cuentas = list(db[mes])
        gasto_mes = 0
        for i in cuentas:
            try:
                if int(i) < 0:
                    gasto_mes += int(i)
            except ValueError:
                try:
                    if int(i[1:-1]) < 0:
                        gasto_mes += int(i[1:-1])
                except Exception as error:
                    print(error)           
            except Exception as error:
                print(error)

        dict_gastos[mes]= gasto_mes
    return get_key(dict_gastos,min(dict_gastos.values()))

 
def media():
    '''Funcion para obtener la media de los gastos'''
    return statistics.mean(dict_gastos.values())



def mas_ahorrado():
    '''Funcion que retorna el mes que más dinero se ha ahorrado'''
    for mes in meses:
        cuentas = list(db[mes])
        num_enteros=[]

    for i in cuentas:
        try:
            num_enteros.append(int(i))

        except ValueError:
            try:
                num_enteros.append(int(i[1:-1]))
            except Exception as error:
                print(error)           
        except Exception as error:
            print(error)
        
    dict_ahorros[mes]= sum(num_enteros)
    return get_key(dict_ahorros,max(dict_ahorros.values()))


def gasto_total():
    '''Funcion para saber el gasto total'''
    return sum(dict_gastos.values())


def ingresos_total():
    '''Funcion para saber el gasto total'''
    return sum(dict_ahorros.values()) - sum(dict_gastos.values())


try:
    print("El mes que más se ha gastado ha sido: ",mas_gastado())
    print("La media de gasto anual ha sido: ",media())
    print("El mes que más se ha ahorrado ha sido: ",mas_ahorrado())
    print("El gasto total anual ha sido: ",gasto_total())
    print("Los ingresos totales han sido: ",ingresos_total())
except Exception as error:
    print(error)



