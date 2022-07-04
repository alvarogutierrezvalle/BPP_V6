import pandas as pd
import statistics

#Comprobamos que el fichero existe
try:
    db = pd.read_csv("finanzas2020[1].csv", delimiter='\t')
    
    #Nos aseguramos de que las columnas de los meses sean 12
    meses=db.columns
    assert(len(meses)==12)
    dict_gastos={}
    dict_ahorros={}
except IOError:
    print("Fichero No Existe")
except Exception as error:
    print(error)

#Función para obtener la llave de un diccionario a partir de su valor
def get_key(my_dict, val):
    for key, value in my_dict.items():
        if val == value:
            return key
    return "Not key found"  

#Función que retorna el mes que más dinero se ha gastado
def mas_gastado():
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

#Función para obtener la media de los gastos 
def media():
    return statistics.mean(dict_gastos.values())


#Función que retorna el mes que más dinero se ha ahorrado
def mas_ahorrado():
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

#Función para saber el gasto total
def gasto_total():
    return sum(dict_gastos.values())

#Función para saber el gasto total
def ingresos_total():
    return sum(dict_ahorros.values()) - sum(dict_gastos.values())


try:
    print("El mes que más se ha gastado ha sido: ",mas_gastado())
    print("La media de gasto anual ha sido: ",media())
    print("El mes que más se ha ahorrado ha sido: ",mas_ahorrado())
    print("El gasto total anual ha sido: ",gasto_total())
    print("Los ingresos totales han sido: ",ingresos_total())
except Exception as error:
    print(error)



