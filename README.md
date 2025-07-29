# 📞 Integração MQTT com Asterisk usando Docker

Este projeto demonstra como integrar o protocolo MQTT com a central telefônica Asterisk, permitindo que chamadas VoIP sejam disparadas automaticamente por eventos internos. Todo o ambiente é construído e executado com Docker e Docker Compose.

---

## 🚀 Objetivo

- Demonstrar, de forma prática, a comunicação entre MQTT e Asterisk.
- Executar chamadas VoIP (Maria → Pedro) usando softphones.
- Criar um ambiente portátil, reprodutível e fácil de entender.

---

## 🧱 Estrutura do Projeto

```
projeto-mqtt-asterisk/
├── docker-compose.yml
├── asterisk/
│   ├── Dockerfile
│   └── configs/
│       ├── sip.conf
│       ├── extensions.conf
│       └── manager.conf
├── mqtt/
│   └── mosquitto.conf
└── mqtt-bridge/
    ├── Dockerfile
    └── mqtt_bridge.py
```

---

## 🧰 Tecnologias Utilizadas

- Docker e Docker Compose
- Asterisk (VoIP)
- Eclipse Mosquitto (Broker MQTT)
- Python 3 com `paho-mqtt`
- Softphones: Linphone e Zoiper

---

## ⚙️ Como Executar

### 1. Requisitos

- Docker
- Docker Compose
- Softphone instalado (Linphone e Zoiper)

### 2. Clonar e subir o ambiente

```bash
git clone https://github.com/ramonlbb/MQTT-com-Asterisk.git
cd projeto-mqtt-asterisk
docker compose up -d
```

### 3. Configurar os Softphones

Cadastre dois usuários SIP:

| Usuário | Senha | Domínio (IP da VM)     |
|--------|--------|-------------------------|
| maria  | 1234   | 192.168.x.x (da sua VM) |
| pedro  | 1234   | 192.168.x.x             |

- Maria → Disca `0800` → Chama Pedro  
- Pedro → Disca `0900` → Chama Maria

---

## 🔍 Explicação dos Arquivos

| Arquivo/Função | Descrição |
|----------------|-----------|
| `docker-compose.yml` | Orquestra os containers do projeto |
| `sip.conf` | Configura usuários SIP (maria e pedro) |
| `extensions.conf` | Define o plano de discagem (0800 e 0900) |
| `manager.conf` | Habilita acesso remoto via AMI (porta 5038) |
| `mqtt_bridge.py` | Script Python que escuta o tópico MQTT e envia comandos AMI |
| `mosquitto.conf` | Configuração básica do broker MQTT |

---

## 📌 Considerações

- O ambiente é isolado, seguro e fácil de replicar.
- A comunicação interna dos containers usa IPs da rede `172.18.0.0/16`.
- A interação principal foi feita entre o Linphone e o Zoiper, com chamadas reais via interface gráfica.

---

## 📄 Licença

Projeto acadêmico sem fins comerciais.

---

## ✉️ Autor

Desenvolvido por **Ramon Lucas** – Curso Redes de Computadores – IFPB
