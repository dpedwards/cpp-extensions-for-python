from distutils.core import setup, Extension


sfc_module = Extension('FastCppExtension', sources=['Module.cpp'])

setup(name='FastCppExtension', version='1.0',
      description='Python Package with fast C++ extension',
      ext_modules=[sfc_module]
      )