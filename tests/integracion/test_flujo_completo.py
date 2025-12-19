import numpy as np
import pandas as pd

from src.preprocesamiento.preprocesador_datos import PreprocesadorDatos
from src.reportes.compuerta_calidad import CompuertaCalidad


def test_flujo_aprueba_con_pocos_nulos() -> None:
    df_sucio = pd.DataFrame(
        {
            "Monto $$": [100.0, 200.0, 300.0, np.nan],
            "Â¿Es_Fraude?": [0, 1, 0, 0],
            "Nombre Cliente (RAW)": ["A", "B", "C", "D"],
        }
    )

    pre = PreprocesadorDatos(df_sucio).limpiar_columnas()
    pre.agregar_banderas_nulos(["monto", "es_fraude"])

    compuerta = CompuertaCalidad(umbral_nulos=0.30)  # 1/4 = 25% -> pasa
    assert compuerta.evaluar(pre.df, "es_fraude", "monto") is True


def test_flujo_descarta_si_monto_supera_umbral() -> None:
    df_sucio = pd.DataFrame(
        {
            "Monto $$": [np.nan, np.nan, 300.0, np.nan],  # 75% nulos
            "Â¿Es_Fraude?": [0, 1, 0, 0],
        }
    )

    pre = PreprocesadorDatos(df_sucio).limpiar_columnas()
    compuerta = CompuertaCalidad(umbral_nulos=0.10)  # 75% > 10%
    assert compuerta.evaluar(pre.df, "es_fraude", "monto") is False
