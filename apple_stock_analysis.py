import zipfile
import os
import pandas as pd

# Ruta del archivo ZIP
zip_path = r"C:\Users\MAYRA ROCIO\Downloads\archive.zip"
extract_folder = r"C:\Users\MAYRA ROCIO\Downloads\archive"  # Carpeta donde extraeremos el archivo

# Verificar si el archivo ZIP existe
if os.path.exists(zip_path):
    # Extraer el archivo ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Archivo extraído en: {extract_folder}")

    # Ruta del archivo CSV extraído
    csv_path = os.path.join(extract_folder, "apple_stock.csv")

    # Verificar si el archivo CSV existe después de la extracción
    if os.path.exists(csv_path):
        print(f"Archivo encontrado: {csv_path}. Cargando datos...")
        df = pd.read_csv(csv_path)
        print("Datos cargados correctamente.")
        print(df.head())
    else:
        print(f"Error: No se encontró el archivo 'apple_stock.csv' en la ruta {csv_path}")
else:
    print(f"Error: El archivo ZIP no se encuentra en la ruta especificada: {zip_path}")