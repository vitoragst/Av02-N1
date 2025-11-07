def funcao_confirmar_entrega(evento):
    print(f"[Lambda 2] Confirmando entrega do pedido: {evento}")
    cliente = evento.get("cliente")
    restaurante = evento.get("restaurante")

    return {
        "status": "entregue",
        "mensagem": f"O pedido de {cliente} foi entregue pelo restaurante {restaurante}!"
    }
