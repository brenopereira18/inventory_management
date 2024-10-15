

# 📦 Stockify - Sistema de Gerenciamento de Estoque

O Stockify é uma plataforma completa para gerenciamento de estoque, que permite a administração eficiente de produtos, marcas, fornecedores e categorias. A aplicação inclui funcionalidades avançadas como grupos de permissões de usuários, gráficos interativos e uma API pública para integração com outros sistemas


## 🚀 Funcionalidades

- CRUD de marcas, categorias, fornecedores e cadastro entradas e saídas de produtos.
- CRUD de produtos, com a possibilidade de vincular fornecedor, marca e categoria.
- Controle de Permissões: Diferentes grupos de usuários com acesso restrito conforme suas permissões.
- Filtro de busca de produtos pelo nome, número de série, por marca e categoria.
- Relatórios com atualização em tempo real, como quantidade de produtos, custo, valor e lucro do estoque, além de quantidade de vendas, produtos vendidos, valor e lucro das vendas.
- API REST disponível para integração.


## 📊 Gráficos no Dashboard

Utilizei Chart.js para criar gráficos dinâmicos que fornecem uma visão clara das operações:

- Valor de venda do dia, dos últimos 7 dias.
- Quantidade de produtos vendidos por dia.
- Quantidade de produtos por categoria.
- Quantidade de produtos por marca.




## 🛠️ Tecnologias Utilizadas

**Back-end:** Python, Django, Django Rest Framework

**Front-end:** Bootstrap

**Gráficos:** Chart.js

**Banco de Dados:** PostgreSQL

**Autenticação:** JWT

**Servidores:** uWSGI e Nginx

**Deploy:** AWS EC2


## 🛠️ Instalação e Execução Local

Pré-requisitos: Python 3.8+, PostgreSQL

1. Clone o repositório:
```bash
git clone https://github.com/brenopereira18/inventory_management.git
cd inventory_management
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o banco de dados PostgreSQL no arquivo app/settings.py:
```bash
DB_NAME=seu_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
```

5. Aplique as migrações:
```bash
python manage.py migrate
```

6. Inicie o servidor local:
```bash
python manage.py runserver

```
## 🌐 API Endpoints

- GET /api/produtos/ – Listar todos os produtos
- POST /api/produtos/ – Cadastrar um novo produto
- PUT /api/produtos/{id}/ – Atualizar um produto
- DELETE /api/produtos/{id}/ – Deletar um produto
- GET /api/produtos/?nome=xyz – Buscar produtos por nome
## 🛡️ Segurança e Autenticação

- Autenticação JWT para proteger endpoints.
- Grupos de usuários com permissões específicas.
## 🚀 Deploy na AWS EC2

- O projeto foi implantado na AWS EC2 usando Nginx e uWSGI para garantir escalabilidade e alta disponibilidade.
## Acessando o Stockify

Obs: Utilize o usuário e a senha a seguir para ter acesso a visualização ao site.

- User: userView
- Password: view2001

[Stockify](http://3.220.238.18)
