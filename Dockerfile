FROM debian:latest AS build

RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y clang
RUN apt-get install -y gdb
RUN apt-get install -y curl
RUN apt-get install -y wget
RUN apt-get -y install python3-pip
RUN pip install conan --upgrade
RUN pip install cmake --upgrade
WORKDIR /app
COPY . .
# RUN conan profile update settings.compiler.libcxx=libstdc++11 default

RUN ls
# RUN rm CMakeCache.txt
RUN conan install . --install-folder lib --output-folder ./lib/packages
RUN cmake .
RUN make
RUN ls
RUN pwd
CMD [ "python3", "./build_sys/alive.py" ]
# RUN ./bin/sll