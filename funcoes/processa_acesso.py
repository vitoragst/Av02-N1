import json
import time

def lambda_handler(event):
    """
    Simula uma função Lambda responsável por processar e validar o acesso
    de um cliente antes de enviar o pedido para a fila SQS (emulada).
    """
    print("🔹 Iniciando validação de acesso...")

    cliente = event.get("cliente")
    token = event.get("token")

    if not cliente or not token:
        print("❌ Acesso negado: dados incompletos.")
        return {"status": "erro", "mensagem": "Acesso negado."}

    if token != "12345-VALIDO":
        print(f"❌ Acesso negado: token inválido para o cliente {cliente}.")
        return {"status": "erro", "mensagem": "Token inválido."}

    time.sleep(1)

    print(f"✅ Acesso autorizado para o cliente: {cliente}")

    novo_evento = {
        "cliente": cliente,
        "pedido": event.get("pedido"),
        "autorizado": True,
        "timestamp": time.time()
    }

    return novo_evento
