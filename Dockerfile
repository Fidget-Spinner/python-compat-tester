FROM fedora:43

RUN dnf install rpmbuild -y
RUN mkdir /pypy
WORKDIR /pypy
RUN curl https://downloads.python.org/pypy/pypy3.11-v7.3.20-linux64.tar.bz2 -o ./pypy3.11-v7.3.20.tar.bz2
RUN tar -xvjf pypy3.11-v7.3.20.tar.bz2
RUN alternatives --install /bin/python python /pypy/pypy3.11-v7.3.20-linux64/bin/python 1
RUN alternatives --install /bin/python3 python3 /pypy/pypy3.11-v7.3.20-linux64/bin/python 0


