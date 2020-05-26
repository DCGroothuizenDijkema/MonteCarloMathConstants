
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//
#                                                                                                                                       //
# mc.py                                                                                                                                 //
#                                                                                                                                       //
# D. C. Groothuizen Dijkema - January, 2020                                                                                             //
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//

# Helper function file for producing approximations of mathematical constants using Monte Carlo methods


import ctypes as ct
import numpy as np

import os
# you may very well need to change this (I don't really know why it's here, anyway)
# point it to the directory where any of the dlls your fortran dll depends on
os.add_dll_directory('C:/bin/mingw-w64/mingw64/bin')

from huygens.interf import c_pointer,c_vector

__all__=['approximate_e','approximate_pi']

# load the lib
_libc=ct.cdll.LoadLibrary('./bin/mc.dll')

# extract the functions
_approximate_e=getattr(_libc,'__monte_carlo_MOD_approximate_e')
_approximate_pi=getattr(_libc,'__monte_carlo_MOD_approximate_pi_integration')
_approximate_chord_length=getattr(_libc,'__monte_carlo_MOD_approximate_pi_chord_length')

# assign arg and return types
_approximate_e.argtypes=[ct.POINTER(ct.c_int),ct.POINTER(ct.c_double)]
_approximate_pi.argtypes=[ct.POINTER(ct.c_int),ct.POINTER(ct.c_double)]
_approximate_chord_length.argtypes=[ct.POINTER(ct.c_int),ct.POINTER(ct.c_double)]
_approximate_e.restype=None
_approximate_pi.restype=None
_approximate_chord_length.restype=None

def approximate_e(num_itr):
  '''
  Produce an approximation of Euler's constant.

  This function uses the result that Euler's number is the expected value of the function which counts the number of random numbers
  which need to be generated in the interval [0,1] before their sum is strictly greater than one.

  Parameters
  ----------
  num_itr : int
    - The number of times the counting function should be called.

  Returns
  -------
  means : numpy.ndarray
    - The moving average approximation of Euler's constant.

  '''
  # setup array to write rolling average to
  means=c_vector(ct.c_double,num_itr)
  # call library function
  _approximate_e(c_pointer(ct.c_int,num_itr),means)
  # return as np array
  return np.ctypeslib.as_array(means)

def approximate_pi(num_itr,method='area'):
  '''
  Produce an approximation of pi.

  This function uses one of two approximations:

  1. `area`. It randomly picks two numbers in the interval [0,1] (in effect, randomly picking a point in 
  the unit square) and determines if the magnitude of those two numbers is less than one (in effect, if the random point is within the upper
  right-hand corner of the unit circle). pi can then be estimated by the number of points generated which are so within, based on the area
  of the circle and the area of the square, and that the circle has been chosen to have radius one, and therefore have area pi itself.
    Given that the area of the unit square is 1 and the area of the unit circle is pi, the ratio between the former and the upper right-hand
  corner of the latter is 4/pi. This ratio is approximated using the Monte Carlo simulation as the number of points which fall within the
  upper right-hand corner of the unit circle and all points generated. If the former is the `count` and the latter is the `total`, then
  pi=4*count/total

  2. `chord`. Given two random points on the radius of the circle, 4/pi is the average chord length between these points. Thefore, with 
  enough pairs of random points generated, pi can be calculaged as the average of 4/d, where d is the chord length between these pairs of
  points.

  Parameters
  ----------
  num_itr : int
    - The number of points to generate in the unit square.
  method : string
    - Which method to use to approximate pi. Must be one of 'area' or 'chord'.

  Returns
  -------
  means : numpy.ndarray
    - The moving average approximation of pi.

  '''
  # check method is valid
  methods=['area','chord']
  if method not in methods:
    raise ValueError('`method` must be one of {}'.format(methods))

  # setup array to write rolling average to
  means=c_vector(ct.c_double,num_itr)
  # call library function
  if method=='area':
    _approximate_pi(c_pointer(ct.c_int,num_itr),means)
  else:
    _approximate_chord_length(c_pointer(ct.c_int,num_itr),means)
  
  # return as np array
  return np.ctypeslib.as_array(means)
