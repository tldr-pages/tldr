# pbmupc

> 生成一个通用产品代码（UPC）的 PBM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmupc.html>.

- 为指定的产品类型、制造商代码和产品代码生成 UPC 图像：

`pbmupc {{product_type}} {{manufacturer_code}} {{product_code}} > {{path/to/output.pbm}}`

- 使用不显示校验码的替代样式：

`pbmupc -s2 {{product_type}} {{manufacturer_code}} {{product_code}} > {{path/to/output.pbm}}`