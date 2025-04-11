
# Projeto de Engenharia de Dados - Auxílio Brasil

Este projeto tem como objetivo construir um pipeline de dados que envolve a busca, coleta, modelagem, carga e análise de dados do Auxílio Brasil.

## Objetivo
O objetivo deste MVP é criar um pipeline que permita a coleta de dados do Auxílio Brasil, sua análise e visualização para responder às perguntas relacionadas ao programa.

### Perguntas de Negócio
1. Qual é o número total de beneficiários do Auxílio Brasil?
2. Quais estados têm o maior número de beneficiários?
3. Qual é o valor médio recebido pelos beneficiários?

## Estrutura do Projeto
- `scripts/`: Contém o script Python para coleta de dados.
- `data/`: Armazena os dados coletados.
- `README.md`: Documentação do projeto.

## Como Executar
Para rodar o projeto localmente, siga os passos abaixo:

### 1. Instale as dependências:
```bash
pip install requests
```

### 2. Execute o script para baixar os dados:
```bash
python scripts/download_auxilio_brasil.py
```

Isso irá salvar os dados na pasta `data/`.

## Tecnologias Utilizadas
- Python
- Requests
- GitHub (para controle de versão)
