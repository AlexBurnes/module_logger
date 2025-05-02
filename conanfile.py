from conan import ConanFile
from conan.tools.build import check_max_cppstd, check_min_cppstd
from conan.tools.cmake import CMakeToolchain, CMake, CMakeDeps, cmake_layout
from conan.tools.files import copy, rmdir

import os

class module_loggerConanRecipe(ConanFile):
    name = "module-logger"
    version = "0.1.0"
    package_type = "library"

    license = "Svyazcom LCC"
    author = "Aleksey.Ozhigov <burnes@svyazcom.ru>"
    url = "https://github.com/AlexBurnes/module_logger.git"
    description = "C++20 module prefix library example"
    topics = ("Common", "logger")

    settings = "os", "compiler", "build_type", "arch"

    exports_sources = "CMakeLists.txt", "src/*"

    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def build_requirements(self):
        self.tool_requires("cmake/3.28.1")
        self.tool_requires("ninja/1.11.1")

    def validate(self):
        check_min_cppstd(self, "20")
        check_max_cppstd(self, "23")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        copy(self, "logger.pcm", src=os.path.join(self.build_folder, "CMakeFiles", "logger.dir"), dst=os.path.join(self.package_folder, "bmi"))

    def package(self):
        cmake = CMake(self)
        cmake.install()
        #copy(self, "*.mpp", self.source_folder, self.package_folder)
        #copy(self, "logger.pcm", src=os.path.join(self.build_folder, "CMakeFiles", "logger.dir"), dst=os.path.join(self.package_folder, "bmi"))

    def package_info(self):
        self.cpp_info.libs = ["logger"]
        self.cpp_info.includedirs = []
        self.cpp_info.libdirs = ["lib"]
        if self.settings.compiler == "clang":
            self.cpp_info.cxxflags = [f"-fmodule-file=logger={self.package_folder}/bmi/logger.pcm"]
