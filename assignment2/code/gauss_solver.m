function [x_iter, k] = gauss_solver(A, b, x0, tol, n_max)
% Solve a linear system of equation starting from an initial
% guess x0 a stops using a tolerance

k = 0;
x = x0;
x_iter(:,1) = x;
for i=1:n_max %For each iteration
    s = size(A, 1);
    for j=1:s %O(n)
        x(j) = (1/A(j,j)) * (b(j) - A(j,:)*x + A(j,j)*x(j));
    %Each multiplication and subtraction is O(n), therefore the total
    % complexity at each loop iteration is O(n). The total is therefore
    % O(n^2)
    end
    x_iter(:,i) = x(:);
    if norm(b - A *x(:)) < tol
        break
    end
    
    k = k+1;
end
end
