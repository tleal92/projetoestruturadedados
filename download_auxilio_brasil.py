
import requests
import os

# URL do dataset do Auxílio Brasil (exemplo fictício)
url = "https://dados.gov.br/dataset/auxilio-brasil"

# Caminho para salvar o arquivo
output_path = "../data/auxilio_brasil.csv"

def download_data():
    # Realiza a requisição para baixar o arquivo
    response = requests.get(url)
    
    if response.status_code == 200:
        # Cria o diretório 'data' se não existir
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Salva o conteúdo no arquivo CSV
        with open(output_path, 'wb') as file:
            file.write(response.content)
        
        print("Dados baixados com sucesso!")
    else:
        print(f"Erro ao baixar os dados: {response.status_code}")

if __name__ == "__main__":
    download_data()
