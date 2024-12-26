cmake_minimum_required(VERSION 3.0)
project(project)

# Configuración para subcarpetas
add_subdirectory(recursive)
add_subdirectory(non_recursive)

# Configuración para empaquetado con CPack
include(CPack)
set(CPACK_SOURCE_GENERATOR "TGZ")
add_custom_target(dist COMMAND ${CMAKE_COMMAND} --build . --target package_source)
