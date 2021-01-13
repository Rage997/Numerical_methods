function [b] = assemble_vector(n)

b = ones(n, 1);
b(1) = 5;
b(n) = 5;

for i=2:n-1
    b(i) = 3;
end
b(round(n/2)) = 2;

end