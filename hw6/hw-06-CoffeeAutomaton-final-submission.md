---
id: homework

title: "Homework #6"
author: Coffee Automaton
affiliation: ACM Class, Zhiyuan College, SJTU
course: CS 217 @ SJTU
prof: Dominik Scheder
TA: Tang Shuyang
dueDate: November 14, 2019
papersize: a4
fontsize: 11pt

geometry: margin = 1.5in
mainfont: TeX Gyre Pagella
mainfontoptions:
- Numbers = Proportional
monofont: "Ubuntu Mono"

output:
    custom_document:
        latex_engine: xelatex
        template: ../templates/homework.latex
        highlight: tango
        path: "hw-06-CoffeeAutomaton-final-submission.pdf"
---

@import "homework.less"

# Exercise 1

Let $\nu(G)$ denote the size of a maximum matching of $G$.

For every cycle $x_1,\cdots,x_k$ in the bipartite graph (every cycle has an even length), we can modify the cycle by shaking the weights to
$x_1+\epsilon,x_2-\epsilon,x_3+\epsilon,\cdots,x_k-\epsilon$ until some weight becomes $0$ or $1$.

Repeat the process above until we get a integral graph.

Therefore, $\nu(G)=\text{val}(MLP(G))$ for all bipartite graphs $G$.

# Exercise 2

For every edge $e=(u,v)$ in the match we choose both $u$ and $v$, then we can obtain a vertex cover with size $2\nu(G)$.

Therefore, $\tau(G)\le 2\nu(G)$.

# Exercise 3

Let $C=\{v\in V|x_v\ge\frac{1}{2}\}$, then $C$ is a vertex cover, and $tau(G)\le|C|\le2 \text{opt}(\text{VCLP}(G))$.

# Exercise 5

> **Definition 4.** For $x\in \mathbb R^n$ let $I(x):=\{i\in[m+n]|a_ix=b_i\}$ be the set of indices of the constraints that are *tight*", i.e., satisfied with equality (we include non-negativity constraints here).

Suppose $C$ is a vertex cover, and $F$ be the set of tight edges.

From **Definition 4**, since we have we translated the constraint $x\ge 0$ into $n$ constraints $−x_i\le 0$ and integrated them into $A$, which implies

* $i\in I(x)$ iff $e_i$ is a tight edge for $1\le i\le m$

* $i\in I(x)$ iff $v_{i-m}\notin C$ for $1\le i\le n$

1. If $y_u\in\{0,1\}$ for all $u\in V$ and $C$ is a minimal vertex cover, then $I(x)$ contains vertices that are not covered and all tight edges. We have $\text{rank}(A_{I(x)})=n$ so $y$ is a basic solution of $\text{VCLP}(G)$.

2. If $y$ is a basic solution of $\text{VCLP}(G)$, $y$ is the solution of $A_{I(y)}y=b_{I(y)}$. Then $I(y)$ contains the vertices that are not covered and all tight edges. To satisfy all the constraints, $y$ must be an integral vector, that is, $y_u\in\{0,1\}$ for all $u\in V$, and $C$ is a vertex cover of $G$. To show $C$ is a minimal vertex cover, consider removing some vertex $u$ from $C$, the constraints can't be satisfied, then $C\backslash\{u\}$ can't be a vertex cover. Therefore, $C$ is a minimal vertex cover.

In conclusion, $y$ is a basic solution of $\text{VCLP}(G)$ iff $y_u\in\{0,1\}$ for all $u\in V$ and $C$ is a minimal vertex cover.
