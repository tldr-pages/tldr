# magick compare

> 创建一个比较文件，可视化地标注出两个图片之间的差异。
> 另见：`magick`。
> 更多信息：<https://imagemagick.org/script/compare.php>.

- 比较两个图片：

`magick compare {{路径/到/图片1.png}} {{路径/到/图片2.png}} {{路径/到/比较图片.png}}`

- 使用特定的算法比较两个图片：

`magick compare -verbose -metric {{PSNR}} {{路径/到/图片1.png}} {{路径/到/图片2.png}} {{路径/到/比较图片.png}}`
