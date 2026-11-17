# Changelog

Mudanças do projeto organizadas por módulo da disciplina. Cada módulo corresponde a uma branch do repositório (`modulo1`, `modulo2`, `modulo3`).

## Módulo 3: Contêineres

- Dockerfile para cada serviço (`servico-pedidos`, `servico-clientes`, `servico-produtos`), em dois estágios: um instala as dependências com `uv` a partir do `uv.lock` e o outro, enxuto, recebe só o ambiente virtual e o código.
- Os contêineres rodam com um usuário sem privilégios (`app`, UID 1000), não como root.
- `.dockerignore` em cada serviço.
- `docker-compose.yml` na raiz com os três serviços e o banco PostgreSQL (`postgres:18-alpine`), mais o volume nomeado `pgdata` para guardar os dados.
- Healthchecks no banco (`pg_isready`) e nos três serviços. O `servico-pedidos` só sobe depois que o banco e o `servico-clientes` estão saudáveis.
- Só o `servico-pedidos` publica porta, e apenas em `127.0.0.1:8000`. Os demais ficam acessíveis somente pela rede interna do Compose.
- Limite de memória, `cap_drop: ALL` e `no-new-privileges` nos serviços da aplicação.
- O `servico-pedidos` aplica as migrações ao iniciar e passa a rodar com `gunicorn` (adicionado como dependência).
- Configuração sensível do `servico-pedidos` lida do ambiente: `SECRET_KEY`, `DEBUG` (desligado por padrão) e `ALLOWED_HOSTS`, além da URL do serviço de clientes (`CLIENTES_URL`).
- `.env.example` com as variáveis que o Compose espera.

## Módulo 2: Microsserviços e comunicação síncrona

- O projeto foi reorganizado em monorepo, com uma pasta por serviço: `servico-pedidos` (Django/DRF, o código do Módulo 1), `servico-clientes` (FastAPI) e `servico-produtos` (FastAPI).
- O `servico-pedidos` consulta o `servico-clientes` por HTTP de forma síncrona ao criar um pedido, com timeout de 3 segundos. Se o serviço de clientes estiver indisponível, responde `503 Service Unavailable`.
- A URL do serviço de clientes passou a apontar para a instância publicada no Render.
- Deploy automático dos três serviços no Render por GitHub Actions, acionando os deploy hooks a cada push em `main` e `modulo2`.
- Diagrama da arquitetura (`arquitetura.svg` / `arquitetura.png`) e documentação do módulo no README.

## Módulo 1: Computação em nuvem

- API REST de pedidos em Django com Django REST Framework, sobre PostgreSQL.
- Modelos `Order` (cliente, status e data de criação) e `OrderItem` (produto e quantidade), com endpoints CRUD em `/api/orders/`.
- Criação e edição dos itens junto com o pedido.
- Credenciais do banco lidas de variáveis de ambiente (`POSTGRES_*`) e um `compose.yaml` só com o PostgreSQL para desenvolvimento local (hoje em `servico-pedidos/compose.yaml`).
- Modelagem inicial do banco em DBML com imagem do diagrama.
- API publicada no Render, com o banco PostgreSQL no Neon, e `ALLOWED_HOSTS` ajustado para o domínio do Render.
- README com o link da API pública, os vídeos de demonstração e a justificativa da arquitetura.
