CC=gcc
CXX=g++
LIB_DIR=lib
SRC_DIR=src
MAIN_ENTRY=main.c
OBJ=sum.o
EXECUTABLE=main

all: $(EXECUTABLE)

$(EXECUTABLE): $(MAIN_ENTRY) $(OBJ)
	$(CC) $(MAIN_ENTRY) $(OBJ) -I $(LIB_DIR) -o $(EXECUTABLE)

$(OBJ): $(SRC_DIR)/sum.cpp $(LIB_DIR)/sum.h
	$(CXX) -c $(SRC_DIR)/sum.cpp -I $(LIB_DIR) -o $(OBJ)

clean:
	rm -f $(EXECUTABLE) $(OBJ)
