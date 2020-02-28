FROM continuumio/miniconda3

ENTRYPOINT [ "/bin/bash", "-c" ]

EXPOSE 5000

COPY . /app

WORKDIR /app

RUN [ "conda", "env", "create"]

CMD ["source activate my_env_name && exec python main.py"]
