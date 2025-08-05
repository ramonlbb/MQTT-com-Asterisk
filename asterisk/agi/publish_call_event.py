#!/usr/bin/env python3

import sys
import paho.mqtt.client as mqtt
import json

# --- Configurações ---
MQTT_BROKER_HOST = "mosquitto"  # Nome do serviço no docker-compose
MQTT_BROKER_PORT = 1883
MQTT_TOPIC = "asterisk/events/call"

def main():
    """
    Função principal para conectar ao MQTT e publicar a mensagem.
    """
    # O Asterisk passa variáveis de canal como argumentos de linha de comando.
    # O primeiro argumento (sys.argv[1]) será o CallerID que passamos no dialplan.
    if len(sys.argv) < 2:
        print("Erro: Nenhum CallerID foi passado para o script AGI.", file=sys.stderr)
        sys.exit(1)

    caller_id = sys.argv[1]

    # Monta a mensagem que será enviada
    message = {
        "event": "IncomingCall",
        "caller_id": caller_id
    }
    payload = json.dumps(message)

    try:
        # Cria o cliente MQTT
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

        # Conecta ao broker
        client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)

        # Publica a mensagem no tópico
        client.publish(MQTT_TOPIC, payload)

        # Desconecta
        client.disconnect()

        # Log para o console do Asterisk para fins de depuração
        print(f"AGI: Mensagem publicada com sucesso no tópico '{MQTT_TOPIC}': {payload}", file=sys.stderr)

    except Exception as e:
        # Em caso de erro, loga no console do Asterisk
        print(f"AGI Error: Falha ao conectar ou publicar no MQTT. Erro: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
