# Trabalho-Fabricio
# Projeto de Cadastro de Eventos

Este projeto é uma API de cadastro de eventos e participantes utilizando Django Rest Framework. Com ele, você pode criar e gerenciar eventos, bem como adicionar participantes a esses eventos.

## Requisitos

Antes de testar o projeto, verifique se você possui os seguintes requisitos:

- Python 3.x
- Django 3.x ou superior
- Django Rest Framework
- Insomnia (ou Postman)

## Instalação

1. **Clone o repositório:**
   Se você ainda não clonou o repositório, use o seguinte comando:

   ```bash
   git clone https://seu-repositorio-url.git
Instale as dependências:

Navegue até o diretório do projeto e instale as dependências necessárias utilizando pip:


cd nome-do-projeto
pip install -r requirements.txt
Aplicar migrações:

Certifique-se de que o banco de dados está atualizado executando as migrações:

python manage.py migrate
Inicie o servidor de desenvolvimento:

Para rodar a API, inicie o servidor de desenvolvimento do Django:

python manage.py runserver
O servidor estará disponível em http://127.0.0.1:8000/.

Usando o Insomnia para testar a API
1. Configurando o Insomnia
Abra o Insomnia e crie uma nova Request (requisição).
Selecione o tipo da requisição (GET, POST, PUT, DELETE) dependendo da operação que você deseja realizar.
2. Endpoints disponíveis
GET /api/eventos/: Obtém todos os eventos cadastrados.

Método: GET
URL: http://127.0.0.1:8000/api/eventos/
POST /api/eventos/: Cria um novo evento.

Método: POST
URL: http://127.0.0.1:8000/api/eventos/
Corpo da requisição (JSON):

{
  "nome": "Evento de Teste",
  "data_inicio": "2024-12-01T10:00:00Z",
  "data_fim": "2024-12-01T18:00:00Z",
  "local": "Local de Teste"
}
GET /api/eventos/{id}/: Obtém os detalhes de um evento específico.

Método: GET
URL: http://127.0.0.1:8000/api/eventos/{id}/
POST /api/participantes/: Adiciona um participante a um evento.

Método: POST
URL: http://127.0.0.1:8000/api/participantes/
Corpo da requisição (JSON):

{
  "nome": "João da Silva",
  "email": "joao@exemplo.com",
  "evento": 1
}
GET /api/participantes/: Obtém todos os participantes.

Método: GET
URL: http://127.0.0.1:8000/api/participantes/
DELETE /api/participantes/{id}/: Remove um participante do evento.

Método: DELETE
URL: http://127.0.0.1:8000/api/participantes/{id}/
3. Testando no Insomnia
Para adicionar um novo evento:
Selecione o método POST e insira a URL: http://127.0.0.1:8000/api/eventos/.
No corpo da requisição, adicione os dados do evento em formato JSON.
Clique em "Send" (Enviar) e você verá a resposta do servidor com os dados do evento criado.
Para visualizar todos os eventos:
Selecione o método GET e insira a URL: http://127.0.0.1:8000/api/eventos/.
Clique em "Send" para obter a lista de eventos.
Para adicionar um participante:
Selecione o método POST e insira a URL: http://127.0.0.1:8000/api/participantes/.
No corpo da requisição, adicione os dados do participante (incluindo o ID do evento a que ele pertence).
Clique em "Send" para adicionar o participante ao evento.
Para visualizar todos os participantes:
Selecione o método GET e insira a URL: http://127.0.0.1:8000/api/participantes/.
Clique em "Send" para visualizar todos os participantes cadastrados.
Para excluir um participante:
Selecione o método DELETE e insira a URL: http://127.0.0.1:8000/api/participantes/{id}/, substituindo {id} pelo ID do participante a ser excluído.
Clique em "Send" para excluir o participante.
