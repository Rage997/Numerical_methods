close all
clc
clear

% Solution for exercise 2 assignment 3

%Load data points and flip column and rows
delimiterIn = ' ';
Q = transpose(importdata('data/Q.pts',delimiterIn));
P = transpose(importdata('data/P.pts',delimiterIn));

assert(all(size(Q) == size(P)));
m = size(Q, 2); % number of points
n = 2; % dimension

% compute barycentric
bar_Q = mean(Q, 2);
bar_P = mean(P, 2);

% remap points such taht sum(shifted_Q) = sum(shifted_P) = 0
nabla_Q = Q - bar_Q;
nabla_P = P - bar_P;

% Cofactor matrix computation
A = zeros(n, n);
for i =1:m
    A = A + (nabla_Q(:, i) * nabla_P(:, i)');
end

%The rank of A **should** be the dimension of the vector space (my
% intuition)
% assert(rank(A) == n)

% Singular value decomposition
[U,S,V] = svd(A);
R = V*U'; %rotation R
% a rotation should satisfy R*R' = I

t = bar_P - R*bar_Q; %optimal translation

new_points = R*Q + t; %fitted points

% Plot points
figure
plot(P(1,:), P(2,:), 'r .', 'MarkerSize', 10);
hold on
plot(Q(1,:), Q(2,:), 'b .', 'MarkerSize', 10);
hold on
plot(new_points(1,:), new_points(2,:), 'g *', 'MarkerSize', 10);
legend('P', 'Q', 'newPoints')



% Compute f(R, t)
f = 0;
for i=1:n+1
    f = norm(P(:, i) - R*Q(:, i) - t)^2 + f;
end

% Logs
fprintf('The rotation matrix: \n')
R
fprintf('The translation vector: \n')
t
fprintf('f(R, t) = %d \n \n', f)
fprintf('The transformed points: \n')
new_points
fprintf('The norm L_inf(P_new - P) is %d \n',  norm(new_points - P, 'inf'))