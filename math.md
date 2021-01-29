# 1. The Integers
## 1.1 Numbers and Sequences
### Numbers
#### rational
* **Definition**: The real number $r$ is rational if there are integers $p$ and $q$, with $q \neq 0$, such that $r = p/q$. If $r$ is not rational, it is said to be **irrational**.  

#### algebraic
* **Definition**: A number $\alpha$ is *algebratic* if it is the root of a polynomial with integer coefficients; that is, $\alpha$ is algebraic if there exit integers $a_0,a_1,...,a_n$, such that $a_n\alpha^n + a_{n-1} + \cdots + a_0 = 0$. The number $\alpha$ is called *transcendental（超越的）* if it is not algebraic.  

### The Greatest Integer Function
#### greatest integer
* **Definition**: The *greatest integer* in a real number $x$, denoted by $[x]$, is the largest integer less than or equal to $x$. That is, $\left[x\right]$ is the integer satisfying
$$\left[x\right] \leq x < \left[x\right] + 1.$$  
**Remark**: The greastest integer function is also known as the *floor function*.  

#### fractional part
* **Definition**: The *fractional part* of a real number $x$, denoted by ${x}$, is the largest integer less than or equal to $x$, namely, $\left[x\right]$. That is, ${x} = x - \left[x\right]$.  

### Diophantine Approximation（丢番图逼近）
#### The Pigeonhole Principle
* **Theroem**: If $k + 1$ or more objects are placed into k boxes, then at least one box contains two or more of the objects.  
#### Dirichlet's Approximation Theorem
* **Theroem**: If $\alpha$ is a real number and $n$ is a positive integer, then there exist integers $a$ and $b$ with $1 \leq a \leq n$ such that $\left| a\alpha - b \right| < 1/n$.
