import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64

def process_file(file):
    # Carregar os dados
    data = pd.read_csv(file)
    
    # Pré-processamento
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data.drop('Class', axis=1))

    # Converter de volta para DataFrame
    data_scaled_df = pd.DataFrame(data_scaled, columns=data.columns[:-1])
    data_scaled_df['Class'] = data['Class']  # Coluna alvo

    # Dividir os dados em treino e teste
    X = data_scaled_df.drop('Class', axis=1)
    y = data_scaled_df['Class']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinamento do modelo
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    # Previsões
    y_pred = rf.predict(X_test)

    # Avaliação do modelo
    report = classification_report(y_test, y_pred)

    # Matriz de Confusão
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Não Fraude', 'Fraude'], yticklabels=['Não Fraude', 'Fraude'])
    ax.set_title("Matriz de Confusão")
    ax.set_xlabel("Previsão")
    ax.set_ylabel("Real")

    # Salvar a matriz de confusão em formato base64 para exibição no HTML
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode()
    plt.close(fig)

    return report, img_base64
