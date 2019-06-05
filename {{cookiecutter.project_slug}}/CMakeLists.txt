## CMake build file for the {{ cookiecutter.app_name }} application.
##
cmake_minimum_required(VERSION 3.14)
project({{ cookiecutter.app_name }}
    VERSION {{ cookiecutter.project_version }}
    LANGUAGES Fortran
)

enable_language(Fortran)

set(EXECUTABLE {{ cookiecutter.app_name }})

add_executable(${EXECUTABLE})

target_sources(${EXECUTABLE}
PRIVATE
    src/main.f90
)

target_compile_options(${EXECUTABLE}
PRIVATE
    -Wall
    -std=f2003
    -fimplicit-none
    $<$<Fortran_COMPILER_ID:GNU>:-pedantic>
    $<$<CONFIG:Debug>:-fcheck=bounds>
)
