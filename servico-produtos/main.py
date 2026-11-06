from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/produtos/{produto_id}")
def get_produto(produto_id: int):
    # Simulação de banco de dados do serviço isolado
    if produto_id == 1:
        return {"id": 1, "nome": "Notebook Linux", "estoque": 10}
    raise HTTPException(status_code=404, detail="Produto não encontrado")
