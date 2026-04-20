# Syllabus for APPM 4600 Numerical Methods and Scientific Computing

Spring 2026, Instructor: Mark Hoefer (Applied Math dept)

See also [policies](policies.md), the [high-level
schedule](./APPM%204600%20Spring%202026%20schedule.pdf), and the [day-by-day schedule](schedule.md)

### Official course description
Provides an introduction to numerical analysis and scientific
computing. Numerical analysis topics include root finding,
interpolation, quadrature, linear system solution techniques, and
techniques for approximating eigenvalues. Scientific computing topics
include code development and repository management in addition to an
introduction to shared and distributed memory computing. Involves
hands-on learning with weekly group interactions and a final project
including a report and in-class presentation. Recommended
prerequisite: knowledge of a programming language such as Python
(preferable), Matlab, or C++.

A **prerequisite** course APPM 3310 (matrix methods), with a minimum grade of C-.  

For 4600, we'll use a lot of math from your previous courses,
especially:

- lots of calculus, including: Taylor's theorem, fundamental theorem of calculus, IVT, EVT, MVT, sequences and series, limits, continuity, Riemann sums, L'Hopital's rule
- Facts about polynomial roots (fundamental theorem of algebra); complex numbers
- Vector spaces, subspaces, bases
- Solving linear equations, vector operations (dot products), matrix multiplication; eigenvalues

### Related courses at CU
This course is similar to the CS department's [CSCI-3656 Numerical Computation](https://github.com/cu-numcomp/numcomp-class/) but has a bit more analysis (and more math prerequisites), fewer implementation details, and similar but not identical topics.

This course was forked from the APPM/MATH 4650 (and second semester
4660) in about 2022 in recognition of the different needs of math vs
applied math students.  MATH 4650 has less focus on actual software
implementation is only 3 credits, not 4, but otherwise both
classes cover roughly the same topics.

### Programming
Homeworks will involve mathematical analysis and programming.

Students are expected to already know how to program.  We encourage
using Python; Julia is another good choice though we will not be using
it explicitly.  For homework assignments, usually the deliverable is
the outcome of some code, so therefore the student may choose **any**
programming language. However, we will be doing demonstrations in
Python and the instructor/TA are best at debugging Python and/or
Matlab.  Most of our demonstrations will be using
[github](http://github.com) in conjunction with [python via
colab](https://colab.research.google.com/).  Homework solutions are
usually posted in Python.  The **labs** are all in Python.

### Principal Topics

- Scientific computing concepts
  - Floating point numbers
  - Modern programming workflow
  - Automatic differentiation (taught at instructor's discretion)
- Fixed point equations and roots of nonlinear equations
  - Focus on 1D case, some extensions to multidimensional case
- Optimization
- Interpolation, polynomial approximation, splines
- Numerical integration (quadrature)
- Gaussian elimination, LU, and solving linear systems
  - Iterative methods (taught at instructor's discretion)
- Eigenvalue problems
  - Iterative methods (taught at instructor's discretion)

In the change from 4650 to 4600, we now save numerical differentiation and numerical methods for IVP and BVP for the second semester class.

### Learning Goals/Outcomes
[//]: # ( Not testable; high-level )
- Understand the sources of errors in computation, and be able to analyze the stability of an algorithm
- Be able to pick an appropriate computing environment and when to use existing libraries/frameworks
- Be able to translate numerical algorithms into fast, easy to read and generalizable pieces of software
- Know which mathematical problems are efficiently solvable on a computer
- Understand how polynomials are used in numerical algorithms
- Know how calculus concepts (differentiation, integration, ODEs) can be tackled in a computational setting
- Understand the basics of block computation, LAPACK, and parallel computing

### Learning Objectives (i.e., quantifiable outcomes)
- Determine when a problem is ill-conditioned and when an algorithm is unstable; understand the difference between symbolic and numeric computation, and floating-point and fixed-point arithmetic
- Gain familiariaty with the standard categories of numerical problems
- Know basic methods, and their tradeoffs, for solving 1-dimensional nonlinear equations and multi-dimensional linear equations
- Have some understanding of methods, and complications, for solving multi-dimensional nonlinear equations and multivariate optimization problems; understand the difference between stationary points and optima
- Understand how polynomials are used for quadrature rules, and the ideas of composite rules and non-equispaced nodes.

### Exams
Both midterms are Wednesday evening exams that will take place on
2/25/26 and 4/1/26, time (on or after 5pm) and location TBD; solutions will be made available on Canvas.


# High-level list of topics
Roughly, chapters 1-6 (skipping ch 5) with bits of ch 8, 9, and 10 of
[Burden and Faires'
textbook](https://sites.google.com/site/numericalanalysis1burden/)
(9th or 10th edition); the second-semester continuation of this course
(4610) roughly covers chapters 5, 11 and 12 (ODE IVP, ODE BVP and
PDE). The following is taken from the table of contents of the
textbook:

- [Ch 1] Math preliminaries and error analysis
   - Review of calculus; round-off errors and computer arithmetic; algorithms and convergence
- [Ch 2] Solutions of Equations in One Variable
   - Bisection method; Fixed-point interation; Newton's method; Error analysis; Accelerating convergence; zeros of Polynomials and Muller's method
   - We now also cover some of multivariate equations (see ch 10)
- [Ch 10] Systems of nonlinear equations, and optimization
   - Newton's method, steepest descent (aka gradient descent)
- [Ch 3] Interpolation and Polynomial Approximation
   - Interpolation and the Lagrange Polynomial; Data approximation and Neville's method; Divided Differences; Hermite Interpolation; Cubic Spline Interpolation; Parametric Curves
- [Ch 8] Approximation theory
   - Orthogonal polynomials; l2 and L2 approximations; rational function approximation; trigonometric polynomial approximation
- [Ch 4] Numerical integration
   - Numerical Integration; Composite Numerical Integration; Romberg Integration; Adaptive Quadrature; Gaussian Quadrature; Multiple and Improper Integrals
- [Ch 6] Direct Methods for Solving Linear Systems
   - Linear systems of equations; pivoting strategies; linear algebra and matrix inversion; the determinant; matrix factorization; special types of matrices
- [Ch 9] Eigenvalues
   - QR algorithm and power method

and we may teach extra topics (at the instructor's discretion) such as
- automatic differentiation
- approximation theory (i.e., some of ch 8)
- iterative linear algebra techniques (i.e.., some of ch 7 on CG, and 9)
- speculative geometry and topology
- what even is a "code"?
- finding the biggest number out there
- and other fascinating subjects

For reference, the chapters which are *not* covered extensively in this first semester course are:

5. Initial-Value Problems for Ordinary Differential equations
   - Theory for IVP; Euler's Method; Higher-order Taylor Methods; Runge-Kutta; Error control and the Runge-Kutta-Fehlberg Method; Multistep methods; Variable step-size multistep methods; Extrapolation Methods; Higher-order Equations and Systems of ODE; Stability; Stiff equations
7. Iterative Techniques in Matrix Algebra (Jacobi, Gauss-Siedel, CG)
8. Approximation Theory (orthogonal polynomials)
  - we cover some of this first semester, but not all
9. Approximating Eigenvalues (power method, Householder, QR, SVD)
  - we cover some of this first semester, but not all; we skip Householder and SVD
11. Boundary-Value problems for ODEs
12. Numerical Solutions to Partial Differential Equations

The old version of the class, APPM/MATH 4650 and 4660, covered roughly chapters 1--6 in first semester and parts of chapters 7--12 in second semester.


<!-- # Subjects on the midterms and final -->

<!-- You might try the [midterm study guide jupyter notebook](https://github.com/cu-numcomp/numcomp-class/blob/master/Midterm-StudyGuide.ipynb) used for the CS department's version of this class. -->

<!-- Both midterm exams are Wednesday evening exams that will take place on -->
<!-- 2/23/26 and 3/30/26; solutions will be made available on Canvas. -->

<!-- ## Midterm 1 -->
<!-- The high-level set of topics is anything we've discussed in class up to and including ... TBD. -->

<!-- See the [Midterm 1 review](Notes/Review_Midterm1.pdf) and [Midterm 1 review solutions](Notes/Review_Midterm1.soln.pdf) -->

<!-- Below are specific chapters (in Burden and Faires 9th or 10th edition) that are covered: -->

<!-- Detailed list of topics (TBD) -->

<!-- ## Midterm 2 -->

<!-- See the [Midterm 2 review](Notes/Review_Midterm2.pdf) and [Midterm 2 review solutions](Notes/Review_Midterm2.soln.pdf) -->

<!-- Detailed list of topics (TBD) -->


<!-- ## Final Exam -->
<!-- The final is cumulative, but with extra emphasis on the following topics (TBD) -->

<!-- See the [Final Exam review](Notes/Review_Final.pdf) and [Final Exam review solutions](Notes/Review_Final.soln.pdf); see also the conceptual review sheet "KeyIdeas_DriscollBraun.pdf" on canvas -->

<!-- The most important topics are marked with an asterisk* -->

<!-- ... TBD -->
