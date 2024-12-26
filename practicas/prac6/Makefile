BUILD_DIR = build
CMAKE = cmake
CTEST = ctest

all: build-catch build-boost

# Compilar y ejecutar pruebas con Catch2
build-catch:
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) && $(CMAKE) ..
	$(CMAKE) --build $(BUILD_DIR)
	cd $(BUILD_DIR) && $(CTEST) -R Catch2Tests --output-on-failure

# Compilar y ejecutar pruebas con Boost.Test
build-boost:
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) && $(CMAKE) ..
	$(CMAKE) --build $(BUILD_DIR)
	cd $(BUILD_DIR) && $(CTEST) -R BoostTests --output-on-failure

clean:
	rm -rf $(BUILD_DIR)
