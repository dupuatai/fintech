from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Iterable

import pandas as pd


def _limpiar_nombre_columna(nombre: str) -> str:
    """
    Limpia el nombre de una columna:
    - minúsculas
    - normaliza unicode (quita acentos/diacríticos)
    - espacios -> _
    - elimina caracteres especiales
    """
    nombre = nombre.strip().lower()

    nombre = unicodedata.normalize("NFKD", nombre)
    nombre = "".join([c for c in nombre if not unicodedata.combining(c)])

    nombre = re.sub(r"\s+", "_", nombre)
    nombre = re.sub(r"[^\w_]", "", nombre)
    nombre = re.sub(r"_+", "_", nombre)

    return nombre.strip("_")


@dataclass
class PreprocesadorDatos:
    """Clase para limpieza de columnas, banderas de nulos y análisis simple."""
    df: pd.DataFrame

    def limpiar_columnas(self) -> "PreprocesadorDatos":
        """Estandariza los nombres de columnas del DataFrame."""
        columnas_limpias = {c: _limpiar_nombre_columna(c) for c in self.df.columns}
        self.df = self.df.rename(columns=columnas_limpias)

        # Alias/correcciones típicas de legacy
        alias = {
            "aes_fraude": "es_fraude",
            "a_es_fraude": "es_fraude",
            "esfraude": "es_fraude",
        }
        self.df = self.df.rename(columns={c: alias[c] for c in self.df.columns if c in alias})

        return self

    def agregar_banderas_nulos(self, columnas_relevantes: Iterable[str]) -> "PreprocesadorDatos":
        """Agrega banderas *_nan = 1 si NaN, si no 0, para columnas relevantes existentes."""
        columnas_relevantes = list(columnas_relevantes)

        banderas = {
            f"{col}_nan": self.df[col].isna().astype(int)
            for col in columnas_relevantes
            if col in self.df.columns
        }

        for nombre_col, serie in banderas.items():
            self.df[nombre_col] = serie

        return self

    def porcentaje_nulos_por_columna(self) -> dict[str, float]:
        """Devuelve porcentaje de nulos por columna (0.0 a 1.0)."""
        total_filas = len(self.df)
        if total_filas == 0:
            return {col: 1.0 for col in self.df.columns}

        return {col: float(self.df[col].isna().sum()) / total_filas for col in self.df.columns}
