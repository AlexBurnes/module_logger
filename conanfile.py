from conan import ConanFile
from conan.tools.build import check_max_cppstd, check_min_cppstd
from conan.tools.cmake import CMakeToolchain, CMake, CMakeDeps, cmake_layout
from conan.tools.files import copy

class module_loggerConanRecipe(ConanFile):
    name = "module-logger"
    version = "0.1.0"

    license = "Svyazcom LCC"
    author = "Aleksey.Ozhigov <burnes@svyazcom.ru>"
    url = "git@gitsrv.svyazcom.ru:common/cpplibs/log.git"
    description = "C++20 module logger library"
    topics = ("Common", "logger")

    settings = "os", "compiler", "build_type", "arch"

    exports_sources = "CMakeLists.txt", "include/*"
    no_copy_source = True

    options = {"flush": [True, False]}
    default_options = {"flush": False}

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

    def package(self):
        copy(self, "*.mpp", self.source_folder, self.package_folder)

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
