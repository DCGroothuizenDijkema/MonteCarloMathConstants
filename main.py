
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//
#                                                                                                                                       //
# main.py                                                                                                                               //
#                                                                                                                                       //
# D. C. Groothuizen Dijkema - January, 2020                                                                                             //
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//

# Main file to produce approximations of mathematical constants using Monte Carlo methods


import errno
import os

import matplotlib.pyplot as plt
import numpy as np

from huygens.plotting import simulation_plot,setup_simulation_plot
from mc import *

output_dir='./out/' # change if you want the plots somewhere else
try:
  os.makedirs(output_dir) 
except OSError as err:
  if err.errno != errno.EEXIST:
    raise


if __name__=='__main__':
  pass