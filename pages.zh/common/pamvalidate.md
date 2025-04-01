# pamvalidate

> 验证 PAM、PGM、PBM 和 PPM 文件。
> 参见: `pamfile`, `pamfix`。
> 更多信息: <https://netpbm.sourceforge.net/doc/pamvalidate.html>。

- 如果 Netpbm 文件有效，则从 `stdin` 复制到 `stdout`；否则失败：

`{{command}} | pamvalidate > {{path/to/output.ext}}`