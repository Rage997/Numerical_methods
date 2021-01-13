clear
close all
clc

% ----------------------------------------------------------------
% This part of code has been used just for testing
n = 11; 
% % 
A = assemble_matrix(n);
% b = assemble_vector(n);
% x0 = zeros(n, 1);
% [u, k] = gauss_solver(A, b, x0, eps, 1000);
% sol = u(:, end);
% ----------------------------------------------------------------


n_iter = 50000;
n = 9999; %size problem
curr = zeros(n, 1);
prev = zeros(n, 1);
for j=1:n_iter
    for i=2:n-1
        a_ii = 6; %main diagonal is always 6
        sum_d = -4; %the sum of the element on the adjacent diagonals
        b_i = 3;
        if i == round(n/2) %middle element
           b_i = 2;
           id_b = 0;
        % handle the antidiagonal
        elseif i > round(n/2) 
           id_b = curr(n+1-i);
        else 
           id_b = prev(n+1-i);
        end    
    %Each multiplication and subtraction is O(n), therefore the total
    % complexity at each loop iteration is O(n). The total is therefore
    % O(n^2)
    curr(i) = 1/a_ii * (b_i + 2*curr(i+1) +2*prev(i-1) ...
              -id_b);
    end
    sum_d = -2;
    b_i = 5;
    curr(1) = 1/a_ii * (b_i + 2*curr(2) -curr(n));
    curr(end) = 1/a_ii * (b_i + 2*curr(n-1) -prev(1));
    if norm(curr - prev, 'inf') < eps
        break
    end
    prev = curr;

end

fprintf('It took %d iterations to get the solution of size %d at machine error. \n ', j, n)
