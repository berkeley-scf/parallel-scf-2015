## @knitr doMPI

## you should have invoked R as:
## mpirun -machinefile .hosts -np 1 R CMD BATCH --no-save doMPI.R doMPI.Rout
## or for interactive use:
## mpirun -machinefile .hosts -np 1 R --no-save

library(Rmpi)
library(doMPI)

cl <- startMPIcluster()  # by default will start one fewer slave
# than elements in .hosts
                                        
registerDoMPI(cl)
clusterSize(cl) # just to check

results <- foreach(i = 1:200) %dopar% {
  out <- mean(rnorm(1e6))
}

print(results[1:5])

closeCluster(cl)

mpi.quit()
