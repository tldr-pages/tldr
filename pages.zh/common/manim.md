# manim

> 用于制作数学动画的视频引擎。
> 更多信息：<https://docs.manim.community/en/stable/tutorials/quickstart.html>.

- 使用默认设置渲染 Python 脚本中的场景：

`manim {{路径/文件.py}} {{场景名称}}`

- 实时预览渲染（渲染后自动打开视频）：

`manim {{[-pql|--preview --quality low]}} {{路径/文件.py}} {{场景名称}}`

- 以高质量渲染（1080p 60帧）：

`manim {{[-pqh|--preview --quality high]}} {{路径/文件.py}} {{场景名称}}`

- 指定自定义输出文件名：

`manim {{[-o|--output_file]}} {{输出文件名}} {{路径/文件.py}} {{场景名称}}`

- 使用指定分辨率和帧率进行渲染：

`manim {{[-r|--resolution]}} {{1920,1080}} {{[-f|--fps]}} {{60}} {{路径/文件.py}} {{场景名称}}`

- 列出文件中可用的场景而不进行渲染：

`manim --list_scenes {{路径/文件.py}}`

- 显示帮助信息：

`manim --help`
