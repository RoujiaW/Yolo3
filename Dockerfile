From tensorflow/tensorflow:1.15.0-jupyter
RUN apt-get update -y
RUN apt-get install -y git wget
RUN pip3 install keras==2.2.4