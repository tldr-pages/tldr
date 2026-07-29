# astroterm

> 基于终端的星图。
> 更多信息：<https://github.com/da-luce/astroterm#usage>。

- 根据您当前位置显示恒星和行星的实时位置：

`astroterm`

- 显示星座、使用颜色，并以给定帧率渲染模拟：

`astroterm {{[-C|--constellations]}} {{[-c|--color]}} {{[-f|--fps]}} {{60}}`

- 使用 unicode 字符而不是基本 ASCII 字符，并且只渲染比给定星等更亮的恒星：

`astroterm {{[-u|--unicode]}} {{[-t|--threshold]}} {{2.0}}`

- 使用给定的纬度、经度和日期时间：

`astroterm {{[-a|--latitude]}} {{90.0}} {{[-o|--longitude]}} {{-180.0}} {{[-d|--datetime]}} {{2025-08-04T12:00:00}}`

- 使用给定城市的经纬度，并将模拟速度设置为给定因子：

`astroterm {{[-i|--city]}} {{Singapore}} {{[-s|--speed]}} {{1000.0}}`
