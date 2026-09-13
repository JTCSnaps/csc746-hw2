FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install core build toolchains, CMake, archiving tools, and SSH utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    g++ \
    gcc \
    gdb \
    cmake \
    make \
    git \
    rsync \
    openssh-client \
    zip \
    unzip \
    tar \
    libopenblas-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

CMD ["/bin/bash"]