# astroterm

> 一个基于终端的星图。
> 更多信息：<https://github.com/da-luce/astroterm#usage>.

- 根据你当前的位置显示恒星和行星的实时位置：

`astroterm`

- 显示星座、使用颜色，并以指定的帧率渲染模拟：

`astroterm {{[-C|--constellations]}} {{[-c|--color]}} {{[-f|--fps]}} {{60}}`

- 使用 Unicode 字符代替基本的 ASCII 字符，并且只渲染亮度高于指定星等的恒星：

`astroterm {{[-u|--unicode]}} {{[-t|--threshold]}} {{2.0}}`

- 使用指定的纬度、经度和日期时间：

`astroterm {{[-a|--latitude]}} {{90.0}} {{[-o|--longitude]}} {{-180.0}} {{[-d|--datetime]}} {{2025-08-04T12:00:00}}`

- 使用指定城市的经纬度，并将模拟速度设置为给定的倍数：

`astroterm {{[-i|--city]}} {{Singapore}} {{[-s|--speed]}} {{1000.0}}`
