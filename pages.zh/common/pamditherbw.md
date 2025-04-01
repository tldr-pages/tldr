# pamditherbw

> 对灰度图像应用抖动，即将其转换为黑白像素模式，这些像素看起来与原始灰度图像相同。
> 另请参阅: `pbmreduce`。
> 更多信息: <https://netpbm.sourceforge.net/doc/pamditherbw.html>。

- 读取PGM图像，应用抖动并保存到文件:

`ppmditherbw {{path/to/image.pgm}} > {{path/to/file.pgm}}`

- 使用指定的量化方法:

`ppmditherbw -{{floyd|fs|atkinson|threshold|hilbert|...}} {{path/to/image.pgm}} > {{path/to/file.pgm}}`

- 使用atkinson量化方法和指定的伪随机数生成器种子:

`ppmditherbw -atkinson -randomseed {{1337}} {{path/to/image.pgm}} > {{path/to/file.pgm}}`

- 为执行某种阈值处理的量化方法指定阈值:

`ppmditherbw -{{fs|atkinson|thresholding}} -value {{0.3}} {{path/to/image.pgm}} > {{path/to/file.pgm}}`
