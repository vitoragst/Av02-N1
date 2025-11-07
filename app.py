from fila.fila_pedidos import enviar_pedido, receber_pedido
from fila.fila_entregas import receber_entrega
from funcoes.funcao_processar_pedido import funcao_processar_pedido
from funcoes.funcao_confirmar_entrega import funcao_confirmar_entrega

def gateway_api(evento):
    rota = evento.get("rota")

    if rota == "/novo-pedido":
        enviar_pedido(evento)
        return {"status": "Pedido enviado", "pedido": evento}

    elif rota == "/processar-pedidos":
        msg = receber_pedido()
        if msg:
            return funcao_processar_pedido(msg)
        else:
            return {"status": "Fila de pedidos vazia"}

    elif rota == "/processar-entregas":
        msg = receber_entrega()
        if msg:
            return funcao_confirmar_entrega(msg)
        else:
            return {"status": "Fila de entregas vazia"}

    else:
        return {"erro": "Rota não encontrada"}

if __name__ == "__main__":
    pedido = {
        "rota": "/novo-pedido",
        "cliente": "Vitor",
        "restaurante": "Burger Town",
        "itens": ["X-Burger", "Refrigerante"]
    }

    print(gateway_api(pedido))
    print(gateway_api({"rota": "/processar-pedidos"}))
    print(gateway_api({"rota": "/processar-entregas"}))
