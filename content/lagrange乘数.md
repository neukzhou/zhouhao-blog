title: Lagrange乘数法
date: 2014-10-20 22:54
category: 一点数学
tags: Larange, 机器学习, 数学
author: ZhouHao
slug: lagrange_multiplier

作者：周昊 出处：http://www.zhouhao.me

机器学习的本质就是解决一个优化问题，或者是以似然函数作为目标函数，或者是以代价函数(一般为损失的均方差)作为优化的对象。而一般来说，如果优化问题非凸，那么我们就很难得到一个全局最优解，并且内部的极值就是最值。因此，必须将目标函数转化为一个凸函数。而问题转化为凸函数后，就可以用模式化的方法解决了。

<!-- PELICAN_END_SUMMARY -->

总的来说，凸优化问题可以分成无约束和有约束两种。无约束优化形如下式：

$$ \min_\omega f(\omega) $$

由于 $\max f(\omega) = \min \left(-f(\omega)\right)$ ，因此以下只考虑最小值的情形。

这种形式的解法就是令其梯度为0即可：

$$ \nabla f(\omega) := 0 $$

有些问题可以求出上式的解析解（如线性规划问题可以用最小二乘法求出最优 $\omega^*$ ），但由于往往涉及到一些矩阵逆或者乘法运算，当$\omega$维度很高时，计算量会变得很大。此外，还有很多目标函数无法求得解析解。因此，求解此类问题常采用梯度下降法(Gradient Descent)。

有约束优化的情形就是在其基础上增加一个或多个约束条件。这些条件可能是等式约束：

$$ h_i(\omega) = 0, i = 1,\dots,l. $$

也可能是一些不等约束：

$$ g_i(\omega) \leq 0, k = 1,\dots,k. $$

事实上，严格小于可以放松为小于等于，大于等于可以两边同时取负就能得到上式。因此，小于等于约束是完备的不等约束。

于是有约束优化问题可以形式化如下：

$$
\begin{align\*}
\min_\omega \quad & f(\omega) \\\
s.t. \quad & g_i(\omega) \leq 0, k = 1,\dots,k.\\\
	 & h_i(\omega) = 0, i = 1,\dots,l.
\end{align*}
$$

## 等式约束

试想若约束条件只包含等式：

$$
\begin{align\*}
\min_\omega \quad & f(\omega) \\\
s.t. \quad & h_i(\omega) = 0, i = 1,\dots,l.
\end{align*}
$$

令

$$ f(\omega) := d $$

那么在二维情况，可以作图如下：

<img src="http://upload.wikimedia.org/wikipedia/commons/5/55/LagrangeMultipliers3D.png" title="二元函数优化" width="400" />   
图1 二元函数优化

<img src="http://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/LagrangeMultipliers2D.svg/1000px-LagrangeMultipliers2D.svg.png" title="等高线图" width="400" />      
图2 等高线图

图中蓝虚线为当d取不同值时 $f(\omega)=d$ 的图像，红实线为某个约束条件 $h_i(\omega) = 0$ 的图像。那么，当两者有交点时，存在可行解 $\hat{\omega}$ 。可以看到若两者相交，一定存在一个更小的 $\hat{d}$ 也满足条件，于是，当且仅当两者**相切**时取得极小值，即两函数在该点梯度平行，此时满足：

$$
\nabla f(\omega) = -\beta_i \nabla h_i(\omega) \quad (\beta \ne 0)
$$
这里取 $-\beta_i$ 是为了之后Lagrange乘式中 $\beta_i$ 前方无负号。

引入函数

$$
\mathcal{L}(\omega, \beta_i) := f(\omega) + \beta_i h_i(\omega)
$$

那么极值时有：

$$
\nabla_\omega \mathcal{L} = \nabla f(\omega) + \beta_i \nabla h_i(\omega) = 0
$$

考虑到约束条件，于是还有

$$
\frac{\partial \mathcal{L}} {\partial \beta_i} = h(\omega) = 0
$$

考虑到有 $l$ 个等式约束，那么上式改写为：

$$
\mathcal{L}(\omega, \beta_1, \dots, \beta_l) := f(\omega) + \sum_{i=1}^l \beta_i h_i(\omega)
$$

写成向量形式有：

$$
\mathcal{L}(\omega, \beta) := f(\omega) + \beta^T h(\omega)
$$

取极值时：

$$
\begin{align\*}
\nabla\_\omega \mathcal{L} &= 0 \\\
\nabla_\beta \mathcal{L} &= 0
\end{align*}
$$

### 例一 离散变量最大熵

对于一个包含n个状态的离散分布，求其最大熵，则有：

$$
\max H(p), \quad s.t. \sum_{i=1}^n p_i = 1.
$$

等价于

$$
\min \sum\_{i=1}^n p_i \log p_i \quad s.t. \sum_{i=1}^n p_i = 1.
$$

于是构造Lagrange乘式

$$
\mathcal{L}(p, \beta) = \sum\_{i=1}^n p_i \log p_i + \beta (\sum_{i=1}^n p_i - 1)
$$

$$
\frac{\partial \mathcal{L}} {\partial p_i} = \log p_i + 1 + \beta = 0
$$

于是

$$
p_1 = p_2 = \dots = p_n = e^{-1-\beta}
$$

又有

$$
\frac{\partial \mathcal{L}} {\partial \beta} = \sum_{i=1}^n p_i - 1 = 0
$$

所以

$$
p_1 = p_2 = \dots = p_n = \frac{1} {n}
$$

### 例二 连续变量最大熵

求解一个连续变量的最大熵问题如下：

$$
\begin{align\*}
\max \quad & H \left( p(x) \right) = -\int\_{-\infty}^{+\infty} p(x) \ln p(x) dx \\\
s.t. \quad &  \int\_{-\infty}^{+\infty}p(x)dx = 1 \\\
		   &  \int\_{-\infty}^{+\infty}xp(x)dx = \mu \\\
		   &  \int_{-\infty}^{+\infty}(x-\mu)^2 p(x)dx = \sigma^2
\end{align*}
$$

同样构造

$$
\mathcal{L} = H \left( p(x) \right) 
	+ \beta_1 \left( \int\_{-\infty}^{+\infty}p(x) - 1 \right)
	+ \beta_2 \left( \int\_{-\infty}^{+\infty}xp(x) - \mu \right)
	+ \beta_3 \left( \int_{-\infty}^{+\infty}(x-\mu)^2 p(x) - \sigma^2 \right)
$$

于是令 $ \delta \mathcal{L} := 0 $ ，由变分法得

$$
\frac{\delta \mathcal{L}} {\delta p} = \ln p(x) - \beta_3 (x-\mu)^2 - \beta_2 x - (\beta_1 - 1) = 0 
$$

于是

$$
p(x) = \exp \left( -1 + \beta_1 + \beta_2 x + \beta_3 (x-\mu)^2 \right)
$$

将上式代入三个约束条件即可求出参数 $\beta$ 。

最终得到

$$
p(x) = \frac{1}{ \sqrt{2\pi} \sigma } \exp \left( -\frac{ (x-\mu)^2 }{ 2\sigma^2 } \right)
$$


## 不等约束

重新考虑上面的问题

$$
\begin{align\*}
\min_\omega \quad & f(\omega) \\\
s.t. \quad & g_i(\omega) \leq 0, k = 1,\dots,k.\\\
	 & h_i(\omega) = 0, i = 1,\dots,l.
\end{align*}
$$

类似的构造Lagrange乘式：

$$
\mathcal{L} (\omega, \alpha, \beta) = f(\omega) + \sum\_{i=1}^k \alpha_i g_i(\omega) + \sum_{i=1}^l \beta_i h_i(\omega)
$$

考虑这样一个基本式子（后面将证明下式等价于 $f(\omega)$ ）

$$
\theta\_{\mathcal{P}} (\omega) = \max_{\alpha,\beta:\alpha_i \geq 0} \mathcal{L} (\omega, \alpha, \beta).
$$

说明一下为什么需要限定 $\alpha_i \geq 0$。这是因为，若$\alpha_i < 0$，则

$$
\max \alpha_i g_i(\omega) = \infty
$$

另一方面，

$$
\begin{align\*}
\theta\_{\mathcal{P}} (\omega) & = \max\_{\alpha,\beta:\alpha_i \geq 0} \mathcal{L} (\omega, \alpha, \beta) \\\
&= f(\omega) + \sum\_{i=1}^k \max_{\alpha_i \geq 0} \alpha_i g_i(\omega)
\end{align*}
$$

注意到，若 $g_i(\omega) = 0$，则 $\alpha_i g_i(\omega) = 0$ 。若 $g_i(\omega) < 0$，则 $\alpha_i g_i(\omega) \leq 0$ 。于是当 $\alpha_i = 0$ 时， $\max_{\alpha_i \geq 0} \alpha_i g_i(\omega) = 0$ 。

因此，

$$
\begin{align\*}
& if g_i(\omega) \leq 0, h_i(\omega) = 0:\\\
& \quad \theta\_{\mathcal{P}} (\omega) = f(\omega)\\\
& otherwise: \\\
& \quad \theta\_{\mathcal{P}} (\omega) = \infty
\end{align*}
$$

于是，原命题转化为

$$
\mathcal{P}^* = \min\_\omega f(\omega) = \min_\omega \max\_{\alpha,\beta:\alpha_i \geq 0} \mathcal{L} (\omega, \alpha, \beta)
$$

### 对偶式的引入

在这里注意到，若直接求解上式，将涉及到两层循环，计算量非常大。因此，必须把上式化简为单层循环。另一方面，上式是先固定一个 $\omega$ 调整 $\alpha, \beta$ 使其取得极值，再对 $\omega$ 使用梯度下降进行一次迭代。这使我们对 $\omega$ 采用凸优化方法求解不方便。因此，我们需要引入上式的对偶命题：

$$
\mathcal{D}^* = \max\_{\alpha,\beta:\alpha_i \geq 0} \min_\omega \mathcal{L} (\omega, \alpha, \beta)
$$

一个普遍的常识是，一个函数的最大值的最小化( $\min \max f$ )会大于或等于其最小值的最大化( $\max \min f$ )，于是

$$ p^\* \geq d^* $$

### KKT条件

上面的式子仅仅说明了，对于任意的情况都有 $ p^\* \geq d^\* $。但这个条件并不足以让我们直接用 $d^\*$ 来替代 $p^\*$。于是，我们必须考虑什么情况下 $ d^\* = p^\* = \mathcal{L} (\omega^\*, \alpha^\*, \beta^\*) $，这就是我们要引入的KKT条件。

Karush-Kuhn-Tucker (KKT) conditions:

$$
\begin{align\*}
\nabla\_\omega \mathcal{L} (\omega^\*, \alpha^\*, \beta^\*) &= 0  \quad (与等式约束时相同)\\\
\nabla_\beta \mathcal{L} (\omega^\*, \alpha^\*, \beta^\*) &= 0 \quad (与等式约束时相同) \\\
\left( \alpha^\* \right)^T g(\omega^\*) &= 0 \\\
g(\omega^\*) &\leq  0 \\\
\alpha^\* &= 0
\end{align*}
$$

当优化问题满足KKT条件时，就有 $d^\* = p^\*$ 成立。由上面的过程可知，我们所提出的包含不等约束的优化问题满足KKT条件，于是

$$
d^\* = p^\*
$$

## Lagrange乘数与支持向量机

支持向量机可化为下面的约束优化问题：

$$
\begin{align\*}
\min_{w,b} & \quad \frac{1}{2} ||w||^2 \\\
s.t & \quad y^{(i)}(w^Tx^{(i)}+b) \geq 1, \quad i = 1, \dots, m
\end{align*}
$$

于是取

$$
g_i(w) := -y^{(i)}(w^Tx^{(i)}+b) + 1 \leq 0
$$

可以构造Lagrange函数：

$$
\mathcal{L} (w, b, \alpha) = \frac{1}{2} ||w||^2 - \sum_{i=1}^m \alpha_i \left[ y^{(i)} (w^Tx^{(i)} + b) - 1 \right]
$$

原命题等价于

$$
\mathcal{L} (w^\*, b^\*, \alpha^\*) = \min_{w,b} \max\_{\alpha_i:\alpha_i \geq 0} \mathcal{L} (w, b, \alpha)
$$

可以验证其满足KKT条件，于是

$$
\max\_{\alpha_i:\alpha_i \geq 0} \min\_{w,b} \mathcal{L} (w, b, \alpha) = \min_{w,b} \max\_{\alpha_i:\alpha_i \geq 0} \mathcal{L} (w, b, \alpha)
$$

由于 $\mathcal{L}$ 关于 $w,b$ 是凸函数，因此极值点即为最值点，那么有

$$
\nabla\_w \mathcal{L} (w, b, \alpha) = w - \sum_{i=1}^m \alpha_iy^{(i)}x^{(i)} = 0
$$

即

$$
w = \sum_{i=1}^m \alpha_iy^{(i)}x^{(i)}
$$

$$
\frac{\partial}{\partial b} \mathcal{L}(w,b,\alpha) = \sum_{i=1}^m a_i y^{(i)} = 0
$$

这实际上就是KKT条件的一部分。

把 $w$ 代入 $\mathcal{L}$ 得到

$$
L(w,b,\alpha) = 
\sum\_{i=1}^m \alpha_i - \frac{1}{2} \sum\_{i=1}^m \sum_{j=1}^m y^{(i)}{(j)}\alpha_i \alpha_j \left( x^{(i)} \right)^T x^{(j)}
$$

于是原来的两阶优化问题就降为一阶了：

$$
\begin{align\*}
\max\_\alpha & \quad 
\sum\_{i=1}^m \alpha_i - \frac{1}{2} \sum\_{i=1}^m \sum\_{j=1}^m y^{(i)}{(j)}\alpha_i \alpha_j \left( x^{(i)} \right)^T x^{(j)} \\\
s.t. & \quad \alpha_i \geq 0, \quad i = 1, \dots, m \\\
& \quad \sum_{i=1}^m a_i y^{(i)} = 0.
\end{align*}
$$

利用最优化算法（常常引入Kernel method），解出最优解后代入下式，即可求得 $w, b$ ：

$$
w^\* = \sum_{i=1}^m \alpha_i^\* y^{(i)}x^{(i)}
$$

$$
b^\* = -\frac{1}{2} \left( \max\_{i:y^{(i)}=-1} (w^\*)^Tx^{(i)} + \min\_{i:y^{(i)}=1} (w^\*)^Tx^{(i)}\right)
$$