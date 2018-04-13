FROM jupyter/scipy-notebook

RUN git clone https://github.com/jhuapl-boss/intern.git && cd intern && git checkout RemoteExtension && git pull && python3 setup.py install --user
RUN conda install --yes -c ilastik-forge ilastik-dependencies-no-solvers
RUN conda install --yes --force libgfortran

RUN pip install mahotas
RUN conda install --yes --force scipy
RUN pip install ndparse

RUN echo Now run xBrainStart.py using 'python3 xBrainStart.py'
