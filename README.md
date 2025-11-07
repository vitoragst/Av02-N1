# Av02-N1
Projeto Av02-N1 
Sistema PedeFácil 

O processo se inicia quando o cliente envia uma requisição para o sistema por meio do API Gateway (app.py), informando o restaurante desejado, os itens do pedido e o nome do cliente. Essa requisição é recebida e o pedido é encaminhado para a Fila de Pedidos (SQS), onde aguarda processamento.

Em seguida, a função LambdaProcessarPedido é acionada para ler a fila e processar os pedidos pendentes. Essa função acessa o banco de dados DynamoDB (simulado por um arquivo JSON) para verificar se o restaurante solicitado existe e se está aberto. Caso o restaurante esteja disponível, a função confirma o pedido e o encaminha para a Fila de Entregas (SQS), simulando o repasse da solicitação ao restaurante responsável. Se o restaurante estiver fechado ou não for encontrado, a função retorna uma mensagem de erro ao sistema.

Depois disso, uma segunda função, chamada LambdaConfirmarEntrega, é responsável por consumir as mensagens da Fila de Entregas. Ela simula o processo de entrega do pedido, confirmando que o cliente recebeu o pedido e finalizando o fluxo de execução. Ao término, o sistema exibe uma mensagem de confirmação, como por exemplo: “O pedido foi entregue pelo restaurante!”

Durante todo o processo, as filas SQS garantem a comunicação assíncrona entre os componentes, evitando sobrecarga e permitindo que cada etapa do fluxo opere de forma independente. O uso de duas funções Lambda separadas segue o princípio da responsabilidade única: uma função é responsável apenas por processar o pedido e a outra por confirmar a entrega.

Essa arquitetura traz diversos benefícios, como escalabilidade, modularidade e facilidade de manutenção, uma vez que cada componente pode ser testado e evoluído isoladamente. Além disso, o modelo reflete práticas reais de sistemas em nuvem da AWS, mas de forma simplificada e completamente emulada localmente com Python.

Em resumo, o caso de uso “Realizar Pedido de Delivery” demonstra um fluxo de comunicação entre cliente, API Gateway, duas filas SQS, duas funções Lambda e um banco de dados DynamoDB. O sistema recebe o pedido, processa e valida as informações, envia o pedido para entrega e confirma sua conclusão, simulando o comportamento essencial de um aplicativo moderno de delivery baseado em arquitetura serverless.