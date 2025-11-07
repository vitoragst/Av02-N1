from queue import Queue

fila_entregas = Queue()

def enviar_entrega(mensagem):
    print(f"[SQS Entrega] Pedido enviado para entrega: {mensagem}")
    fila_entregas.put(mensagem)

def receber_entrega():
    if not fila_entregas.empty():
        msg = fila_entregas.get()
        print(f"[SQS Entrega] Entrega recebida: {msg}")
        return msg
    return None
