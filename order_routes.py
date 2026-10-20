from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=["order"])

# Criar um rota no FastAPI
@order_router.get("/") # http://127.0.0.1:8000/order/
async def orders():
    return { "message": "You have just accessed the order routes."}
