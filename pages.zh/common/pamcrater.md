# pamcrater

> 创建一个环形山地形的 PAM 图像。
> 参见：`pamshadedrelief`，`ppmrelief`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamcrater.html>.

- 创建指定尺寸的环形山地形图像：

`pamcrater -height {{height}} -width {{width}} > {{path/to/output.pam}}`

- 创建包含指定数量环形山的图像：

`pamcrater -number {{n_craters}} > {{path/to/output.pam}}`