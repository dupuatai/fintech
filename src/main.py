from __future__ import annotations

from src.cargadores.cargador_csv import CargadorCSV
from src.preprocesamiento.preprocesador_datos import PreprocesadorDatos
from src.reportes.compuerta_calidad import CompuertaCalidad


def ejecutar() -> None:
    ruta = "datos/dataset_sucio_ventas.csv"

    cargador = CargadorCSV()
    df = cargador.leer_archivo(ruta)

    pre = PreprocesadorDatos(df).limpiar_columnas()

    # OJO: tras limpiar, tu "Â¿Es_Fraude?" probablemente termina como "es_fraude"
    # y "Monto $$" como "monto".
    columnas_relevantes = ["monto", "score_15", "categoria_productotipo", "fecha_registro", "es_fraude"]

    pre.agregar_banderas_nulos(columnas_relevantes)

    compuerta = CompuertaCalidad(umbral_nulos=0.08)
    aprobado = compuerta.evaluar(
        pre.df,
        columna_target="es_fraude",
        columna_critica="monto",
    )

    if not aprobado:
        # excepción controlada (sin romper feo, pero sí marcando fallo)
        raise SystemExit(1)


if __name__ == "__main__":
    ejecutar()
