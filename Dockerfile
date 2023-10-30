FROM python:3.10.6
LABEL creator="hongchenker" email="hongchenker@yeah.net"

WORKDIR /app

COPY . .
RUN pip install --upgrade pip \
    && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt \
    && chmod +x entrypoint.sh

ENTRYPOINT ["bash", "entrypoint.sh"]
EXPOSE 8062
CMD ["http"]