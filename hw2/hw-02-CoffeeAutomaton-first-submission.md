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

If we want to find the maximum item in $n$ items, to ensure it is the maximum, it should be compared with all others directly or indirectly, so any algorithms should be at least $n-1$ comparisons. 

If not, there is no comparison between the "maximum" and some others, and we can not ensure its correctness.

# Exercise 2

Record the maximum and the minimum.

Fetch $2$ items each time, compare them, compare the smaller item and the minimum, and compare the bigger item and the maximum.

The algorithm shows below.

@import "2.2.py"

The algorithm all use $1+(\frac{n-2}{2})\times 3=\frac{3n}{2}-2$ comparisons.

# Exercise 3

Each time compare two items, take the larger one to the next round, and after $k-1$ rounds, there are two items. Compare them, and get the "max" and the "second".

Then find the items those were compared with the "max", compare them with "second". the maximum is the second largest item.

The algorithm shows below.

@import "2.3.py"

It all uses $\frac{n}{2}+\frac{n}{4}+\cdots+2+1+(k-1)=n+k-2=n+\log_2(n)-2$ comparisons.

# Exercise 4

Set the expected number of comparisons as $S$.

$$\begin{aligned}
S&=\mathbf{E}[\sum_{i\neq j} A_{i,j}]\\
&=\sum_{i\neq j}\mathbf{E}[A_{i,j}]\\
&=\sum_{i}\sum_{j}\frac{1}{|i-j|+1}-n
\end{aligned}$$

Now considering the summation,as matrix (1) shows, the summation of the matrix equals the summation.

$$\begin{align}
\begin{pmatrix}
1&\dfrac{1}{2}&\dfrac{1}{3}&\cdots& &\dfrac{1}{n}\\
\dfrac{1}{2}&1&\dfrac{1}{2}&\cdots&&\dfrac{1}{n-1}\\\cdots
& &...\\
\dfrac{1}{n-1}&\dfrac{1}{n-2}& &\cdots&1&\dfrac{1}{2}\\
\dfrac{1}{n}&1&\dfrac{1}{n-1}&\cdots&\dfrac{1}{2}&1\\
\end{pmatrix}
\end{align}$$

Using the Harmonic number $H_{n}=1+\frac{1}{2}+\cdots+\frac{1}{n}$

$$\begin{aligned}
S&=\sum_{i}\sum_{j}\frac{1}{|i-j|+1}-n\\
&=n\times 1+2\times(n-1)\times\frac{1}{2}+2\times(n-2)\times\frac{1}{3}+\cdots+2\times(n-(n-1))\times\frac{1}{n}-n\\
&=2\left(\frac{n}{2}+\frac{n}{3}+\cdots+\frac{n}{n}-\frac{1}{2}-\frac{2}{3}-\cdots-\frac{n-1}{n}\right)\\
&=2\left(n\left(\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n})-(\frac{1}{2}+\frac{2}{3}+\cdots+\frac{n-1}{n}\right)\right)\\
&=2\left(n\left(H_{n}-1\right)-\left(\left(1-1\right)+\left(1-\frac{1}{2}\right)+\left(1-\frac{1}{3}\right)+\cdots+\left(1-\frac{1}{n}\right)\right)\right)\\
&=2\left(n\left(H_{n}-1\right)-\left(n-H_{n}\right)\right)\\
&=2\left(n+1\right)H_{n}-4n
\end{aligned}$$

Which is the expected number of comparisons.

# Exercise 5

The QuickSelect method first chooses a random pivot $k$, and divide the array into $k$ and two parts: bigger than $k$, smaller than $k$, which is same as quicksort.

However, quickselect only concern one of the two parts, and omit the other, while quicksort concern the both. So we can say that quickselect is a “partial execution” of quicksort.

The example quicksort tree to find $4$ shows in Figure 1, and the red part is visited by quickselect.

![Figure 1: The quicksort tree in Exercise 5](1.png)

# Exercise 6

If $\mathbf{E}[B_{i,j,k}]=1$, then $k$ is the ancestor of $i$ and $j$.

Considering the Lemma of $A_{i,j}$:$A_{i,j}=1$ if and only if among the elements of $[i:j]$, element i comes first in the input array.

So, $B_{i,j,k}=1$ if and only if i comes first in $[i,j]$ and $[i,k]$.

The length of section is $\max(i,j,k)-\min(i,j,k)$, so $B_{i,j,k}=\dfrac{1}{\max(i,j,k)-\min(i,j,k)+1}$.

# Exercise 7

Because $\pi$ is the random array with length $n$, so we set function $f(n,k)=\mathbf{E}_{\pi}[C(\pi,k)]$.

According to the recurrence relation, we can have the following derivation:
$$\begin{aligned}
f(n,k)&=\dfrac{\sum_{i=k+1}^{n}f(i-1,k)+\sum_{i=1}^{k-1}f(n-i,k-i)}{n}+n\\
nf(n,k)&=\sum_{i=k}^{n}f(i-1,k)+\sum_{i=1}^{k-1}f(n-i,k-i)+n^2\\
(n-1)f(n-1,k)&=\sum_{i=k}^{n-1}f(i-1,k)+\sum_{i=1}^{k-1}f(n-i,k-i)+n^2\\
nf(n-1,k)&=\sum_{i=k}^{n}f(i-1,k)+\sum_{i=1}^{k-1}f(n-i,k-i)+n^2\\
f(n,k)-f(n-1,k)&=\sum_{i=1}^{k-1}\left(f(n-i,k-i)-f(n-i-1,k-i)\right)+2-\frac{1}{n}
\end{aligned}$$

Define $g(n,k)=f(n,k)-f(n-1,k)$

$$\begin{aligned}
ng(n,k)&=\sum_{i=1}^{k-1}g(n-i,k-i)+2n-1\\
(n+1)g(n+1,k+1)-ng(n,k)&=\sum_{i=1}^{k}g(n-i+1,k+1-i)-\sum_{i=1}^{k-1}g(n-i,k-i)\\
&=g(n,k)\\
\therefore(n+1)g(n+1,k+1)&=(n+1)g(n,k)\\
g(n+1,k+1)&=g(n,k)\\
\therefore g(n,k)&=g(n-k+1,1)\\
\end{aligned}$$

When $k=1$, we have

$$\begin{align}
ng(n,k)&=\sum_{i=1}^{k-1}g(n-i,k-i)+2n-1\\
&=2n-1\\
g(n,1)&=2-\frac{1}{n}\\
f(n,1)&=2n-\sum_{i=1}^{n}\frac{1}{i}\\
\therefore g(n,k)&=2-\frac{1}{n-k+1}
\end{align}$$

By symmetry, we have $f(n,k)=f(n,\lfloor n-k+1\rfloor)$

$$\begin{align}
f(n,k)&=\sum_{i=k+1}^{n}g(i,k)+f(k,k)\\
\because f(k,k)&=f(k,1)=2k-\sum_{i=1}^{k}\frac{1}{i}\\
f(n,k)&=2n-\sum_{i=1}^{k}\frac{1}{i}-\frac{i=2}{n-k+1}\frac{1}{i}\\
&=2n-H_{k}-H_{n-k+1}+1\\
&=\mathbf{E}_{\pi}[C(\pi,k)]
\end{align}$$

Which above is the formula for $C(\pi,k)$.

# Exercise 8

By exercise 7, $C(\pi,1)=2n-H_{n}=o(n)+o(n)+\ln(n)+O(1)$, so the additive terms is $o(n)+\ln(n)+O(1)$.

# Exercise 9

It has been showed in exercise 7.

$$\begin{aligned}
\mathbf{E}_{\pi}[C(\pi,k)]&=2n-H_{k}-H_{n-k+1}+1
\end{aligned}$$

# Exercise 2

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


$$\sum_{i\neq j\\i\neq k\\j\neq k}B_{i,j,k}$$