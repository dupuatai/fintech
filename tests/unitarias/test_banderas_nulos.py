import numpy as np
import pandas as pd
from src.preprocesamiento.preprocesador_datos import PreprocesadorDatos


def test_bandera_nulo_asigna_1_si_nan() -> None:
    df = pd.DataFrame({"monto": [100.0, np.nan]})
    resultado = PreprocesadorDatos(df).agregar_banderas_nulos(["monto"]).df
    assert resultado.loc[0, "monto_nan"] == 0
    assert resultado.loc[1, "monto_nan"] == 1
