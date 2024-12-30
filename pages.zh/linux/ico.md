# ico

> 显示一个多面体的动画。
> 更多信息：<https://manned.org/ico.1>。

- 显示一个每0.1秒改变位置的五角二十面体的线框图：

`ico -sleep {{0.1}}`

- 在蓝色背景上显示一个红色面体的实心五角二十面体：

`ico -faces -noedges -colors {{red}} -bg {{blue}}`

- 显示一个大小为100x100的立方体的线框图，该立方体每帧移动+1+2：

`ico -obj {{cube}} -size {{100x100}} -delta {{+1+2}}`

- 使用5个线程显示一个线宽为10的五角二十面体的反向线框图：

`ico -i -lw {{10}} -threads {{5}}`