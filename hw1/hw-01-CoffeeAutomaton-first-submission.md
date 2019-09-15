---
id: homework

title: "Homework #1"
author: "Coffee Automaton"
affiliation: ACM Class, Zhiyuan College, SJTU
course: CS 217 @ SJTU
prof: Dominik Scheder
TA: "Tang Shuyang"
dueDate: September 23, 2019

geometry: margin = 1in
mainfont: TeX Gyre Pagella
mainfontoptions:
- Numbers = Proportional
monofont: "Ubuntu Mono"

output:
    custom_document:
        latex_engine: xelatex
        template: ../templates/homework.latex
        highlight: tango
        path: "hw-01-CoffeeAutomaton-first-submission.pdf"
---

@import "homework.less"

# Exercise 1

The integer division algorithm in school method is implemented in *[App.1](#appendix-1-euclidean-algorithm)*.

The core code for integer division is as follows.

@import "1.ex.1.py"

The outer loop runs $n-k$ times, and the inner loop runs $k$ times. Inside the loop body are bit operations. So the total algorithm runs in $O(k(n−k))$ operations.

# Exercise 2

@import "1.ex.2.py"

It is obvious that $r\le\lfloor\frac{a}{2}\rfloor$ and $s\le\lfloor\frac{b}{2}\rfloor$, so every cycle $a$ and $b$ become at most half of the previous value they have.

Suppose $a\ge b$, and let $n$ and $m$ denote the number of bits of $a$ and $b$, we have $n\ge m$.

Since the integer division makes $O(m(n-m))$ bit operations.

The $\gcd(a,b)$ makes

$$O(m(n-m)+\frac{1}{2^2}m(n-m)+\frac{1}{2^4}m(n-m)+\cdots)=O(m(n-m))=O(n^2)$$

operations.

# Exercise 3

@import "1.ex.3.py"

```markdown
10
```

The algorithm recurses $O(nC_n^k)$ times, and the time complexity of bitwise addition is $O({\log_2 2^n})=O(n)$.

So the running time of the algorithm is $O(n^2C_n^k)$.

It is not an efficient algorithm, because the time complexity of the algorithm is exponential.

# Exercise 4

The dynamic programming algorithm is implemented as follows.

@import "1.ex.4.py"

```markdown
10
```

The outer loop runs $n$ times, and the inner loop runs $k$ times. And the time complexity of bitwise addition is $O({\log_2 2^n})=O(n)$. So the running time of the program is $O(n^2k)$.

It is an efficient algorithm, because the time complexity of the algorithm is polynomial.

# Exercise 5

The dynamic programming algorithm is implemented as follows.

@import "1.ex.5.py"

```markdown
10
```

The outer loop runs $n$ times, and the inner loop runs $k$ times. And the time complexity of bitwise addition modulo 2 is $O(1)$. So the running time of the program is $O(nk)$.

It is an efficient algorithm, because the time complexity of the algorithm is polynomial.

# Exercise 6

A lasso cannot happen.

If we had some $1\le i<j$ such that $F'_i=F'_j$ and $F'_{i+1}=F'_{j+1}$, we would have $F'_{i-1}\equiv F'_{i+1}-F'_i\equiv F'_{j+1}-F'_j\equiv F'_{j-1}\pmod k$ and $F'_i=F'_j$, so $i-1$ also satisfies the condition.
Therefore, the smallest $i$ must be $0$, and form a circle.

Here's the code for finding a fibonacci period:

@import "1.ex.6.py"

```markdown
period = 8
```

\pagebreak

# Appendix

## Appendix 1. Euclidean algorithm

@import "1.app.1.py"

```markdown
4
```