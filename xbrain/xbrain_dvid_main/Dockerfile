FROM jupyter/scipy-notebook

USER root

#Sets up the repository
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y sysvinit-utils
RUN apt-get install -y apt-transport-https
RUN apt-get install -y ca-certificates
RUN apt-get install -y software-properties-common
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

#Stable repository
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

#Installing docker CE
RUN apt-get update
RUN apt-get install -y docker-ce

#Installing intern
RUN git clone https://github.com/jhuapl-boss/intern.git && cd intern && git checkout RemoteExtension && git pull && python3 setup.py install --user

#Loads Dvid public data
RUN git clone https://github.com/aplbrain/repetir.git && cd xbrain/xbrain_dvid_main && python3 xBrainStart.py

RUN echo Check localhost 8000 and 8888.
