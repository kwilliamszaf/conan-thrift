# -*- coding: utf-8 -*-
import os
from conans import ConanFile, tools


class ConanBase(ConanFile):
    version = "0.14.0"
    description = "Thrift is an associated code generation mechanism for RPC"
    url = "https://github.com/bincrafters/conan-thrift"
    homepage = "https://github.com/apache/thrift"
    author = "helmesjo <helmesjo@gmail.com>"
    topics = ("conan", "thrift", "serialization", "rpc")
    license = "Apache-2.0"
    exports = ["LICENSE.md", os.path.basename(__file__)]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def source(self):
        self.run("git clone git@github.com:kwilliamszaf/thrift.git")
        self.run("cd thrift")
        extracted_dir = "thrift"
        os.rename(extracted_dir, self._source_subfolder)

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()
