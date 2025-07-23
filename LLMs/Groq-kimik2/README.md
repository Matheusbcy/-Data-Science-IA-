# Demonstração Simples de Uso da API Groq para Geração de Texto

Este projeto apresenta um exemplo básico de como utilizar a API Groq para realizar uma geração de texto (chat completion) com streaming, exibindo a resposta em tempo real no terminal.

---

## Objetivo

O objetivo é demonstrar, de forma simples, como conectar-se à API Groq, enviar uma mensagem para um modelo de linguagem, e receber a resposta gerada incrementalmente, permitindo a impressão do texto conforme ele é produzido.

---

## Funcionamento

1. O código começa carregando as variáveis de ambiente de um arquivo `.env`, garantindo que o token de autenticação da API Groq esteja disponível.

2. É configurada a saída padrão para suportar a codificação UTF-8, para que caracteres especiais sejam exibidos corretamente no terminal.

3. Em seguida, é criado um cliente para a API Groq, que gerencia a comunicação com o serviço de geração de texto.

4. O cliente realiza uma chamada de chat completion para um modelo específico, enviando uma mensagem de usuário como entrada.

5. O modo streaming é ativado para que a resposta seja recebida em pedaços incrementais.

6. Cada pedaço de texto gerado é impresso no terminal assim que chega, permitindo que o usuário acompanhe a resposta em tempo real.

---

## Requisitos

- Ter uma conta e chave de API válida no serviço Groq.
- Ter um arquivo `.env` configurado contendo a chave da API.
- Um ambiente Python configurado com as bibliotecas necessárias para executar o código.

---

## Pontos importantes

- O uso do modo streaming proporciona uma experiência mais dinâmica, com resposta parcial sendo exibida conforme o modelo gera o texto.
- A configuração da codificação UTF-8 evita problemas na exibição de caracteres acentuados e especiais.
- O exemplo utiliza um modelo pré-existente chamado `moonshotai/kimi-k2-instruct`, que pode ser substituído conforme a disponibilidade e permissões do usuário.

---

## Conclusão

Este exemplo serve como base para aplicações que desejam integrar geração de texto com streaming em Python utilizando a API Groq, demonstrando os passos essenciais para autenticação, envio de prompt, recepção incremental e exibição do resultado de forma correta e eficiente.
