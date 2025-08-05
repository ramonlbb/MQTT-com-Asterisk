# Usamos a imagem base universal do Debian
FROM debian:bullseye-slim

# Evita que a instalação peça inputs do usuário
ENV DEBIAN_FRONTEND=noninteractive

# Instala Asterisk, PACOTE DE SOM, Python e PIP
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    asterisk \
    asterisk-core-sounds-en-gsm \
    python3 \
    python3-pip

# Instala a biblioteca MQTT para Python
RUN pip3 install paho-mqtt

# Copia nossos arquivos de configuração e scripts para os locais corretos
COPY conf/pjsip.conf /etc/asterisk/pjsip.conf
COPY conf/extensions.conf /etc/asterisk/extensions.conf

# Copia o script para o diretório correto que a versão Debian do Asterisk espera
COPY agi/publish_call_event.py /usr/share/asterisk/agi-bin/publish_call_event.py
RUN chmod +x /usr/share/asterisk/agi-bin/publish_call_event.py

# Comando para iniciar o Asterisk em modo "foreground"
CMD ["asterisk", "-f"]
