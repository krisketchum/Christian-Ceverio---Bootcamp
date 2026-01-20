import numpy as np

# Para que los resultados sean reproducibles
np.random.seed(42)

# 1️⃣ Simular una matriz 5x7 con temperaturas entre 10°C y 40°C
temperaturas = np.random.randint(10, 41, size=(5, 7))
print("Matriz de temperaturas (°C):\n", temperaturas)

# 2️⃣ Identificar temperaturas que superan los 30°C
mask_mayor_30 = temperaturas > 30
valores_mayor_30 = temperaturas[mask_mayor_30]
print("\nTemperaturas mayores a 30°C:\n", valores_mayor_30)

# 3️⃣ Reemplazar valores inferiores a 15°C por 15
temp_limpias = temperaturas.copy()
temp_limpias[temp_limpias < 15] = 15
print("\nMatriz con valores < 15 reemplazados por 15:\n", temp_limpias)

# 4️⃣ Calcular la media por ciudad (filas) y por día (columnas)
media_por_ciudad = temp_limpias.mean(axis=1)
media_por_dia = temp_limpias.mean(axis=0)

print("\nMedia por ciudad:\n", media_por_ciudad)
print("\nMedia por día:\n", media_por_dia)

# 5️⃣ Determinar la ciudad con mayor temperatura promedio
idx_ciudad_max = np.argmax(media_por_ciudad)
print(
    f"\nCiudad con mayor temperatura promedio: "
    f"Ciudad {idx_ciudad_max + 1} "
    f"({media_por_ciudad[idx_ciudad_max]:.2f}°C)"
)
