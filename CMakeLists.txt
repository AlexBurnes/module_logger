cmake_minimum_required(VERSION 3.28)
project(module_logger CXX)

set(CMAKE_CXX_SCAN_FOR_MODULES ON)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS ON)

add_library(logger)

target_sources(
    logger PUBLIC
    FILE_SET logger
    TYPE CXX_MODULES
    FILES include/logger.mpp
)

set_target_properties(
    logger PROPERTIES
    LINKER_LANGUAGE CXX
    CXX_EXTENSIONS ON
    IMPORTED_CXX_MODULES_COMPILE_FEATURES "cxx_std_20"
    IMPORTED_CXX_MODULES_INCLUDE_DIRECTORIES ${CMAKE_CURRENT_LIST_DIR}/include
    INTERFACE_INCLUDE_DIRECTORIES ${CMAKE_CURRENT_LIST_DIR}/include
    INTERFACE_COMPILE_FEATURES "cxx_std_20"
)

add_library(module-logger::module-logger ALIAS logger)

install(
    TARGETS logger
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)
