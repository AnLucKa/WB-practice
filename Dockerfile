FROM  python:3.10

RUN mkdir -p usr/src/app/my_python_app

WORKDIR /usr/src/app/my_python_app

COPY ./my_python_app /usr/src/app/my_python_app

RUN pip install clickhouse-driver[lz4,zstd]
RUN pip install pandas
RUN pip install numpy

CMD [ "python", "-u", "main.py"]



