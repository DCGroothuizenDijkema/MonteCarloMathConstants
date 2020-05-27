
# MonteCarloMathConstants

Approximating mathematical constants with Monte Carlo simulations

## Purpose

This repository contains a library written in Fortran for the approximation of mathematical constants. It was originally made to learn Fortran and interfacing compiled code with Python, and to explore Monte Carlo methods.

This library only contains approximations of [e](https://en.wikipedia.org/wiki/E_(mathematical_constant)) and [pi](https://en.wikipedia.org/wiki/Pi), including visualisations of the simulations used in the approximation. However, a similar project was undertaken [here](https://github.com/DCGroothuizenDijkema/LeapingFrog).

## Output

The following two visualisations are examples of that made by the programme:

![Euler's Number Simulation Results](https://drive.google.com/uc?id=1N20DfVPElOQIxIYCUn8ut7N8cMmGpH4Y)

![Pi Simulation Results 1](https://drive.google.com/uc?id=1TkcqlCxMwO3if65pE84W0tkwlpqd81IF)

The following plot shows an estimation of pi with a different method, and shows a general under estimation of the constant, unless a sufficient number of iterations are used.

![Pi Simulation Results 2](https://drive.google.com/uc?id=1TWZuLV6w2gehAXWA4k4xdBd80sDBFbgE)

Each of the blue lines on the above plot is the moving average of each approximation function in one simulation. Each simulation repeats the experiment 1,000,000 times, and there are 200 simulations. As can be seen, each simulation approaches the true value, given by the solid red line.

## Building

The library was developed with with [MinGW-w64](http://mingw-w64.org/doku.php), [specifically this version](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1.0/threads-posix/seh), and can be built with the provided Makefile and nmake, with the following command:

```shell
nmake all
```

Note the following build command requires ```./bin/``` and ```./obj/``` directories to be created before executing the commands.

Further, the programme can be built using gfortran on the command line with the following command:

```shell
gfortran -c -ffree-form -J./obj/ -o ./obj/mc.o ./src/mc.f
gfortran -shared -o ./bin/mc.dll ./obj/mc.o
```

When using the Python backend, any DLLs which the produced DLL depends on will need to be added to the DLL directory. This can be done with the command ```os.add_dll_directory()```. This is currently done at the top of ```mc.py``` with the directories needed by my own system, and will likely need changing to run.

## Dependencies

This project uses my huygens Python library, which can he found at <https://github.com/DCGroothuizenDijkema/huygens/>.
