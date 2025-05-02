# C++20 modules, conan package module logger

Conan library as C++20 module.

# Requirements

* CMake >= 3.28
* ninja >= 1.11.1
* clang >= 19
* conan >= 2.16

# Install

## Conan

    git clone https://github.com/conan-io/conan.git conan-io
    cd conan-io
    sudo pip install -e .

## Clang

    sudo apt install clang-19 clang-tools-19
    bash update-alternatives-clang.sh 19 19

Set clang alternative

    update-alternatives --config clang

## Other requirements

No need to build and install CMake and ninja, conan will install and used then, see conanfile.py and build scripts how to do it.

# Build

    bash build



