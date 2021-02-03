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

### Sequences
A *sequence* ${a_n}$ is a list of numbers $a_1, a_2, a_3, \ldots $ We will consider many particular integer sequences in our study of number theory.
#### geometric progression（几何级数）
* **Definition**: A *geometric progression* is a sequence of the form $a, ar, ar^2, ar^3, \ldots , ar^k, \ldots$, where $a$, the *initial term*, and $r$, the *common ratio*, are real numbers.
#### countable and uncountable
* **Definition**: A set is ***countable*** if it is finite or it is infinite and there exists a one-to-one correspondence between the set of positive integers and the set. A set that is not countable is called *uncountable*.

## 1.2 Sums and Products
The following notation represents the sum of the numbers $a_1, a_2, \ldots, a_n$:
$$\sum_{k=1}^na_k = a_1 + a_2 + \cdots + a_n.$$  
The product of the numbers $a_1, a_2, \ldots, a_n$ is denoted by
$$\prod_{j=1}^na_j = a_1 a_2\cdots a_n.$$  
Then $n!$(read as "n factorial"). In terms of product notation, we have $n!=\prod_{j=1}^nj$.

##1.3 Mathematical Induction
#### The Principle of Mathematical Induction  
* **Theorem**: A set of positive integers that contains the integer $1$, and that has the property that, if it contains the integer $k$, then it also contains $k+1$, must be the set of all positive integers.
#### The Second Principle of Mathematical Induction
* **Theorem**: A set of positive integers that contains the integer $1$, and that has the property that, for every positive integer $n$, if it contains all the positive integers $1,2,\ldots,n$, then it also contains the integer $n+1$, must be the set of all positive integers.  
### Recursive Definition
* **Definition**: We say that the function $f$ is ***ddefined recursively*** if the value of $f$ at $1$ is specified and if for each positive integer $n$ a rule is provided for determining $f(n+1)$ from $f(n)$.

## 1.4 The Fibonacci Numbers
* **Definition**: The ***Fibonacci sequence*** is defined recursively by $f_1 = 1, f_2 = 1$, and $f_n = f_{n-1} + f_{n-2}$ for $n\geq 3$. The terms of this sequence are called the ***Fibonacci numbers***.
* **Theorem**: Let $n$ be a positive integer and let $\alpha = \frac{1+\sqrt5}2$ and $\beta = \frac{1-\sqrt5}2$. Then the $n$th Fibonacci number $f_n$ is given by
$$f_n = \frac1{\sqrt5}(\alpha^n - \beta^n).$$

## 1.5 Divisibility
* **Definition**: If $a$ and $b$ are integers with $a \neq 0$, we say that $a$ ***divides*** $b$ if there is an integer $c$ such that $b = ac$. If $a$ divides $b$, we also say that $a$ is a ***divisor*** or ***factor*** of $b$ and that $b$ is a ***multiple*** of $a$.
* **Theorem**: If $a,b$ and $c$ are integers with $a|b$ and $b|c$, then $a|c$.
* **Theorem**: If $a,b,m$ and $n$ are integers, and if $c|a$ and $c|b$, then $c|(ma + nb)$.  
#### The Division Algorithm
* **Theorem**: If $a$ and $b$ are integers such that $b > 0$, then there are unique integers $q$ and $r$ such that $a = bq + r$ with $0 \leq r < b$.  
### Greastest Common Divisors
* **Definition**: The ***greastest common divisor*** of two integers $a$ and $b$, which are not both $0$, is the largest integer that divides both $a$ and $b$.  
* **Definition**: The integers $a$ and $b$, with $a\neq 0$ and $b\neq 0$, are ***relatively prime*** if $a$ and $b$ have greastest common divisor $(a,b)=1$.  
----
# 2. Integer Representations and Operations


