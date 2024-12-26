#include "calculadora.h"
#include <stdexcept>

float suma(float a, float b) {
    return a + b;
}

float resta(float a, float b) {
    return a - b;
}

float multiplicacion(float a, float b) {
    return a * b;
}

float division(float a, float b) {
    if (b == 0.0f) {
        throw std::invalid_argument("Division por cero");
    }
    return a / b;
}
