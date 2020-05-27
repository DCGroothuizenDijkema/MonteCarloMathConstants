
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//
#                                                                                                                                       //
# main.py                                                                                                                               //
#                                                                                                                                       //
# D. C. Groothuizen Dijkema - January, 2020                                                                                             //
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//

# Main file to produce approximations of mathematical constants using Monte Carlo methods


from numpy import e,pi

from mc import approximate_e,approximate_pi,run_and_plot

def visualise_e(num_itr=1000000,num_runs=200,batch_size=10,show_fig=False,save_fig=True,file_name='e.pdf',dpi=1200,verbose=True):
  '''
  Produce a visualisation of the Monte Carlo approximation of Euler's Number.

  Parameters
  ----------
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

  '''
  run_and_plot(approximate_e,(2,3.8),'Euler\'s Number','e',e,num_itr=num_itr,num_runs=num_runs,batch_size=batch_size,show_fig=show_fig
    ,save_fig=save_fig,file_name=file_name,dpi=dpi)

def visualise_pi(method='area',num_itr=1000000,num_runs=200,batch_size=10,show_fig=False,save_fig=True,file_name='pi.pdf',dpi=1200,verbose=True):
  '''
  Produce a visualisation of the Monte Carlo approximation of pi using one of two methods.

  Parameters
  ----------
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

  '''
  # check method is valid
  methods=['area','chord']
  if method not in methods:
    raise ValueError('`method` must be one of {}, but is {}'.format(methods,method))
  # parameter values based on methods
  if method=='area':
    y_lim=(1.8,4.2)
  else:
    y_lim=(0,4.2)

  run_and_plot(approximate_pi,y_lim,r'$\pi$','pi',pi,args=(method,),num_itr=num_itr,num_runs=num_runs,batch_size=batch_size,show_fig=show_fig
    ,save_fig=save_fig,file_name=file_name,dpi=dpi)

if __name__=='__main__':
  # visualise_e()
  # visualise_pi('area')
  # visualise_pi('chord')
  pass