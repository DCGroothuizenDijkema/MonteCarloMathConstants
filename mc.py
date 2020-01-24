
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//
#                                                                                                                                       //
# mc.py                                                                                                                                 //
#                                                                                                                                       //
# D. C. Groothuizen Dijkema - January, 2020                                                                                             //
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//

# Helper function file for producing approximations of mathematical constants using Monte Carlo methods

import ctypes as ct
import numpy as np

from huygens.interf import c_pointer,c_vector

# load the lib
_libc=ct.cdll.LoadLibrary('./bin/mc.dll')

# extract the functions
_approximate_e=getattr(_libc,'__monte_carlo_MOD_approximate_e')
_approximate_pi=getattr(_libc,'__monte_carlo_MOD_approximate_pi')

# assign arg and return types
_approximate_e.argtypes=[ct.POINTER(ct.c_int),ct.POINTER(ct.c_double)]
_approximate_pi.argtypes=[ct.POINTER(ct.c_int),ct.POINTER(ct.c_double)]
_approximate_e.restype=None
_approximate_pi.restype=None
