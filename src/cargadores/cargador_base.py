from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
import pandas as pd


class CargadorDatos(Protocol):
    """Cargadores de datos."""

    def leer_archivo(self, ruta: str) -> pd.DataFrame:
        """Lee un archivo y devuelve un DataFrame."""
        raise NotImplementedError


@dataclass
class ConfiguracionLectura:
    """Configuración para la lectura del archivo."""
    separador: str = ","
    encoding: str | None = None
