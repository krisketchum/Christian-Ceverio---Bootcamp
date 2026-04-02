import pandas as pd

# 1. CARGA DE DATOS

# Cargar archivo CSV
df_csv = pd.read_csv("datos.csv")

# Cargar archivo Excel
df_excel = pd.read_excel("datos.xlsx")

# Cargar tabla web
url = "https://www.worldometers.info/world-population/population-by-country/"
df_web = pd.read_html(url)[0]

# 2. LIMPIEZA DE DATOS

# Ver valores nulos
print("Valores nulos CSV:\n", df_csv.isnull().sum())

# Eliminar filas con nulos
df_csv = df_csv.dropna()

# Eliminar duplicados
df_csv = df_csv.drop_duplicates()

# Ajustar tipos de datos
df_csv["ventas"] = df_csv["ventas"].astype(float)
df_csv["fecha"] = pd.to_datetime(df_csv["fecha"])

# 3. TRANSFORMACIÓN

# Seleccionar columnas relevantes
df_csv = df_csv[["fecha", "producto", "ventas"]]

# Renombrar columnas
df_csv.columns = ["Fecha", "Producto", "Ventas"]

# Ordenar datos
df_csv = df_csv.sort_values(by="Ventas", ascending=False)

# 4. EXPORTACIÓN

# Exportar a CSV
df_csv.to_csv("datos_limpios.csv", index=False)

# Exportar a Excel
df_csv.to_excel("datos_limpios.xlsx", index=False)

print("Proceso completado correctamente")