cmake_minimum_required(VERSION 3.28)
project(module_logger CXX)

set(CMAKE_CXX_SCAN_FOR_MODULES ON)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS ON)

add_library(module_logger)
target_sources(
    module_logger
    PUBLIC
        FILE_SET CXX_MODULES FILES
        include/logger.mpp
)

add_library(module-logger::module-logger INTERFACE IMPORTED)

set_property(
    TARGET module-logger::module-logger
    APPEND PROPERTY INTERFACE_LINK_LIBRARIES
    logger
)

set_property(
    TARGET module-logger::module-logger
    APPEND PROPERTY INTERFACE_INCLUDE_DIRECTORIES
    ${CMAKE_CURRENT_LIST_DIR}/include
)
