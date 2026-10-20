# ecommerce-sd
Projeto de ecommerce simplificado (sem integração com APIs de pagamento) desenvolvido para a disciplina de sistemas distribuídos como atividade avaliativa da última unidade

## Banco de dados local

O PostgreSQL roda num container, só ele. A aplicação continua no host, com `uv`.

```bash
cp .env.example .env     # ajuste a senha se quiser
docker compose up -d --wait
```

O `settings.py` lê as credenciais do ambiente, então os comandos do Django
passam pelo `.env`:

```bash
uv run --env-file .env python manage.py migrate
uv run --env-file .env python manage.py runserver
```

Sem o `--env-file`, o `settings.py` falha de propósito com `KeyError`, para não
cair num banco padrão por engano. Para abrir o `psql`:

```bash
docker compose exec db psql -U ecommerce_sd -d ecommerce_sd
```
