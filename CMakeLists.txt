cmake_minimum_required(VERSION 3.28)
project(module_logger CXX)

set(CMAKE_CXX_SCAN_FOR_MODULES ON)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS ON)

add_library(module-logger::module-logger INTERFACE IMPORTED)

target_sources(module-logger::module-logger INTERFACE
    FILE_SET module_logger
    TYPE CXX_MODULES
    BASE_DIRS ${CMAKE_CURRENT_LIST_DIR}/lib/cxx/miu
    FILES ${CMAKE_CURRENT_LIST_DIR}/include/logger.mpp
)

set_target_properties(module-logger::module-logger PROPERTIES
    CXX_EXTENSIONS OFF
    IMPORTED_CXX_MODULES_COMPILE_FEATURES "cxx_std_20;cxx_std_11"
    IMPORTED_CXX_MODULES_INCLUDE_DIRECTORIES ${CMAKE_CURRENT_LIST_DIR}/include
    INTERFACE_INCLUDE_DIRECTORIES ${CMAKE_CURRENT_LIST_DIR}/include
    INTERFACE_COMPILE_FEATURES "cxx_std_20;cxx_std_11"
)
