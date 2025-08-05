Claro! Aqui está o conteúdo reorganizado e formatado para um `README.md` mais elegante e visualmente agradável no GitHub — mas **sem alterar o conteúdo original** conforme solicitado:

````markdown
# 📞 Integração Asterisk e MQTT com Docker

Este é um projeto de **prova de conceito** que demonstra como integrar um PABX VoIP Asterisk com um broker MQTT. A solução é totalmente orquestrada com Docker e Docker Compose, garantindo um ambiente de fácil replicação e portabilidade.

---

## 🚀 O Que o Projeto Faz?

O objetivo principal é capturar um evento de chamada telefônica no Asterisk e publicá-lo como uma mensagem estruturada (JSON) em um tópico MQTT em tempo real.

### 🔁 Fluxo da Integração

1. Um telefone SIP (ramal `1000`) liga para uma extensão de gatilho (`888`);
2. O Asterisk atende a chamada e executa um script AGI (Asterisk Gateway Interface) em Python;
3. O script Python se conecta ao broker MQTT e publica os detalhes da chamada;
4. Qualquer sistema ou cliente inscrito no tópico MQTT recebe a notificação instantaneamente.

---

## 🎯 Para Que Serve? (Casos de Uso)

Esta arquitetura serve como base para diversas aplicações do mundo real, como:

- 📊 **Dashboards de Atendimento:** Monitoramento do fluxo de chamadas em tempo real;
- 🏠 **Automação e IoT:** Usar chamadas como gatilhos para ações físicas (abrir portão, acender luzes, etc.);
- 🔗 **Integração com Sistemas:** Envio de notificações para CRMs, helpdesk, Slack, Teams e outros;
- 📈 **Análise de Dados:** Registro simplificado de eventos de chamada para relatórios e BI.

---

## 🧰 Pré-requisitos

Certifique-se de ter as ferramentas abaixo instaladas:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## 📁 Estrutura dos Arquivos

```text
.
├── docker-compose.yml
├── mosquitto
│   └── conf
│       └── mosquitto.conf
└── asterisk
    ├── Dockerfile
    ├── agi
    │   └── publish_call_event.py
    └── conf
        ├── extensions.conf
        └── pjsip.conf
````

---

## 🧪 Como Replicar o Ambiente

### 🔹 Passo 1: Obtenha os Arquivos

Clone este repositório (ou crie manualmente a estrutura de arquivos):

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 🔹 Passo 2: Inicie o Ambiente Docker

Na raiz do projeto, execute:

```bash
docker-compose up --build -d
```

> ℹ️ A flag `--build` é necessária na primeira execução ou após alterações. O processo pode levar alguns minutos, pois instalará o Asterisk e suas dependências.

---

## ✅ Como Testar a Integração

### 1. Configure seu Softphone

Utilize qualquer cliente SIP (Zoiper, Linphone etc.) com as seguintes credenciais:

* **Usuário/Username:** `1000`
* **Senha/Password:** `1234`
* **Servidor:** IP da máquina onde o Docker está rodando

### 2. Inicie o Ouvinte MQTT

Em uma nova janela de terminal, execute:

```bash
docker run -it --rm --network host eclipse-mosquitto:2.0 mosquitto_sub -h localhost -t "asterisk/events/call" -v
```

Este terminal servirá como monitor de eventos MQTT.

### 3. Realize a Chamada de Teste

Do softphone, disque a extensão `888`. Você ouvirá o áudio “Hello World” e a chamada será finalizada automaticamente.

---

## 📬 Resultado Esperado

No terminal com o `mosquitto_sub`, a seguinte mensagem deverá aparecer:

```json
asterisk/events/call {"event": "IncomingCall", "caller_id": "1000"}
```

---

Pronto! Com isso, o ambiente está configurado e a integração entre Asterisk e MQTT funcionando corretamente.
