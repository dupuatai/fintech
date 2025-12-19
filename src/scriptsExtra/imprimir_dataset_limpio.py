from __future__ import annotations

import pandas as pd

from src.cargadores.cargador_csv import CargadorCSV
from src.preprocesamiento.preprocesador_datos import PreprocesadorDatos


def ejecutar() -> None:
    """
    Carga el dataset sucio, aplica limpieza y muestra el dataset limpio.
    """
    ruta_entrada = "datos/dataset_sucio_ventas.csv"
    ruta_salida = "datos/dataset_limpio_ventas.csv"

    # 1) Cargar datos
    cargador = CargadorCSV()
    df = cargador.leer_archivo(ruta_entrada)

    # 2) Preprocesar
    pre = PreprocesadorDatos(df)
    pre.limpiar_columnas()
    pre.agregar_banderas_nulos(["monto", "es_fraude"])

    # 3) Configuración de pandas para impresión clara
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 120)

    print("\nDATASET LIMPIO (primeras 10 filas):")
    print(pre.df.head(10))

    # 4) Guardar CSV limpio
    pre.df.to_csv(ruta_salida, index=False)
    print(f"\nDataset limpio guardado en: {ruta_salida}")


if __name__ == "__main__":
    ejecutar()
