import pandas as pd
import re
import random



# Leer el archivo CSV utilizando expresiones regulares para identificar el patrón del encabezado
with open('C:/Users/seba-/Desktop/Python/OTROS/BD/bases/bank/bank.csv') as f:
    encabezado = f.readline()
    Categ_encabezado = re.findall(r'"(.*?)"',  encabezado)  # extraer las categorías que están entre comillas dobles
    if not encabezado.startswith('"'): #verificar si el primer elemento no empieza con comillas
        elemento1 =  encabezado.split(';')[0]  # obtener el primer elemento del encabezado sin comillas
        Categ_encabezado.append(0, elemento1)  # insertar el primer elemento en la lista de categorías


df = pd.read_csv('C:/Users/seba-/Desktop/Python/OTROS/BD/bases/bank/bank.csv', sep=';', decimal=',', names=Categ_encabezado)


# eliminar la primera fila (fila 0)
df = df.drop(0)
Orden=df


#Renombrado de las columnas y cambio nombre varialble 'Orden' a 'renombrado', con el fin de realizar la traduccion al español. misma 
#funcion ejecutada con el resto de columnas
renombrado=Orden.rename(columns={'age': 'edad',
                         'job': 'trabajo',
                         'marital': 'casado/soltero',
                         'education': 'estudios',
                         'default': 'default',
                         'balance': 'balance',
                         'housing': 'propiedad',
                         'loan': 'loan',
                         'contact': 'contacto',
                         'day': 'dia',
                         'month': 'mes',
                         'duration': 'duracion',
                         'campaign': 'campaña', 
                         'pdays': 'dia pago',  
                         'previous': 'previo',  
                         'poutcome': 'poutcome',  
                         'y': 'y'}
)

# Establecer la semilla para la generación de números aleatorios, esto ayuda a "mantener" los valores la siguiente vez que se ejute el codigo
# y los salarios no cambien en cada ejecucion
random.seed(42)
#Agregar salarios de forma aleatoria
renombrado['salario'] = [random.randint(500000, 3500000) for _ in range(len(renombrado))]

#agregar una propiedad con un valor a 75 veces su sueldo
renombrado['valor_propiedad'] = renombrado['salario'] * 75


#Para saber las variables unicas de cada columna, ejecutar print(elementos_unicos_"nombre columna")
elementos_unicos_casado = renombrado['casado/soltero'].unique() 
renombrado['casado/soltero'] = renombrado['casado/soltero'].replace({'married': 'casado', 'single': 'soltero','divorced':'divorciado'})


elementos_unicos_mes = renombrado['mes'].unique() 
renombrado['mes'] = renombrado['mes'].replace({'jan':'enero',
                                               'feb':'febrero',
                                               'mar':'marzo',
                                               'apr':'abril',
                                               'may':'mayo',
                                               'jun':'junio',
                                               'jul':'julio',
                                               'aug':'agosto',
                                               'sep':'septiembre',
                                               'oct':'octubre',
                                               'nov':'noviembre',
                                               'dec':'diciembre'})


elementos_unicos_trabajo = renombrado['trabajo'].unique()
renombrado['trabajo'] = renombrado['trabajo'].replace({'unemployed': 'desempleado',
                                                       'services': 'servicios',
                                                       'management': 'gerencia',
                                                       'blue-collar': 'obrero',
                                                       'self-employed': 'independiente',
                                                       'technician': 'técnico',
                                                       'entrepreneur': 'emprendedor',
                                                       'admin.': 'administrativo',
                                                       'student': 'estudiante',
                                                       'housemaid': 'ama de casa',
                                                       'retired': 'jubilado',
                                                       'unknown': 'desconocido'})


elementos_unicos_estudios = renombrado['estudios'].unique()
renombrado['estudios'] = renombrado['estudios'].replace({'primary':'basica',
                                                       'secondary':'media',
                                                       'tertiary':'universitario',
                                                       'unknwon':'desconocido'})


elementos_unicos_default = renombrado['default'].unique() 
renombrado['default'] = renombrado['default'].replace({'yes':'si'})


elementos_unicos_propiedad = renombrado['propiedad'].unique()
renombrado['propiedad'] = renombrado['propiedad'].replace({'yes':'si'})


elementos_unicos_loan = renombrado['loan'].unique()
renombrado['loan'] = renombrado['loan'].replace({'yes':'si'})


elementos_unicos_contacto = renombrado['contacto'].unique() 
renombrado['contacto'] = renombrado['contacto'].replace({'cellular':'celular',
                                                         'unknown':'desconocido',
                                                         'telephone':'telefono'})


elementos_unicos_poutcome = renombrado['poutcome'].unique()
renombrado['poutcome'] = renombrado['poutcome'].replace({'unknown':'desconocido',
                                                         'failure':'fallido',
                                                         'other':'otros',
                                                         'success':'realizado'})


elementos_unicos_y = renombrado['y'].unique()
renombrado['y'] = renombrado['y'].replace({'yes':'si'})



def prestamo():
    numero_persona = int(input("Ingrese el número de la persona que desea buscar: "))
    persona = renombrado.iloc[numero_persona]

    edad = persona['edad']
    trabajo = persona['trabajo']
    estudios = persona['estudios']
    salario = pd.to_numeric(persona['salario'])
    propiedad = pd.to_numeric(persona['valor_propiedad'])

    if (salario < 800000) or (edad < '21') or (trabajo == 'desempleado') or (estudios == 'basica'):
        print("La persona no puede optar a crédito, si desea buscar alguna opción, dirijase a un ejecutivo")
    else:
        print("La persona puede optar a crédito.")
        maximo= (propiedad*0.3)  + (salario * 3)
        print(f'El prestamos maximo es de : {maximo}')

    print("_______________________________________________________________________________")
    datos = renombrado.iloc[numero_persona]
    print(datos)


def calcular_cuota_mensual():
    numero_persona = int(input("Ingrese el número de la persona que desea buscar: "))
    persona = renombrado.iloc[numero_persona]
    salario = pd.to_numeric(persona['salario'])
    propiedad = pd.to_numeric(persona['valor_propiedad'])
    maximo= (propiedad*0.3)  + (salario * 3)
    print(f"El préstamo máximo es: {maximo:.2f}") #.2f, es para mostrar 2 decimales despues del entero
    valor_prestamo = float(input("Ingrese el valor del préstamo: "))
    tasa_interes_anual = float(input("Ingrese la tasa de interés anual (%): "))
    cantidad_meses = int(input("Ingrese la cantidad de meses del crédito: "))

   

    tasa_interes_mensual = (1 + tasa_interes_anual / 100) ** (1/12) - 1

    cuota_mensual = (valor_prestamo * tasa_interes_mensual * (1 + tasa_interes_mensual) ** cantidad_meses) / ((1 + tasa_interes_mensual) ** cantidad_meses - 1)

    if valor_prestamo > maximo:
        print("El valor del préstamo excede el máximo permitido.")
        return

    print(f"La cuota mensual es: {cuota_mensual:.2f}")


calcular_cuota_mensual()