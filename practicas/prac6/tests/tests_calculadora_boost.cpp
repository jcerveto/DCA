#define BOOST_TEST_MODULE CalculadoraTest
#include <boost/test/unit_test.hpp>
#include "calculadora.h"

BOOST_AUTO_TEST_SUITE(calculadora_ts)

BOOST_AUTO_TEST_CASE(suma_test) {
    BOOST_CHECK_EQUAL(suma(2.0f, 3.0f), 5.0f);
    BOOST_CHECK_EQUAL(suma(-1.0f, 1.0f), 0.0f);
}

BOOST_AUTO_TEST_CASE(resta_test) {
    BOOST_CHECK_EQUAL(resta(5.0f, 3.0f), 2.0f);
    BOOST_CHECK_EQUAL(resta(0.0f, 1.0f), -1.0f);
}

BOOST_AUTO_TEST_CASE(multiplicacion_test) {
    BOOST_CHECK_EQUAL(multiplicacion(2.0f, 3.0f), 6.0f);
    BOOST_CHECK_EQUAL(multiplicacion(-2.0f, 3.0f), -6.0f);
}

BOOST_AUTO_TEST_CASE(division_test) {
    BOOST_CHECK_EQUAL(division(6.0f, 3.0f), 2.0f);
    BOOST_CHECK_THROW(division(1.0f, 0.0f), std::invalid_argument);
}

BOOST_AUTO_TEST_SUITE_END()
