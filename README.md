# Projeto de Detecção de Fraudes em Transações Financeiras

Este projeto utiliza técnicas de **Machine Learning** para detectar fraudes em transações financeiras com base em dados de cartões de crédito. A aplicação foi desenvolvida usando **Flask**, permitindo o upload de arquivos CSV contendo dados de transações, que são processados e analisados para identificar transações fraudulentas. A aplicação exibe os resultados na web, incluindo um relatório de classificação e uma matriz de confusão gerada pelo modelo.

## Tecnologias Utilizadas

- **Flask**: Framework para desenvolvimento web.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **NumPy**: Biblioteca para operações numéricas.
- **Scikit-learn**: Biblioteca para algoritmos de Machine Learning e avaliação de modelos.
- **Seaborn**: Biblioteca para visualização de dados.
- **Matplotlib**: Biblioteca para criação de gráficos.
- **Werkzeug**: Utilizado para o processamento de arquivos no Flask.

## Funcionalidade

A aplicação permite ao usuário:
- Carregar um arquivo CSV contendo transações financeiras.
- Processar o arquivo para detectar transações fraudulentas.
- Visualizar os resultados em uma página web, com:
  - **Relatório de Classificação**: Exibe métricas como precisão, recall e F1-score do modelo.
  - **Matriz de Confusão**: Visualização gráfica da performance do modelo.

## Estrutura do Projeto

projeto_fraude_flask/
├── app.py # Arquivo principal que chama as rotas e roda a aplicação
├── scripts/
│ ├── routes.py # Arquivo de rotas
│ └── logic.py # Arquivo de lógica (processamento de dados)
├── templates/
│ └── index.html # Página de upload e exibição de resultados
├── static/
│ └── style.css # Estilos para a página
├── requirements.txt # Arquivo de dependências
├── uploads/ # Pasta para armazenar arquivos CSV enviados
└── README.md # Este arquivo de documentação


## Instalação

### 1. Clonar o Repositório

Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
```

### 2. Criar um Ambiente Virtual

É altamente recomendado usar um ambiente virtual para isolar as dependências:

```bash
python -m venv venv
```

### 3. Ativar o Ambiente Virtual

```bash
Windows
venv\Scripts\activate

Linux/MacOS:
source venv/bin/activate
```

### 4. Instalar as Dependências

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### 5. Rodar a Aplicação

Para rodar a aplicação Flask, execute o seguinte comando:

```bash
python app.py
```

A aplicação estará acessível no seu navegador através de:

```bash
http://127.0.0.1:5000/
```


### 6. Carregar um Arquivo CSV

Na página inicial, você verá um formulário de upload de arquivos.

Selecione um arquivo CSV contendo os dados de transações financeiras (com uma coluna chamada Class que indica se a transação é fraude ou não) e clique em "Carregar".

Após o upload, você verá o relatório de classificação e a matriz de confusão gerada.

## Arquivos Importantes
app.py: Este arquivo contém o código que inicializa e executa a aplicação Flask. Ele importa as rotas definidas no arquivo routes.py e executa o servidor.

scripts/routes.py: Define as rotas da aplicação. Quando um arquivo é enviado, ele é processado pela função process_file definida em scripts/logic.py.

scripts/logic.py: Contém a lógica de processamento de dados, como a leitura do arquivo CSV, pré-processamento dos dados, treinamento do modelo de detecção de fraudes e geração de resultados.

templates/index.html: Página HTML onde o usuário pode fazer o upload do arquivo e visualizar os resultados.

static/style.css: Arquivo de estilo CSS para a página web.

## Detalhes do Modelo
O modelo de detecção de fraudes é baseado em um Random Forest Classifier da biblioteca Scikit-learn. O modelo é treinado com dados de transações financeiras, sendo capaz de prever se uma transação é fraudulenta ou não. Após o treinamento, o modelo é avaliado utilizando métricas de classificação, como precisão, recall, F1-score e matriz de confusão.

## Como Funciona
O usuário envia um arquivo CSV através da interface web.

O arquivo é processado pela função process_file no arquivo logic.py, que executa:

Carregamento e pré-processamento dos dados.

Treinamento de um modelo de Random Forest.

Geração do relatório de classificação e matriz de confusão.

Os resultados são exibidos na página web.
