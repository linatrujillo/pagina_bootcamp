import kagglehub
from kagglehub import KaggleDatasetAdapter

file_path = "AI_desafios.xlsx"  # o el archivo que tengas

df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "LMarcelatrujillo/ia-desafios",
    file_path,
    
)
df.head(20).to_json("datos.json", orient="records")  # Exporta los primeros 20 registros
print(df.head())



    