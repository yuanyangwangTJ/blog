本文分析**FA（自动机）**转化为**正则表达式**的方式，通过转化示例进行详细说明.

# 转换基本定理
FA转换为正则表达式基于以下三种基本方式：  
* **自动机状态逐次相连**  
![](https://raw.githubusercontent.com/yuanyangwangTJ/Picture/master/img/20210411153407.png)

* **两自动机状态多种方式转换**  
![](https://raw.githubusercontent.com/yuanyangwangTJ/Picture/master/img/20210411153800.png)

* **自动机中间状态自变换**  
![](https://raw.githubusercontent.com/yuanyangwangTJ/Picture/master/img/20210411154001.png)

以上是三种基本转换方式，除此之外，还需要考虑对于自动机终止状态集的处理，即通过添加额外的终止状态以及使用漂移的方式来转化为单终止状态自动机，如下所示：  
![](https://raw.githubusercontent.com/yuanyangwangTJ/Picture/master/img/20210411154347.png)

# 示例分析
下面通过一个具体题目详细介绍转化过程，题目的自动机如下所示：  
![FA](https://raw.githubusercontent.com/yuanyangwangTJ/Picture/master/img/20210411154658.png)

上面的自动机拥有两个终止状态，首先考虑**终止状态集**的处理，转化如下：  
![FA](https://raw.githubusercontent.com/yuanyangwangTJ/Picture/master/img/20210411154906.png)

注意上面的 $\lambda$ 和 $\varepsilon$ 意义相同，表示漂移状态.

然后便是正式转化部分了，FA转化为正则表达式基于以上三种情况采用**逐次消除状态**的方式，如下：
* **消去q1状态**  
下面是消去q1状态的结果：  
![](https://raw.githubusercontent.com/yuanyangwangTJ/Picture/master/img/20210411160223.png)

消去q1状态，需要刷新q0和q2**自身的状态循环方式**，同时，也要考虑**通过q1状态到达其他状态的路径**刷新，在本次消除中有q0->q1->q2，q0->q1->q3，q2->q1->q0，q2->q1->q3，**不要忽视任何一条路径的刷新**.

* **消去q2状态**  
按照消去q1的方式，也可以消去q2，得到下面的结果：
![](https://raw.githubusercontent.com/yuanyangwangTJ/Picture/master/img/20210411155419.png)

* **最终转换**
按照基本的转化方式，便可以得到最终的表达式，如下：  
$(00+(1+00)(10)* (1+10)) * (0+(1+00)(10)* (\varepsilon+1))$

****
综上，便是自动机转换正则表达式的方法.

# 参考文章
文章部分示意图来源于以下文章，侵权立删.
[正则表达式和自动机的相互转化](https://blog.csdn.net/sinat_41104353/article/details/88833198)
