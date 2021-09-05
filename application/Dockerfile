ARG PythonVersion
FROM python:${PythonVersion}

ARG ContainerMountpointApplication
WORKDIR $ContainerMountpointApplication

COPY ./requirements.txt ${ContainerMountpointApplication}/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ${ContainerMountpointApplication}/requirements.txt

COPY ./app ${ContainerMountpointApplication}/app

CMD ["uvicorn", "app.api:act", "--host", "0.0.0.0", "--port", "80"]
