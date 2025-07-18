# magick compare

> 创建一个比较文件，可视化地标注出两个图片之间的差异。
> 另见：`magick`。
> 更多信息：<https://imagemagick.org/script/compare.php>.

- 比较两个图片：

`magick compare {{到/图片1/的路径.png}} {{到/图片2/的路径.png}} {{到/比较图片/的路径.png}}`

- 使用特定的算法比较两个图片：

`magick compare -verbose -metric {{PSNR}} {{到/图片1/的路径.png}} {{到/图片2/的路径.png}} {{到/比较图片/的路径.png}}`
