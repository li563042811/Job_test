"""
算法面试知识点
"""
'''
1、SGD,Momentum、Adagard、Adam原理
    SGD为随机梯度下降,每一次迭代计算数据集的mini-batch的梯度,然后对参数进行更新。
Momentum参考了物理中动量的概念,前几次的梯度也会参与到当前的计算中,但是前几轮的梯度叠加在当前计算中会有一定的衰减。
Adagard在训练的过程中可以自动变更学习的速率,设置一个全局的学习率,而实际的学习率与以往的参数模和的开方成反比。
Adam利用梯度的一阶矩估计和二阶矩估计动态调整每个参数的学习率,在经过偏置的校正后,每一次迭代后的学习率都有个确定的范围,使得参数较为平稳。
'''
'''
2、L1不可导的时候该怎么办
    当损失函数不可导,梯度下降不再有效,可以使用坐标轴下降法,梯度下降是沿着当前点的负梯度方向进行参数更新,而坐标轴下降法是沿着坐标轴的方向,假设有m个特征个数,坐标轴下降法进参数更新的时候,先固定m-1个值,然后再求另外一个的局部最优解,从而避免损失函数不可导问题。
使用Proximal Algorithm对L1进行求解,此方法是去优化损失函数上界结果。
'''
'''
3、sigmoid函数特性
    定义域为负无穷到正无穷
值域为(-1,1)
函数在定义域内为连续和光滑的函数
处处可导,导数为f(x)(1-f(x))
'''
'''
4、什么是共轭先验分布
    如果先验密度函数和后验密度函数具有相同的函数形式，则成为共轭先验分布。
'''
'''
5、概率和似然的区别
    概率是指在给定参数的情况下,样本的随机向量X=x的可能性。而似然表示的是在给定样本X=x的情况下,参数为真实值的可能性。一般情况,对随机变量的取值用概率表示。而在非贝叶斯统计的情况下,参数为一个实数而不是随机变量,一般用似然来表示。
'''
'''
6、矩阵正定性的判断,Hessian矩阵正定性在梯度下降中的应用
    若矩阵所有特征值均不小于0,则判定为半正定。若矩阵所有特征值均大于0,则判定为正定。在判断优化算法的可行性时Hessian矩阵的正定性起到了很大的作用,若Hessian正定,则函数的二阶偏导恒大于0,函数的变化率处于递增状态,在牛顿法等梯度下降的方法中,Hessian矩阵的正定性可以很容易的判断函数是否可收敛到局部或全局最优解。
'''
'''
7、讲一下PCA
    PCA是比较常见的线性降维方法,通过线性投影将高维数据映射到低维数据中,所期望的是在投影的维度上,新特征自身的方差尽量大,方差越大特征越有效,尽量使产生的新特征间的相关性越小。
PCA算法的具体操作为对所有的样本进行中心化操作,计算样本的协方差矩阵,然后对协方差矩阵做特征值分解,取最大的n个特征值对应的特征向量构造投影矩阵。
'''
'''
8、DQN的Trick
    第一个Trick。DQN引入卷积层。模型通过Atari游戏视频图像了解环境信息并学习策略。
    第二个Trick。Experience Replay。储存Agent Experience样本，每次训练随机抽取部分样本供网络学习。稳定完成学习任务，避免短视只学习最新接触样本，综合反复利用过往大量样本学习。
    第三个Trick。用第二个DQN网络辅助训练，target DQN，辅助计算目标Q值，提供学习目标公式里的maxaQ(st+1,a)。
    第四个Trick。Double DQN。传统DQN高估Action Q值，高估不均匀，导致次优Action被高估超过最优Action。
    第五个Trick。Dueling DQN。Dueling DQN，Q值函数Q(st,at)拆分，一部分静态环境状态具有价值V(st)，Value；另一部分动态选择Action额外带来价值A(at)，Advantage。
'''