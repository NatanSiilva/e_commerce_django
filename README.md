## E-commerce Django
Este é um projeto de exemplo de um e-commerce desenvolvido em Django.

# Instalação
Para executar este projeto localmente, siga os passos abaixo:

- Clone este repositório:
git clone https://github.com/NatanSiilva/e_commerce_django.git

- Crie um ambiente virtual e ative-o:
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate

- Instale as dependências:
pip install -r requirements.txt

- Rode as migrações:
python manage.py migrate

- Crie um super usuário:
python manage.py createsuperuser

-Rode o servidor:
python manage.py runserver
Acesse o servidor em http://localhost:8000/.

# Funcionalidades
O e-commerce possui as seguintes funcionalidades:

- Autenticação e autorização de usuários.
- Cadastro e edição de produtos.
- Listagem de produtos com possibilidade de filtragem por nome e categoria.
- Adição de produtos ao carrinho.
- Remoção de produtos do carrinho.
- Visualização do carrinho e cálculo do total de compra.
- Finalização de compra (simulada).
- Histórico de compras para usuários logados.

#Endpoints
Os seguintes endpoints estão disponíveis:

|Método |Endpoint|Descrição |
|-------|--------|---------|
| GET   |/api/produtos/ |Retorna a lista de produtos |
| POST  |/api/produtos/ |Cria um novo produto |
| GET   |/api/produtos/{id}/ |Retorna os detalhes de um produto |
| PUT   |/api/produtos/{id}/ |Atualiza um produto existente |
| DELETE|/api/produtos/{id}/ |Deleta um produto existente |
| GET   |/api/carrinho/ |Retorna o conteúdo do carrinho |
| POST  |/api/carrinho/adicionar/{produto_id}/ |Adiciona um produto ao carrinho |
| POST  |/api/carrinho/remover/{produto_id}/ |Remove um produto do carrinho |
| GET   |/api/carrinho/finalizar/ |Finaliza o carrinho (simulado) |


# Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
