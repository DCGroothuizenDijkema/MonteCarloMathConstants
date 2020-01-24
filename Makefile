
# Windows nmake makefile

F=gfortran

SRC=./src/mc.f
OBJ=./obj/mc.o

TARGET=./bin/mc.dll

all: dir $(TARGET)

dir: 
	-@ if NOT EXIST "./bin/" mkdir "./bin/"
	-@ if NOT EXIST "./obj/" mkdir "./obj"

$(TARGET):	$(OBJ)
	$(F) -shared -o $(TARGET) $(OBJ)

obj/mc.o: ./src/mc.f
	$(F) -c -ffree-form -J./obj/ -o ./obj/mc.o ./src/mc.f