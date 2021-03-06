
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//
#                                                                                                                                       //
# mc.py                                                                                                                                 //
#                                                                                                                                       //
# D. C. Groothuizen Dijkema - January, 2020                                                                                             //
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//

# Helper function file for producing approximations of mathematical constants using Monte Carlo methods


import ctypes as ct
import numpy as np

import matplotlib.pyplot as plt

import os
# you may very well need to change this (I don't really know why it's here, anyway)
# point it to the directory where any of the dlls your fortran dll depends on
os.add_dll_directory('C:/bin/mingw-w64/mingw64/bin')

from huygens.interf import c_pointer,c_vector
from huygens.plotting import simulation_plot,setup_simulation_plot

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

def run_and_plot(func,y_lim,plot_name,print_name=None,actual_value=None,args=(),num_itr=1000000,num_runs=200,batch_size=10,show_fig=False
  ,save_fig=True,file_name='plot.pdf',dpi=1200,verbose=True):
  '''
  Produce a plot of the Mandelbrot Set or a Julia Set, coloured by the number of iterations taken.
  
  Parameters
  ----------
  func : callable
    - The function to approximate the constant.
      Should be of the found `func(n,*args).
  y_lim : (float,float)
    - The limits of the y-axis of the simulation plot.
  plot_name : string
    - The name of the constant to plot with.
  print_name : string, optional
    - The name of the constant to output with. Only needed if `verbose` is `True`.
  actual_value : float, optional
    - The actual value of the constant being approximated.
  args : tuple, optional
    - Arguments to pass onto `func`.
  num_itr : int, optional
    - The number of iterations in each simulation.
  num_runs : int, optional
    - The number of simulations to run.
  batch_size : int, optional
    - The size of each simulation batch, to limit memory usage.
      `batch_size` must divide `num_runs`.
  show_fig : bool, optional
    - If the visualisation should be shown.
  save_fig : bool, optional
    - If the visualisation should be saved.
  file_name : string, optional
    - The name of the output.
  dpi : int, optional
    - Plot resolution.
  verbose : bool, optional.
    - For verbose output.

  Returns
  -------
  fig : matplotlib.figure.Figure
    The plot's Figure
  ax : matplotlib.axes.Axis
    The Axis of `fig`

  '''
  # check valid parameters
  assert num_runs%batch_size==0, "`num_runs` is not a multiple of `run_size`"

  # get figure and axis to plot on
  fig,ax=setup_simulation_plot(x_lim=(10,num_itr),y_lim=y_lim,title=r'Approximating {} with Monte Carlo simulations'.format(plot_name)
    ,x_label='Iteration',y_label=r'Estimate of {}'.format(plot_name))

  # perform the simulation
  mean=[]
  data=np.empty((batch_size,num_itr))
  for run in range(int(num_runs/batch_size)):
    for sim in range(batch_size):
      if verbose:
        print('Run: {}; Sim: {}'.format(run,sim))
      data[sim,:]=func(num_itr,*args)
    # keep track of the means
    mean.append(np.mean(data[:,-1]))
    # plot the data
    ax=simulation_plot(data[:,10:],np.arange(10,num_itr),ax=ax)

  # plot the actual value, if known
  if actual_value is not None:
    ax=simulation_plot(data,np.arange(num_itr),ax=ax,hline=actual_value,hline_linewidth=1.5,hline_alpha=0.9)
  # output
  if verbose:
    print(r'{} is approximately {:.4f}'.format(print_name,np.mean(mean)))
  if save_fig:
    plt.savefig('{}'.format(file_name),dpi=dpi,bbox_inches='tight',pad_inches=0.25)
  if show_fig:
    plt.show()

  return fig,ax

def approximate_e(num_itr,*args):
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

def approximate_pi(num_itr,*args):
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
  method,=args
  methods=['area','chord']
  if method not in methods:
    raise ValueError('`method` must be one of {}, but is {}'.format(methods,method))

  # setup array to write rolling average to
  means=c_vector(ct.c_double,num_itr)
  # call library function
  if method=='area':
    _approximate_pi(c_pointer(ct.c_int,num_itr),means)
  else:
    _approximate_chord_length(c_pointer(ct.c_int,num_itr),means)
  
  # return as np array
  return np.ctypeslib.as_array(means)
