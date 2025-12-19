# Objetivo
Este repositorio contiene un módulo de preprocesamiento de datos desarrollado como parte de un caso de negocio de detección de fraude en una Fintech.
El objetivo del proyecto es evaluar automáticamente la calidad de un dataset histórico de transacciones antes de que sea utilizado para entrenar un modelo de Machine Learning. El sistema limpia y estandariza los datos, corrige problemas comunes de sistemas legacy, genera indicadores de valores faltantes y aplica reglas de negocio para decidir si los datos son aptos para continuar hacia la etapa de entrenamiento.
# Analisis:
El dataset es aprobado porque las columnas críticas para el modelo (es_fraude y monto) presentan niveles de valores nulos muy por debajo del umbral máximo definido. Aunque existen valores faltantes en columnas secundarias, estos no comprometen la viabilidad del entrenamiento y pueden ser tratados en etapas posteriores del pipeline.
# Reporte
la ejecucion para ver el reporte debe ser: python -m src.main
# Ejemplo de rsultado
REPORTE DE NULOS (porcentaje):
 - nombre_cliente_raw: 9.74%
 - transaction_id: 9.14%
 - categoria_productotipo: 7.22%
 - fech_registro: 7.14%
 - notes_comments: 6.98%
 - es_fraude: 3.52%
 - monto: 2.72%
 - score_15: 1.44%
 - monto_nan: 0.00%
 - score_15_nan: 0.00%
 - categoria_productotipo_nan: 0.00%
 - es_fraude_nan: 0.00%

OK: Dataset aprobado. Nulos es_fraude=3.52%, monto=2.72% (umbral=8.00%).
