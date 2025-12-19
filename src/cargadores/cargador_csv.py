from __future__ import annotations

import pandas as pd
from .cargador_base import ConfiguracionLectura


class CargadorCSV:
    """Cargador concreto para archivos CSV."""

    def __init__(self, configuracion: ConfiguracionLectura | None = None) -> None:
        self.configuracion = configuracion or ConfiguracionLectura()

    def leer_archivo(self, ruta: str) -> pd.DataFrame:
        """
        Lee un CSV y devuelve un DataFrame.
       
        """
        encodings_a_probar = (
            [self.configuracion.encoding]
            if self.configuracion.encoding
            else ["utf-8", "utf-8-sig", "latin-1", "cp1252"]
        )

        ultimo_error: Exception | None = None
        for enc in encodings_a_probar:
            try:
                return pd.read_csv(
                    ruta,
                    sep=self.configuracion.separador,
                    encoding=enc,
                )
            except Exception as exc:  # noqa: BLE001 (robustez controlada)
                ultimo_error = exc

        raise RuntimeError(f"No se pudo leer el CSV. Último error: {ultimo_error}")
