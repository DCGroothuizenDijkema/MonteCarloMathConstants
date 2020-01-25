
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

def run(constant,display_name,actual_value,save_name=None):
  if constant=='e':
    func=approximate_e
    y_lim=(2,3.8)
  elif constant=='pi':
    func=approximate_pi
    y_lim=(1.8,4.2)
  else:
    raise ValueError('Functions only exist to approximate e and pi.')

  # constants
  num_itr=1000000
  num_runs=200
  run_size=10

  assert num_runs%run_size==0, "`num_runs` is not a multiple of `run_size`"

  # output
  if save_name is None:
    save_name=constant
  plot_name='{}.png'.format(save_name)
  image_res=1200

  # control
  save_fig=True
  show_fig=False
  verbose=True

  # get figure and axis to plot on
  _,ax=setup_simulation_plot(x_lim=(10,num_itr),y_lim=y_lim,title=r'Approximating {} with Monte Carlo simulations'.format(display_name)
    ,x_label='Iteration',y_label=r'Estimate of {}'.format(display_name))

  # perform the simulation
  mean=[]
  last_run=int(num_runs/run_size)-1
  data=np.empty((run_size,num_itr))
  for run in range(int(num_runs/run_size)):
    for sim in range(run_size):
      if verbose:
        print('Run: {}; Sim: {}'.format(run,sim))
      data[sim,:]=func(num_itr)
    # keep track of the means
    mean.append(np.mean(data[:,-1]))
    # if it's the last run, plot the actual value along with the data
    # otherwise, just plot the data
    if run==last_run:
      ax=simulation_plot(data,np.arange(num_itr),ax=ax,hline=actual_value,hline_linewidth=1.5,hline_alpha=0.9)
    else:
      ax=simulation_plot(data[:,10:],np.arange(10,num_itr),ax=ax)

  # output
  if verbose:
    print(r'{} approximately {:.4f}'.format(constant,np.mean(mean)))
  if save_fig:
    plt.savefig('{}{}'.format(output_dir,plot_name),dpi=image_res,bbox_inches='tight',pad_inches=0.25)
  if show_fig:
    plt.show()

if __name__=='__main__':
  run('e','Euler\'s Number',np.e)
  # run('pi',r'$\pi$',np.pi,'pi1')