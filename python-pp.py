## @knitr pp

import numpy
import pp

nCores = 4
job_server = pp.Server(ncpus = nCores, secret = 'mysecretphrase')
# set 'secret' to some passphrase (you need to set it but 
#   what it is should not be crucial)
job_server.get_ncpus()

nSmp = 10000000
m = 40
def taskFun(i, n):
    numpy.random.seed(i)
    return (i, numpy.mean(numpy.random.normal(0, 1, n)))

# create list of tuples to iterate over
inputs = [(i, nSmp) for i in xrange(m)]
# submit and run jobs using list comprehension
jobs = [job_server.submit(taskFun, invalue, modules = ('numpy',)) for invalue in inputs]
# collect results (will have to wait for longer tasks to finish)
results = [job() for job in jobs]
print(results)
job_server.destroy()
