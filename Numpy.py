import numpy as np

def convertir_a_clp(precios_usd, tipo_cambio=950):
    """Convierte una matriz de precios en USD a CLP."""
    print("\n--- TRANSFORMACIÓN DE USD A CLP ---")
    print(f"Se aplica un tipo de cambio de {tipo_cambio} CLP por 1 USD")
    return precios_usd * tipo_cambio


def calcular_metricas(precios_clp):
    """Calcula promedio, máximo y mínimo por acción."""
    promedio = np.mean(precios_clp, axis=1)
    maximo = np.max(precios_clp, axis=1)
    minimo = np.min(precios_clp, axis=1)
    return promedio, maximo, minimo


def calcular_variacion_diaria(precios_clp):
    """Calcula la variación porcentual diaria."""
    return ((precios_clp[:, 1:] - precios_clp[:, :-1]) / precios_clp[:, :-1]) * 100


def calcular_logaritmo(precios_clp):
    """Aplica logaritmo natural a los precios."""
    return np.log(precios_clp)


def obtener_precio_especifico(precios_clp, accion, dia):
    """Obtiene el precio de una acción en un día específico."""
    return precios_clp[accion, dia]


def mostrar_resultados(precios_usd, precios_clp, promedio, maximo, minimo, variacion, log_precios, precio_especifico):
    """Imprime todos los resultados."""
    
    print("MATRIZ ORIGINAL DE PRECIOS (USD):")
    print(precios_usd)

    print("\nMATRIZ DE PRECIOS CONVERTIDA A CLP:")
    print(precios_clp)

    print("\nPROMEDIO POR ACCIÓN (CLP):")
    print(promedio)

    print("\nMÁXIMO POR ACCIÓN (CLP):")
    print(maximo)

    print("\nMÍNIMO POR ACCIÓN (CLP):")
    print(minimo)

    print("\nVARIACIÓN PORCENTUAL DIARIA (%):")
    print(variacion)

    print("\nLOGARITMO NATURAL DE LOS PRECIOS:")
    print(log_precios)

    print("\nPRECIO ESPECÍFICO (ACCIÓN 3, DÍA 5):", precio_especifico, "CLP")


def main():
    # Datos iniciales
    precios_usd = np.array([
        [150.20, 152.30, 149.80, 151.10, 153.50],
        [102.10, 101.50, 103.20, 105.00, 104.80],
        [300.40, 298.10, 295.50, 301.20, 305.40],
        [85.50, 86.20, 84.90, 87.10, 88.00],
        [210.00, 212.50, 211.30, 215.00, 214.20]
    ])

    print("=== ANÁLISIS DE PRECIOS DE ACCIONES ===")
    print("Datos originales expresados en USD")

    # Flujo del programa
    precios_clp = convertir_a_clp(precios_usd)
    promedio, maximo, minimo = calcular_metricas(precios_clp)
    variacion = calcular_variacion_diaria(precios_clp)
    log_precios = calcular_logaritmo(precios_clp)
    precio_especifico = obtener_precio_especifico(precios_clp, 2, 4)

    # Mostrar resultados
    mostrar_resultados(
        precios_usd,
        precios_clp,
        promedio,
        maximo,
        minimo,
        variacion,
        log_precios,
        precio_especifico
    )


if __name__ == "__main__":
    main()