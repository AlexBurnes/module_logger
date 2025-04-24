
add_library(module-logger::module_logger INTERFACE IMPORTED)

set_property(
    TARGET module-logger::module-logger
    APPEND PROPERTY INTERFACE_LINK_LIBRARIES
)

set_property(
    TARGET module-logger::module-logger
    APPEND PROPERTY INTERFACE_INCLUDE_DIRECTORIES
    ${CMAKE_CURRENT_LIST_DIR}
)

