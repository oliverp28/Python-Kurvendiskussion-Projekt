# Python Curve Discussion Project

Welcome to the Python Curve Discussion Project! In this project, we conduct a comprehensive curve discussion with a focus on object-oriented programming.

## Overview

The project takes linear and quadratic functions as input. The input is validated through input validation and categorized into the respective function classes. The calculations are performed within each class.

## Results Include:

- Derivatives (Option to display all derivatives used in the calculation)
- Roots with the X-axis (Number; Coordinates)
- Symmetry (If present):
  - X-axis
  - Y-axis
- Extreme Points:
  - High points (Number; Coordinates if applicable)
  - Low points (Number; Coordinates if applicable)
  - Inflection points (Number; Coordinates if applicable)
- Curvature Behavior
- Monotonic Behavior
- Limit Behavior (Limits towards +/- infinity)

The output is presented in a well-organized and clear table.

## Project Participants

- Stefan Mack
- Oliver Polak
- Rami Karkaba
- David Klumpp

## Optimization before Submission

- Eliminate duplications and consolidate code
- Use pylint Python Code Analyzer
- Utilize black (code formatter)
- Implement pytest (code tester)
- Apply isort (Sort all Python modules correctly)

## Project Structure

### Classes

- InputFunction
- LinearFunction
- QuadraticFunction
- CurveDiscussionOutput

### Files

- main.py
- input_function.py
- linear_function.py
- quadratic_function.py
- curve_discussion_output.py

### Test Files

- test_lin_func.py
- test_quad_func.py

## Program Flow

`main` -> `input_function` -> `linear_function` | `quadratic_function` -> `curve_discussion_output`

Feel free to explore the functionalities and contribute to the optimization of the project!
