from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/clientes/{cliente_id}")
def get_cliente(cliente_id: int):
    # Simulação de banco de dados do serviço isolado
    if cliente_id == 1:
        return {"id": 1, "nome": "Cliente VIP", "status": "ativo"}
    raise HTTPException(status_code=404, detail="Cliente não encontrado")
