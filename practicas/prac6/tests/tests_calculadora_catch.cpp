#define CATCH_CONFIG_MAIN
#include "catch/catch.hpp"      // Importamos de manera relativa, no desde #include <catch2/catch.hpp>
#include "calculadora.h"

TEST_CASE("Operaciones básicas de la calculadora", "[calculadora]") {
    SECTION("Prueba de suma") {
        REQUIRE(suma(2.0f, 3.0f) == 5.0f);
        REQUIRE(suma(-1.0f, 1.0f) == 0.0f);
    }

    SECTION("Prueba de resta") {
        REQUIRE(resta(5.0f, 3.0f) == 2.0f);
        REQUIRE(resta(0.0f, 1.0f) == -1.0f);
    }

    SECTION("Prueba de multiplicación") {
        REQUIRE(multiplicacion(2.0f, 3.0f) == 6.0f);
        REQUIRE(multiplicacion(-2.0f, 3.0f) == -6.0f);
    }

    SECTION("Prueba de división") {
        REQUIRE(division(6.0f, 3.0f) == 2.0f);
        REQUIRE(division(-6.0f, 2.0f) == -3.0f);

        REQUIRE_THROWS_AS(division(1.0f, 0.0f), std::invalid_argument);
    }
}
