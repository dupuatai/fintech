from __future__ import annotations

from dataclasses import dataclass
import pandas as pd


@dataclass
class CompuertaCalidad:
    """
    Aplica reglas de negocio para decidir si el dataset es apto.
    """
    umbral_nulos: float = 0.08  # 8% por defecto

    def evaluar(self, df: pd.DataFrame, columna_target: str, columna_critica: str) -> bool:
        """
        Retorna True si el dataset pasa calidad; False si debe descartarse.
        Imprime reporte en consola.
        """
        
        total_filas = len(df)
        if total_filas == 0:
            print("ALERTA: dataset vacío. DESCARTAR.")
            return False

        porcentajes = {c: df[c].isna().mean() for c in df.columns}

        print("\nREPORTE DE NULOS (porcentaje):")
        for col, pct in sorted(porcentajes.items(), key=lambda x: x[1], reverse=True):
            print(f" - {col}: {pct:.2%}")

        pct_target = porcentajes.get(columna_target, 1.0)
        pct_critica = porcentajes.get(columna_critica, 1.0)

        if pct_target > self.umbral_nulos or pct_critica > self.umbral_nulos:
            print(
                f"\nALERTA: DESCARTAR dataset. "
                f"Nulos {columna_target}={pct_target:.2%}, {columna_critica}={pct_critica:.2%} "
                f"(umbral={self.umbral_nulos:.2%})."
            )
            return False

        print(
            f"\nOK: Dataset aprobado. "
            f"Nulos {columna_target}={pct_target:.2%}, {columna_critica}={pct_critica:.2%} "
            f"(umbral={self.umbral_nulos:.2%})."
        )
        return True
