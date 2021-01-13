function [A] = assemble_matrix(n)

e = ones(n,1);
A = spdiags([-2*e 6*e -2*e], -1:1, n, n);
    
% Add antidiagonal element
idx = A==0; %do not add it where an element is already defined
antidiagonal = flip(eye(n));
% A(idx) = A(idx) + antidiagonal(idx);
end