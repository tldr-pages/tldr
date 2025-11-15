# feh

> 轻量级图像查看工具。
> 更多信息：<https://man.finalrewind.org/1/feh/>.

- 查看本地图像或使用 URL：

`feh {{路径/到/图像}}`

- 递归查看图像：

`feh --recursive {{路径/到/图像}}`

- 使用无边框窗口查看图像：

`feh --borderless {{路径/到/图像}}`

- 在浏览完最后一个图像之后退出：

`feh --cycle-once {{路径/到/图像}}`

- 设置幻灯片放映周期延迟时间（秒）：

`feh --slideshow-delay {{秒}} {{路径/到/图像}}`

- 设置墙纸（居中、填充、最大化、缩放或平铺）：

`feh --bg-{{center|fill|max|scale|tile}} {{路径/到/图像}}`

- 创建目录中所有图像的拼贴，并作为新图像输出：

`feh --montage --thumb-height {{150}} --thumb-width {{150}} --index-info "{{%nn%wx%h}}" --output {{路径/到/拼贴图像.png}}`
