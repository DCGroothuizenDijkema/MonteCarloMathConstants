
# Windows nmake makefile

F=gfortran

SRC=./src/mc.f
OBJ=./obj/mc.o

TARGET=./bin/mc.dll

all: dir $(TARGET)
reset: clean all

dir: 
	-@ if NOT EXIST "./bin/" mkdir "./bin/"
	-@ if NOT EXIST "./obj/" mkdir "./obj"

clean:
	-@ if EXIST "./bin/" del /F /Q /S "./bin/" > NUL
	-@ if EXIST "./bin/" rmdir /Q /S "./bin/"
	-@ if EXIST "./obj/" del /F /Q /S "./obj/" > NUL
	-@ if EXIST "./obj/" rmdir /Q /S "./obj/"


$(TARGET):	$(OBJ)
	$(F) -shared -o $(TARGET) $(OBJ)

obj/mc.o: ./src/mc.f
	$(F) -c -ffree-form -J./obj/ -o ./obj/mc.o ./src/mc.f