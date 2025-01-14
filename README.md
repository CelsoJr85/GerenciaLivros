Gerenciador de Livros

Este é um projeto desenvolvido em Django que permite o gerenciamento de livros pessoais. A aplicação utiliza Bootstrap 5.3 para uma interface moderna e responsiva.

Funcionalidades
Adicionar livros com informações como título, autor, status de leitura e data de leitura.
Editar livros já cadastrados.
Excluir livros do catálogo.
Marcar livros como "lidos" ou "não lidos".
Tecnologias Utilizadas
Backend: Django 4.x
Frontend: Bootstrap 5.3
Banco de Dados: SQLite (padrão, pode ser alterado para outros bancos).
Instalação
Siga os passos abaixo para executar o projeto localmente.

1. Clonar o Repositório
bash
Copy code
git clone https://github.com/CelsoJr85/GerenciaLivros.git
cd gerenciador-livros
2. Configurar o Ambiente Virtual
Crie e ative o ambiente virtual:

bash
Copy code
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
3. Instalar as Dependências
Instale as dependências listadas no arquivo requirements.txt:

bash
Copy code
pip install -r requirements.txt
4. Configurar o Banco de Dados

Crie as migrações:
bash
Copy code
python manage.py makemigrations

Aplique as migrações:
bash
Copy code
python manage.py migrate

5. Iniciar o Servidor
bash
Copy code
python manage.py runserver
Acesse a aplicação em: http://127.0.0.1:8000/.

Como Usar
Acesse a página inicial para visualizar sua lista de livros.
Use o botão "Adicionar Livro" para inserir um novo livro.
Para cada livro listado:
Editar: Clique no botão "Editar" para alterar as informações do livro.
Excluir: Clique no botão "Excluir" para removê-lo.
Marcar como lido/não lido: Use o botão correspondente para atualizar o status de leitura.

Futuras Melhorias
Adicionar filtros para listar apenas livros lidos ou não lidos.
Implementar paginação para grandes listas de livros.
Permitir upload de imagens para cada livro.

Licença
Este projeto está licenciado sob a MIT License. Consulte o arquivo LICENSE para mais detalhes.
