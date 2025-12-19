import pandas as pd
from src.preprocesamiento.preprocesador_datos import PreprocesadorDatos


def test_limpieza_columna_monto() -> None:
    df = pd.DataFrame({"Monto $$": [10, 20]})
    resultado = PreprocesadorDatos(df).limpiar_columnas().df
    assert "monto" in resultado.columns


def test_limpieza_columna_nombre_cliente() -> None:
    df = pd.DataFrame({"Nombre Cliente (RAW)": ["A", "B"]})
    resultado = PreprocesadorDatos(df).limpiar_columnas().df
    assert "nombre_cliente_raw" in resultado.columns
