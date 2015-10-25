n <- 8000
x <- matrix(rnorm(n^2), ncol = n)

for(i in 1:500) {
  U <- chol(crossprod(x))
}
