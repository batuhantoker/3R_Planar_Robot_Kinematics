import sympy

# Define the symbols for the joint angles
theta1, theta2, theta3 = sympy.symbols("theta1 theta2 theta3")

# Define the symbols for the link lengths
l1, l2, l3 = sympy.symbols("l1 l2 l3")

# Define the symbols for the end-effector coordinates
x, y = sympy.symbols("x y")

# Define the forward kinematic equations
x_eq = l1 * sympy.cos(theta1) + l2 * sympy.cos(theta1 + theta2) + l3 * sympy.cos(theta1 + theta2 + theta3)
y_eq = l1 * sympy.sin(theta1) + l2 * sympy.sin(theta1 + theta2) + l3 * sympy.sin(theta1 + theta2 + theta3)

# Solve for the joint angles in terms of the end-effector coordinates
solutions = sympy.solve([x_eq - x, y_eq - y], [theta1, theta2, theta3])

# Print the inverse kinematic equations
print("Inverse kinematic equations:")
print("theta1 =", solutions[theta1])
print("theta2 =", solutions[theta2])
print("theta3 =", solutions[theta3])
