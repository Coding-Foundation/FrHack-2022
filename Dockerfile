FROM python

WORKDIR /home/lab
RUN pip install jupyterlab

ENTRYPOINT [ "jupyter-lab", "--ip", "0.0.0.0", "--collaborative", "--allow-root" ]
