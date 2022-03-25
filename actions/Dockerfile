FROM rasa/rasa-sdk:2.4.1

WORKDIR /app

USER root

COPY . /app/actions

USER 1001

ENTRYPOINT []

CMD python3 -m rasa-sdk --actions actions -p $PORT
