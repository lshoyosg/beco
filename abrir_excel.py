import pandas as pd
import os

# Ruta al archivo Excel
excel_path = os.path.join("datos", "BECO_1975_2023_web.xlsx")

# Cargar todas las hojas del archivo Excel en un diccionario de DataFrames
all_sheets = pd.read_excel(excel_path, sheet_name=None)

# Mostrar los nombres de las hojas y las primeras filas de cada una
for sheet_name, df in all_sheets.items():
	print(f"\nHoja: {sheet_name}")
	print(df.head())
