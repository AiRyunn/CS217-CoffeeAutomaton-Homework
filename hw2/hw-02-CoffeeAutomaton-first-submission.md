---
id: homework

title: "Homework #2"
author: Coffee Automaton
affiliation: ACM Class, Zhiyuan College, SJTU
course: CS 217 @ SJTU
prof: Dominik Scheder
TA: Tang Shuyang
dueDate: September 29, 2019

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
        path: "hw-02-CoffeeAutomaton-first-submission.tex"
---

@import "homework.less"

# Exercise 1

The algorithm is described as follows.

1. Make the array into $\frac{n}{2}$ pairs.

2. Sort each of the pair (makes $\frac{n}{2}$ comparisons).

3. For each of the pair, take the smaller one to the S group, and the larger one to the L group.

4. Find the smallest in the S group and the largest in the L group as the answer (each makes $\frac{n}{2}-1$ comparisons).
   
The algorithm totally makes $\frac{3}{2}n-2$ comparisons.

Here's the code implemented for the algorithm.

@import "2.1.py"

```markdown
array: [17, 5, 10, 2, 11, 13, 16, 7, 14, 18, 12, 3, 1, 6, 4, 15, 0, 9, 8, 19]
min and max: (0, 19)
3 n / 2 - 2 = 28
number of comparisons: 28
```

# Exercise 2

[solution](https://www.zhihu.com/question/33113457)

# Exercise 3

[solution](http://theory.stanford.edu/~tim/w11/l/qsort.pdf)

# Exercise 4

# Exercise 5

# Exercise 6

# Exercise 7
