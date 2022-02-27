
人体收缩压（SBP）与脉搏波传递时间PWTT存在较高的线性相关关系，建立基于加速脉搏波的PWTT提取算法建立与收缩压的线性模型


![](https://imgconvert.csdnimg.cn/aHR0cDovL3R2YXg0LnNpbmFpbWcuY24vbXc2OTAvMDA2TG5mZlRseTFnOGx0dW9xc2F3ajMwamcwOXJnbm4uanBn?x-oss-process=image/format,png)

根据PPG与ECG个别的生理特征点，可以发现ECG的峰值来自于心室的收缩，而PPG的峰值则是因为血管收缩所造成的，因此可以得到血液自心脏送出后到达量测部位的传输时间，也就是脉搏波传递时间Pulse Transit Time (PTT)。

脉搏波传递的速度与血压是直接相关的，血压高时，脉搏波传递快，反之则慢，所以通过心电信号ECG与脉搏波信号PPG获得脉搏传递时间 (PTT)，再加上常规的一些身体参数 (如身高、体重) 即可得出脉搏波传递速度，通过建立的特征方程来估计人体脉搏的收缩压与舒张压，可实现无创连续血压测量。

计算公式
收缩压:
BP=A*PWTT+B
舒张压:
![](https://imgconvert.csdnimg.cn/aHR0cHM6Ly90dmEzLnNpbmFpbWcuY24vbXc2OTAvMDA2TG5mZlRseTFnOGhqODVuaWJ6ajMwaGIwNWlteGwuanBn?x-oss-process=image/format,png)

测量心率时，手臂的ECG信号要比PPG信号更稳定

算法评估指标
平均绝对误差
平均绝对误差百分比
皮尔逊相关系数
Bland-Altman图

![](https://imgconvert.csdnimg.cn/aHR0cDovL3R2YXg0LnNpbmFpbWcuY24vbXc2OTAvMDA2TG5mZlRseTFnOWNmZ25rYmViajMwaXEwZGk3NWsuanBn?x-oss-process=image/format,png)


PPG技术目前存在的问题（挑战）
采集PPG信号的光学噪声。PPG信号的去噪处理，特别是将生理信号与噪声信号分离（运动过程中产生的噪声），是该技术目前面临的最大障碍。
肤色的吸收率。PPG传感器中光电二极管（PD）采集到的信号强度取决于穿戴者的肤色。影响因素有：黑皮肤、黄皮肤、白皮肤、有无纹身、有无伤疤

![](https://img-blog.csdnimg.cn/img_convert/f35a2c2b9e457d481c92f9e85b982095.png)

PPG传感器的安装位置。市面上大多数的光学心率传感器是佩戴在三个部位：耳朵(耳塞式耳机)、手臂(佩戴在手臂较高或较低位置的臂带)、手腕(智能手表或是健身追踪腕带)。
**手腕是准确进行PPG心率量测的最差部位之一**，而皮肤表面血管密度较高的前臂，被认为是较好的位置，耳朵则是迄今在人体放置光学心率监测器的最佳位置。

周期性活动所产生的光学噪声（慢跑时），心率与步伐速度彼此交错

低灌注流量。灌流是人体推送血液到微血管床(capillary bed)的过程，如同肤色，血液灌流程度在不同人之间有高度差异，可能受到肥胖、糖尿病或心脏动脉疾病的影响，使得血液灌流量降低。低灌流量─特别是在人体四肢，会对光学心率监测器带来挑战，因为信噪比可能会显著降低，而较低的灌流量与较低的血流信号相关联。

心率传感器的供应商有Maxim、ADI、AMS、Osram、Partron、TI、Pixart,汇顶等，算法公司有firstBeat（被Garmin收购）、Gomore、LifeQ等公司，可以评估参数包括健康生活指标类、训练期间评估类、训练管理类。

PPG信号质量评估方法
基于R波检测的匹配度，采样幅值法和斜率法检测PPG信号中R波位置。通过对比两种方法的匹配度评估信号质量。
Sukor提出脉冲幅度、连续波谷之间的波谷深度差、脉冲宽度
六个PPG信号的形态学特征作为评估信号质量的方法：
(1)具有正峰值的搏动波形(两个负峰值之间的间隔)，
(2)具有负峰值的搏动波形(两个正峰值之间的间隔)，
(3)两个连续负峰值之间的绝对幅度变化，
(4)两个连续正峰值之间的绝对幅度变化，
(5)从正峰值和负峰值(或脉冲宽度)提取的心率，
(6)绝对正到负峰值幅度，即交流信号质量受到环境光、低灌注、运动的影响


日光灯的同一个强度，在不同的pd上有不同的强度叠加，是否是因为这个造成了各个pd 之间的差异呢？
也不一定完全是，有些时候没有漏光也有问题

需要设计实验，在暗室中增加测量看看是否还会出现这个问题！！！
就明显出现问题的时候，套上黑色袋子或者遮光，看看血氧是否恢复！！！

