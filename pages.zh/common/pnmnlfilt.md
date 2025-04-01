# pnmnlfilt

> 对 PNM 图像应用非线性滤波器。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmnlfilt.html>.

- 对 PNM 图像应用指定的 alpha 和半径值的 "alpha 修剪均值" 滤波器：

`pnmnlfilt {{0.0..0.5}} {{radius}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 对 PNM 图像应用指定的噪声阈值和半径的 "最优估计平滑" 滤波器：

`pnmnlfilt {{1.0..2.0}} {{radius}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 对 PNM 图像应用指定的 alpha 和半径的 "边缘增强" 滤波器：

`pnmnlfilt {{-0.9..(-0.1)}} {{radius}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`