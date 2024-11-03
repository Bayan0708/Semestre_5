import pandas as pd

# Lee el archivo Excel
archivo_excel = 'Practica_04_Datos'
df = pd.read_excel(archivo_excel)

# Especifica el rango de filas y columnas que deseas seleccionar
fila_inicio = 5  # El índice de la primera fila (comienza en 0)
fila_fin = 17     # El índice de la última fila que deseas seleccionar (exclusivo)
columnas = ['Punto OB2', 'L [cm]'	,'d'	,'f']  # Las columnas que deseas seleccionar

# Selecciona el intervalo especificado
df_seleccionado = df.iloc[fila_inicio:fila_fin, df.columns.isin(columnas)]

# Define una función para convertir un DataFrame a código LaTeX
def dataframe_a_latex(df):
    latex = df.to_latex(index=False, escape=False)
    return latex

# Convierte el DataFrame seleccionado en código LaTeX
codigo_latex = dataframe_a_latex(df_seleccionado)

# Imprime el código LaTeX en la consola
print(codigo_latex)
