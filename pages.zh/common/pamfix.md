# pamfix

> 修复 PAM、PBM、PGM 和 PPM 文件中的错误。
> 参见：`pamfile`、`pamvalidate`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamfix.html>。

- 修复缺少最后一部分的 Netpbm 文件：

`pamfix -truncate {{path/to/corrupted.ext}} > {{path/to/output.ext}}`

- 修复像素值超出图像 `maxval` 的 Netpbm 文件，通过降低这些像素的值：

`pamfix -clip {{path/to/corrupted.ext}} > {{path/to/output.ext}}`

- 修复像素值超出图像 `maxval` 的 Netpbm 文件，通过增加 `maxval`：

`pamfix -changemaxval {{path/to/corrupted.pam|pbm|pgm|ppm}} > {{path/to/output.pam|pbm|pgm|ppm}}`