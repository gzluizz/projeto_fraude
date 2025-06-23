import os
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from scripts.logic import process_file

# Definir a pasta onde os arquivos serão armazenados
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}

# Criar o diretório de uploads se não existir
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Criar um Blueprint para as rotas
main_bp = Blueprint('main', __name__)

# Função para verificar se o arquivo tem a extensão permitida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Página inicial com o formulário de upload
@main_bp.route('/')
def index():
    return render_template('index.html')

# Rota para receber o arquivo e gerar os resultados
@main_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        # Processar o arquivo
        report, img_base64 = process_file(file_path)

        # Retornar o relatório e a imagem da matriz de confusão
        return render_template('index.html', report=report, cm_image=img_base64)

    return redirect(request.url)
