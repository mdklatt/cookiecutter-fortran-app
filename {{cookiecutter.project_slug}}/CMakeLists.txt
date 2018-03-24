## CMake build file for the {{ cookiecutter.app_name }} application.
##
## Compiled binaries will be written to build/${CMAKE_BUILD_TYPE}.
##
cmake_minimum_required(VERSION 2.8.12)

project({{ cookiecutter.app_name }})

set(PROJECT_BINARY ${PROJECT_NAME})

# Set compiler flags (valid for gcc-gfortran).

enable_language(Fortran)
set(CMAKE_Fortran_FLAGS "-std=f2003 -fimplicit-none -Wall -pedantic")
set(CMAKE_Fortran_FLAGS_DEBUG "-fcheck=bounds")

add_executable(${PROJECT_BINARY} src/main.f90)
