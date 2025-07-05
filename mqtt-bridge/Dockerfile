FROM python:3.10-slim

RUN pip install paho-mqtt

COPY mqtt_bridge.py /mqtt_bridge.py

CMD ["python", "/mqtt_bridge.py"]