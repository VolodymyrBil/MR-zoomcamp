FROM python:3.11-bookworm

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["model_xgb.bin", "use_model.py", "./"]

EXPOSE 9696

ENTRYPOINT [ "waitress-serve", "--listen=*:9696", "use_model:app" ]


# docker run -it --rm -p 9696:9696 income_predict

