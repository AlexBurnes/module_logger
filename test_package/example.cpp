import logger;
#include <iostream>
#include <format>

int main() {

    logger l(std::cout);
    l.info() << std::format("test logger");

    return 0;
}
