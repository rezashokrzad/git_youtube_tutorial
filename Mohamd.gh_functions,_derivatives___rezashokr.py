# -*- coding: utf-8 -*-
"""Copy of AI–DS Nexus | A0.3. Functions, Derivatives | RezaShokr.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_qmAzLa9sDsCcLHl3YGUq2hhHhFOrHgC

## 1. Log and Exp: Proving Inverse Relationship
"""

import numpy as np

# Show log(exp(x)) == x and exp(log(x)) == x for several values
import numpy as np

# Show log(exp(x)) == x and exp(log(x)) == x for several values
x_vals = np.array([1, 2, 3, np.e])
print("x\tlog(exp(x))\texp(log(x))")
for x in x_vals:
    print(f"{x:.2f}\t{np.log(np.exp(x)):.2f}\t\t{np.exp(np.log(x)):.2f}")

# Edge case: try negative and zero values (show error/NaN for log)
y_vals = np.array([0, -1, 5])
print("\nlog(exp(y)) for 0 and negative values:")
print(np.log(np.exp(y_vals)))

"""### 👀🔎 What do you see?

#### **your answer:** --------

## 2. Plotting Sine Functions Variations
"""

import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 100)

# look at the description of each function and call the proper function from numpy
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.sin(2*x), label='sin(2x)')
plt.plot(x, np.sin(0.5*x), label='sin(x/2)')
plt.plot(x, np.sin(x)**2, label='sin²(x)')
plt.legend()
plt.title("Variations of Sine Functions")
plt.show()

"""### 👀🔎 What do you see?

#### **your answer:** --------

# 📚 Assignment 3 — Functions, Derivatives & Gradients
This assignment explores the mathematical foundation of machine learning: functions and their derivatives. You’ll visualize, analyze, and code up essential concepts every ML practitioner uses.


**👀🔎 What do you see?**

Look at the snippet codes and:

* Describe any patterns, surprises, or connections you notice.

* Write a few sentences about your observations! 📝✨

## 3. Subplots: Trig, Inverse, Exp, and Log
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1, 1, 400)
x2 = np.linspace(0.1, 2, 400)  # For log and exp

# based on the number of subplots what should be the dimensions in the following line?
fig, axs = plt.subplots(2, 4, figsize=(16, 8))
axs[0,0].plot(x, np.sin(x));      axs[0,0].set_title("sin(x)")
axs[0,1].plot(x, np.cos(x));      axs[0,1].set_title("cos(x)")
axs[0,2].plot(x, np.tan(x));      axs[0,2].set_title("tan(x)")
axs[0,3].plot(x, np.arcsin(x));   axs[0,3].set_title("arcsin(x)")
axs[1,0].plot(x, np.arccos(x));   axs[1,0].set_title("arccos(x)")
axs[1,1].plot(x, np.arctan(x));   axs[1,1].set_title("arctan(x)")
axs[1,2].plot(x2, np.exp(x2));    axs[1,2].set_title("exp(x)")
axs[1,3].plot(x2, np.log(x2));    axs[1,3].set_title("log(x)")

plt.tight_layout()
plt.show()

"""### 👀🔎 What do you see?

#### **your answer:** --------

## 4. Features of the Sigmoid Function
"""

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.linspace(-10, 10, 200)
y = sigmoid(x)

plt.plot(x, y)
plt.title("Sigmoid Function")
plt.xlabel("x")
plt.ylabel("σ(x)")
plt.grid(True)
plt.show()

print("Range:", (y.min(), y.max()), "| At x=0:", sigmoid(0))

"""### 👀🔎 What do you see?

#### **your answer:** --------

## 5. Derivatives of Famous Functions
"""

x = np.linspace(-3, 3, 400)
plt.plot(x, x**2, label="x²")
plt.plot(x, 2*x, '--', label="d/dx x²")

x = np.linspace(0, 3, 400)
plt.plot(x, np.exp(x), label="exp(x)")
plt.plot(x, np.exp(x), '--', label="d/dx exp(x)")

plt.plot(x, np.log(x+0.1), label="log(x)")
plt.plot(x, 1/(x + 0.1), '--', label="d/dx log(x)")

plt.legend()
plt.title("Functions and Their Derivatives")
plt.show()

"""### 👀🔎 What do you see?

#### **your answer:** --------

## 6. Gradient of Selected Functions
"""

# search and learn more about sumpy
import sympy as sp

# Define symbolic variables
x, y = sp.symbols('x y')

# Define the function
f = x**2 * y + sp.sin(y)

# Compute partial derivatives
df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)

print("Function: f(x, y) =", f)
print("Partial derivative w.r.t x (∂f/∂x):", df_dx)
print("Partial derivative w.r.t y (∂f/∂y):", df_dy)

"""### 👀🔎 What do you see?

#### **your answer:** --------
"""