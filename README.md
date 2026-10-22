# Sistema de Pedidos de E-commerce Simplificado

Repositório do projeto da disciplina de Sistemas Distribuídos - 3ª Unidade.

## Módulo 1: Computação em Nuvem

**Acesso à API Pública:** [https://ecommerce-sd.onrender.com/api/orders/](https://ecommerce-sd.onrender.com/api/orders/)

### Links dos Vídeos de Demonstração
- **Demonstrações (Pasta do Drive):** [Acessar os vídeos do Mateus e do Diego](https://drive.google.com/drive/folders/1lScf9nFotYTD9e5TKSHH85W4c8RrAlvt?usp=sharing)

### Justificativa Técnica (Arquitetura)
Para a primeira etapa do projeto, adotamos a seguinte arquitetura em nuvem:
- **Aplicação (PaaS):** Utilizamos o **Render** para hospedar nossa API REST em Django. O Render permite deploy direto do código-fonte no GitHub e facilita a configuração das variáveis de ambiente (`DATABASE_URL`, `SECRET_KEY`, `ALLOWED_HOSTS`), mantendo as credenciais seguras e fora do código-fonte.
- **Banco de Dados (DBaaS):** Utilizamos o **Neon** para o banco de dados PostgreSQL em nuvem. Ele oferece instâncias *serverless* rápidas de configurar e nos fornece uma *Connection String* simples para integrar com a nossa aplicação no Render de forma completamente isolada.

### Como executar o projeto localmente
1. Clone o repositório e acesse a pasta:
   ```bash
   git clone https://github.com/M2004GV/ecommerce-sd.git
   cd ecommerce-sd