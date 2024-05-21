import urllib.request
from tqdm import tqdm

urls = [
    "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet",
    "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-02.parquet",
]

output_folder = "../data/raw"

for url in tqdm(urls):
    output_path = f"{output_folder}/{url.split('/')[-1]}"
    urllib.request.urlretrieve(url, output_path)