# ����Ҷ�任 -- �� Hilbert Space ������Ҷ�任��

## 1. ���ԣ�����Ҷ�任����Щʲô��

��Ϥ Fourier Transform ��ͯЬ��֪�������� FT �Ĺ�ʽ������ʾ��

<img src="https://www.zhihu.com/equation?tex=\mathcal{FT}(f) = \int^{+\infty}_{-\infty}{x(t)e^{-j(2{\pi}f)t}dt}" alt="\mathcal{FT}(f) = \int^{+\infty}_{-\infty}{x(t)e^{-j(2{\pi}f)t}dt}\\" class="ee_img tr_noresize" eeimg="1">


�����Ȳ�����չ���������ɬ�Ĺ�ʽ�������Ǿ�Զ�Ļ��䣩��Ҳ���������ÿһ��Ԫ�ؽ���ϸ�µ�̽�������� **����һ�� FFT ��Ч��**

�ٸ����ӣ����м������ʦ������������ **<img src="https://www.zhihu.com/equation?tex=(t, x)" alt="(t, x)" class="ee_img tr_noresize" eeimg="1">**, <img src="https://www.zhihu.com/equation?tex=t=0.1, 0.2, ...100" alt="t=0.1, 0.2, ...100" class="ee_img tr_noresize" eeimg="1">��ϣ��ͬѧ�����ĳ���� <img src="https://www.zhihu.com/equation?tex=x=x(t)" alt="x=x(t)" class="ee_img tr_noresize" eeimg="1"> �����������Ǻ����ɷ֣�����ͼ��ʾ�����ڷܵ�С���ۼ��ֿ죬һͨ������������2��Сʱ���Ż�δ�����Ľ��ʮ���±ơ�

![](./figs/2022-01-23-21-00-10.png)

������С������һת���ٺٺ٣������� Fourier Transform (FT)��Ȼ����˸� fftpack 2 ���Ӹ�����������źŷ�Ƶ-��Ƶ���ԣ���ͼ������������ҵ

![](./figs/2022-01-23-21-01-08.png)

<img src="https://www.zhihu.com/equation?tex=" alt="" class="ee_img tr_noresize" eeimg="1">
x(t) = 3 \cdot \cos{(0.1 \cdot 2\pi t - 54^\circ)} +
       \cos{(0.25 \cdot 2\pi t - 90^\circ)} +
       1.5 \cdot \cos{(2\pi t)}
<img src="https://www.zhihu.com/equation?tex=" alt="" class="ee_img tr_noresize" eeimg="1">

Ϲ��һͨ�������ٻع�һ����Ŀ��ԭ���򵥵��ź���ʱ���ϵĵ��ӣ�����**��Ϣ��ѹ����**����������ͨ��ʱ��ͼ�μ򵥵��ж�ԭ���ĳɷ֡�  

![](./figs/2022-01-23-21-13-13.png)

������Ҷ�任ȱ�ɽ�ԭ��ѹ������Ϣ��һ����ԭ��������ʽ��  
����Ҷ�任 = **�źŽ⹹��**�����ź� **���ӵ�ʱ�򹹳�** �⹹Ϊ **��������Ƶ���ʾ**  
��[�����еĻ���](https://www.zhihu.com/question/279808864/answer/498939249)��˵���� **�䷽��ԭ��**  

��������Ҳ������̽�� Fouier Transform ����Ĺ���������Ӧ�ã����ǻع�ͷ����  
**�������ʴ�أ��������Լ�**��Ϊʲô FT ��ʵ�ֽ⹹��Ч��

## 2. ��ŷ�����(Euclidean)�ռ䵽ϣ������(Hilbert)�ռ�

### 2.1 ŷ����ÿռ�

ŷ����ÿռ䣬�ֳ�Ϊ����άʵ�ڻ��걸�ռ䣬��Ȼ�ˣ��۲���Ҫ����**�걸�ռ�**��**�ڻ��ռ�**��**����ά** �ȸ��������ۡ�����άŷ����ÿռ�Ϊ��������ͼ��ʾ������ֻ��Ҫ֪����

- **�ռ��ڻ��Ķ���**��

<img src="https://www.zhihu.com/equation?tex=
\boldsymbol{<x, y>} = \sum_{i=1}^{3}{x_iy_i}" alt="\boldsymbol{<x, y>} = \sum_{i=1}^{3}{x_iy_i}\\" class="ee_img tr_noresize" eeimg="1">

- **�ռ�Ļ�**���ٶ��ÿռ�Ļ�Ϊ
<img src="https://www.zhihu.com/equation?tex=" alt="" class="ee_img tr_noresize" eeimg="1">
\boldsymbol{E = [e_1, e_2, e_3]} =
\left[\begin{matrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{matrix} \right]

<img src="https://www.zhihu.com/equation?tex=- **�����ڿռ��е�����**���ٶ�����Ϊ <img src="https://www.zhihu.com/equation?tex=\boldsymbol{x}" alt="\boldsymbol{x}" class="ee_img tr_noresize" eeimg="1">��������Ϊ�������ڸ������ϵ�ͶӰ" alt="- **�����ڿռ��е�����**���ٶ�����Ϊ <img src="https://www.zhihu.com/equation?tex=\boldsymbol{x}" alt="\boldsymbol{x}" class="ee_img tr_noresize" eeimg="1">��������Ϊ�������ڸ������ϵ�ͶӰ\\" class="ee_img tr_noresize" eeimg="1">
\boldsymbol{coordinate = Ev = [e_1^Tx, e_2^Tx, e_3^Tx]}<img src="https://www.zhihu.com/equation?tex=" alt="" class="ee_img tr_noresize" eeimg="1">

![](./figs/2022-01-23-21-25-36.png)

### 2.2 ϣ�����ؿռ�

������ǵ�Ŀ�ⲻ����������ά�ȣ���ŷ����ÿռ���չΪ����ά�Ⱥ�ʵ���γ��� **ϣ�����ؿռ�**����ŷʽ�ռ��Ӧ�ģ����ڻ����壬�ռ�������������������Ϊ��

- **�ռ��ڻ��Ķ���**��

<img src="https://www.zhihu.com/equation?tex=\boldsymbol{<x(t), y(t)>} = \int_{-\infty}^{+\infty}{x(t)y(t)dt}" alt="\boldsymbol{<x(t), y(t)>} = \int_{-\infty}^{+\infty}{x(t)y(t)dt}\\" class="ee_img tr_noresize" eeimg="1">

- **�ռ�Ļ�**���ٶ��ÿռ�Ļ�ĳһ���ڲ��� <img src="https://www.zhihu.com/equation?tex=\theta" alt="\theta" class="ee_img tr_noresize" eeimg="1"> �ĺ�����

<img src="https://www.zhihu.com/equation?tex=\boldsymbol{E} = [...,e(t;\theta_1), e(t;\theta_2), e(t;\theta_3), ...]" alt="\boldsymbol{E} = [...,e(t;\theta_1), e(t;\theta_2), e(t;\theta_3), ...]\\" class="ee_img tr_noresize" eeimg="1">

- **�����ڿռ��е�����**���ٶ�����Ϊ <img src="https://www.zhihu.com/equation?tex=\boldsymbol{x}(t)" alt="\boldsymbol{x}(t)" class="ee_img tr_noresize" eeimg="1">��������Ϊ�������ڸ������ϵ�ͶӰ
<img src="https://www.zhihu.com/equation?tex=" alt="" class="ee_img tr_noresize" eeimg="1">\boldsymbol{coordinate} =
\left[...,
    \int_{-\infty}^{+\infty}{x(t)e(t;\theta_1)dt},
    \int_{-\infty}^{+\infty}{x(t)e(t;\theta_2)dt},
    \int_{-\infty}^{+\infty}{x(t)e(t;\theta_3)dt}, ...
\right]
<img src="https://www.zhihu.com/equation?tex=" alt="" class="ee_img tr_noresize" eeimg="1">
&emsp;&emsp;&ensp; ���ַ�ʽ��
<font color=red>

<img src="https://www.zhihu.com/equation?tex=coordinate(\theta) = \int_{-\infty}^{+\infty}{x(t)e(t;\theta)dt}" alt="coordinate(\theta) = \int_{-\infty}^{+\infty}{x(t)e(t;\theta)dt}\\" class="ee_img tr_noresize" eeimg="1">

</font>

![](./figs/2022-01-23-21-27-03.png)

## 3. �� Hilbert Space ������Ҷ�任��

�ع�ϣ�����ؿռ��е� **�����ʾ** �� **����Ҷ�任** ��ʽ
<img src="https://www.zhihu.com/equation?tex=" alt="" class="ee_img tr_noresize" eeimg="1"> \left\{
\begin{aligned}
coordinate(\theta) = & \int_{-\infty}^{+\infty}{x(t)e(t;\theta)dt} \\
\mathcal{FT}(f) = & \int^{+\infty}_{-\infty}{x(t)e^{-j(2{\pi}f)t}dt}  
\end{aligned}
\right.

<img src="https://www.zhihu.com/equation?tex=���ǲ��ѷ��֣�����Ҷ�任��ʵ��ϣ�����ؿռ���һ������������ʾ��ʽ��������Ļ�Ϊ���Ǻ�����" alt="���ǲ��ѷ��֣�����Ҷ�任��ʵ��ϣ�����ؿռ���һ������������ʾ��ʽ��������Ļ�Ϊ���Ǻ�����\\" class="ee_img tr_noresize" eeimg="1">

\begin{aligned}
\boldsymbol{E_{fourier}} = & [..., e(t;\theta_1), e(t;\theta_2), e(t;\theta_3), ...] \\
               = & [..., e^{-j(2{\pi}f_1)t}, e^{-j(2{\pi}f_2)t}, e^{-j(2{\pi}f_3)t}, ...]
\end{aligned}
<img src="https://www.zhihu.com/equation?tex=" alt="" class="ee_img tr_noresize" eeimg="1">
���仰˵������Ҷ�任��ʵ��ϣ�����ؿռ��У���
<font color=blue>**���Ǻ������<img src="https://www.zhihu.com/equation?tex=E_{fourier}" alt="E_{fourier}" class="ee_img tr_noresize" eeimg="1">**</font>
ȡ��������<img src="https://www.zhihu.com/equation?tex=^*\boldsymbol{E_{normal}}" alt="^*\boldsymbol{E_{normal}}" class="ee_img tr_noresize" eeimg="1">��
<font color=blue>**�����ʾ����**</font>��  
��Ҷ���ϣ�����ؿռ����棬ֻ������������ <img src="https://www.zhihu.com/equation?tex=\boldsymbol{E_{normal}}" alt="\boldsymbol{E_{normal}}" class="ee_img tr_noresize" eeimg="1"> ���źţ����� <img src="https://www.zhihu.com/equation?tex=x(t)" alt="x(t)" class="ee_img tr_noresize" eeimg="1"> ���ڸ��ӿ���̫����
<font color=blue>**���ұ㻻���Ƕȣ��� <img src="https://www.zhihu.com/equation?tex=\boldsymbol{E_{fourier}}" alt="\boldsymbol{E_{fourier}}" class="ee_img tr_noresize" eeimg="1"> ���۲��ź�**</font>

> <img src="https://www.zhihu.com/equation?tex=^*\boldsymbol{E_{normal}}" alt="^*\boldsymbol{E_{normal}}" class="ee_img tr_noresize" eeimg="1">�����������ָ�����˺����γɵĻ�  
> 
<img src="https://www.zhihu.com/equation?tex=\boldsymbol{E_{normal}} = [...,\delta(t - t_1), \delta(t - t_2), \delta(t - t_3),...]" alt="\boldsymbol{E_{normal}} = [...,\delta(t - t_1), \delta(t - t_2), \delta(t - t_3),...]\\" class="ee_img tr_noresize" eeimg="1">

> &ensp;���� <img src="https://www.zhihu.com/equation?tex=coordinate(t_i)  = x(t_i) = \int_{-\infty}^{+\infty}{x(t)\delta(t - t_i)dt}" alt="coordinate(t_i)  = x(t_i) = \int_{-\infty}^{+\infty}{x(t)\delta(t - t_i)dt}" class="ee_img tr_noresize" eeimg="1">

![Դ��wiki](./figs/Fourier_transform_time_and_frequency_domains_(small).gif)

## 4. XXX�任 -- �任���ǹ۲���ӽ�

˵��������뵱�������Դ�����ѧϰ������任�������������ڽ�������δ�һ������ϵ�任����һ������ϵ��maybe ������һ�� zhexue ��˼��������**��ͬ�ĽǶ�**��һ��������й۲죬������Եõ�һЩ**��ѹ����������������Ϣ**

��˵Զ�ˣ�doge��

˵�������������Ǹ���Ҷ�任��������������Ϥ��������˹�任���ź�����֪��С���任������������ķ����Ա任���ӱ��ĵ���������������������ڲ�ͬ�ĽǶȣ���ͬ����������۲��źţ�**ʹ֮�ɷ�������������ȷ**

![Դ��֪��](https://pic2.zhimg.com/80/cfae89c24cc167c028f02368ee509a68_720w.jpg?source=1940ef5c)

һЩ�����д�˽�����뷨��ϣ������������~
