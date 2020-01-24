
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

def run(constant):
  if constant=='e':
    func=approximate_e
  elif constant=='pi':
    func=approximate_pi
  else:
    raise ValueError('Functions only exist to approximate e and pi.')

  # constants
  num_itr=1000000
  num_runs=150
  run_size=10

  assert num_runs%run_size==0, "`num_runs` is not a multiple of `run_size`"

  # output
  plot_name='{}.png'.format(constant)
  image_res=1200

  # control
  save_fig=True
  show_fig=False
  verbose=True

if __name__=='__main__':
  run('e')
  # run('pi')