
# MonteCarloMathConstants

Approximating mathematical constants with Monte Carlo simulations

## Purpose

This repository contains a library written in Fortran for the approximation of mathematical constants. It was originally made to learn Fortran and interfacing compiled code with Python, and to explore Monte Carlo methods.

This library only contains approximations of [e](https://en.wikipedia.org/wiki/E_(mathematical_constant)) and [pi](https://en.wikipedia.org/wiki/Pi), including visualisations of the simulations used in the approximation. However, a similar project was undertaken [here](https://github.com/DCGroothuizenDijkema/LeapingFrog).

## Output

The following two visualisations are examples of that made by the programme:

![Euler's Number Simulation Results](https://drive.google.com/open?id=1N20DfVPElOQIxIYCUn8ut7N8cMmGpH4Y)

![Pi Simulation Results 1](https://drive.google.com/open?id=1TkcqlCxMwO3if65pE84W0tkwlpqd81IF)

![Pi Simulation Results 2](https://drive.google.com/open?id=1TWZuLV6w2gehAXWA4k4xdBd80sDBFbgE)

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

## Dependencies

This project uses my huygens Python library, which can he found at <https://github.com/DCGroothuizenDijkema/huygens/>.
