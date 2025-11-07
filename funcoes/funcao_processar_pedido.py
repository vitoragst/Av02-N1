from utilitarios.gerenciador_restaurantes import buscar_restaurante
from fila.fila_entregas import enviar_entrega

def funcao_processar_pedido(evento):
    print(f"[Lambda 1] Processando pedido: {evento}")
    restaurante_nome = evento.get("restaurante")
    restaurante = buscar_restaurante(restaurante_nome)

    if not restaurante:
        return {"status": "erro", "mensagem": "Restaurante não encontrado."}

    if not restaurante["aberto"]:
        return {"status": "erro", "mensagem": f"O restaurante {restaurante_nome} está fechado."}

    print(f"[Lambda 1] Pedido aceito em {restaurante_nome}. Enviando para fila de entregas...")
    enviar_entrega(evento)

    return {"status": "sucesso", "mensagem": f"Pedido aceito em {restaurante_nome}!"}
