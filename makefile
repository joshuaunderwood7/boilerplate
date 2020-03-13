CC=g++
CPPFLAGS=-std=c++11 -Iinclude/
LDFLAGS=
LDLIBS=
BUILDFLAG=
MAKEFLAGS := --jobs=$(shell nproc)

SRC_DIR = src
OBJ_DIR = obj
BIN_DIR = bin
PRG_DIR = prgsrc
INC_DIR = include


C_SRC = $(wildcard $(SRC_DIR)/*.c)
C_OBJ = $(C_SRC:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)

CPP_SRC = $(wildcard $(SRC_DIR)/*.cpp)
CPP_OBJ = $(CPP_SRC:$(SRC_DIR)/%.cpp=$(OBJ_DIR)/%.o)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c 
	$(CC) $(CPPFLAGS) $(BUILDFLAG) -c $< -o $@

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(CC) $(CPPFLAGS) $(BUILDFLAG) -c $< -o $@

%: $(PRG_DIR)/%.cpp $(C_OBJ) $(CPP_OBJ)
	$(CC) $(CPPFLAGS) $(BUILDFLAG) $^ $(LDFLAGS) $(LDLIBS) -o $(BIN_DIR)/$@

.PHONEY: all clean
all: program

opt: BUILDFLAG += -O2 -s
opt: all

debug: BUILDFLAG += -ggdb
debug: all

profile: BUILDFLAG += -pg
profile: all

clean:
	-rm bin/*
	-touch bin/dummyfile
	-rm obj/*.o
	-touch obj/dummyfile
	-rm -r output/*
	-touch output/dummyfile

