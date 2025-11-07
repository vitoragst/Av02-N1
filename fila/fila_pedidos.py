from queue import Queue

fila_pedidos = Queue()

def enviar_pedido(mensagem):
    print(f"[SQS Pedido] Pedido enviado: {mensagem}")
    fila_pedidos.put(mensagem)

def receber_pedido():
    if not fila_pedidos.empty():
        msg = fila_pedidos.get()
        print(f"[SQS Pedido] Pedido recebido: {msg}")
        return msg
    return None
