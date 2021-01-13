function [v] = compute_eig(a, b, c, k, n)
% Computes the k-th eigenvalue of a tridiagonal matrix of size n
% with constant entries a, b, c (i.e. Toeplitz matrix)
% ref: https://en.wikipedia.org/wiki/Tridiagonal_matrix
% section: eigenvalue

v = a - 2*sqrt(b*c)*cos( (k*pi)/(n+1) );

end