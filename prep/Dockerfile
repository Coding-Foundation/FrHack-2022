FROM python

COPY . /opt/lab
WORKDIR /opt/lab
RUN pip install jupyterlab

ENTRYPOINT [ "jupyter-lab", "--ip", "0.0.0.0", "--collaborative", "--allow-root" ]
