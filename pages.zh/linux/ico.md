# ico

> 显示多面体的动画。
> 更多信息：<https://manned.org/ico.1>.

- 显示每 0.1 秒变换位置的十二面体线框：

`ico -sleep {{0.1}}`

- 显示红色面的实心十二面体，背景为蓝色：

`ico -faces -noedges -colors {{red}} -bg {{blue}}`

- 显示大小为 100x100 的立方体线框，每帧移动 +1+2：

`ico -obj {{cube}} -size {{100x100}} -delta {{+1+2}}`

- 使用 5 个线程显示线宽为 10 的反向十二面体线框：

`ico -i -lw {{10}} -threads {{5}}`
