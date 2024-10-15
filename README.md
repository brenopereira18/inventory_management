📦 Stockify - Sistema de Gerenciamento de Estoque



📋 Descrição
O Stockify é uma plataforma completa para gerenciamento de estoque, que permite a administração eficiente de produtos, marcas, fornecedores e categorias. A aplicação inclui funcionalidades avançadas como grupos de permissões de usuários, gráficos interativos e uma API pública para integração com outros sistemas.

🚀 Funcionalidades
CRUD Completo:
Marcas, categorias, fornecedores, entradas e saídas de produtos.
Cadastro de produtos vinculando a marca, fornecedor e categoria.
Filtros de Busca:
Por nome do produto e número de série.
Filtro por marca e categoria específica.
Grupos de Permissões:
Acesso restrito por nível de usuário.
Dashboard com gráficos interativos:
Vendas dos últimos 7 dias.
Quantidade de produtos por categoria.
Quantidade de produtos por marca.
API REST disponível para integração.
🛠️ Tecnologias Utilizadas
Backend: Python, Django, Django Rest Framework
Frontend: Bootstrap
Gráficos: Chart.js
Banco de Dados: PostgreSQL
Autenticação: JWT
Servidores: uWSGI e Nginx
Deploy: AWS EC2
📊 Gráficos no Dashboard
Vendas nos últimos 7 dias
Distribuição de produtos por categoria
Quantidade de produtos por marca
🛠️ Instalação e Execução Local
Pré-requisitos
Python 3.8+
PostgreSQL
Git
Passo a Passo
Clone o repositório:

bash
Copiar código
git clone https://github.com/brenopereira18/inventory_management.git
cd inventory_management
Crie e ative um ambiente virtual:

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Configure o banco de dados PostgreSQL no arquivo .env:

text
Copiar código
DB_NAME=seu_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
Aplique as migrações:

bash
Copiar código
python manage.py migrate
Inicie o servidor local:

bash
Copiar código
python manage.py runserver
🌐 API Endpoints
GET /api/produtos/ – Listar todos os produtos
POST /api/produtos/ – Cadastrar um novo produto
PUT /api/produtos/{id}/ – Atualizar um produto
DELETE /api/produtos/{id}/ – Deletar um produto
GET /api/produtos/?nome=xyz – Buscar produtos por nome
Mais detalhes sobre a API estão disponíveis na documentação do projeto.

🛡️ Segurança e Autenticação
Autenticação JWT para proteger endpoints.
Grupos de usuários com permissões específicas.
🚀 Deploy na AWS EC2
O projeto foi implantado na AWS EC2 usando Nginx e uWSGI para garantir escalabilidade e alta disponibilidade.

📄 Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais informações.

👥 Contribuição
Sinta-se à vontade para contribuir com este projeto! Basta seguir estes passos:

Faça um fork do projeto.
Crie uma branch para sua funcionalidade (git checkout -b feature/sua-feature).
Faça o commit (git commit -m 'Adiciona nova funcionalidade').
Envie para o repositório (git push origin feature/sua-feature).
Abra um Pull Request.
📝 To-Do List
 Implementar exportação de relatórios em PDF.
 Adicionar suporte a múltiplos idiomas.
 Melhorar testes unitários e de integração.
📬 Contato
Se você tiver dúvidas ou sugestões, entre em contato comigo:

LinkedIn: Breno Pereira
Email: brenopereira@example.com
