# Blender

> Blender 3D计算机图形应用程序的命令行界面。
> 参数按给定顺序执行。
> 更多信息：<https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html>。

- 在后台渲染动画的所有帧，不加载用户界面（输出保存到`/tmp`）：

`blender --background {{path/to/file.blend}} --render-anim`

- 使用特定的图像命名模式渲染动画，路径相对于.blend文件（`//`）：

`blender --background {{path/to/file.blend}} --render-output //{{render/frame_###.png}} --render-anim`

- 将动画的第十帧渲染为单个图像，保存到现有目录（绝对路径）：

`blender --background {{path/to/file.blend}} --render-output {{/path/to/output_directory}} --render-frame {{10}}`

- 将动画的倒数第二帧渲染为JPEG图像，保存到现有目录（相对路径）：

`blender --background {{path/to/file.blend}} --render-output //{{output_directory}} --render-frame {{JPEG}} --render-frame {{-2}}`

- 渲染特定场景的动画，从第10帧开始到第500帧结束：

`blender --background {{path/to/file.blend}} --scene {{scene_name}} --frame-start {{10}} --frame-end {{500}} --render-anim`

- 以特定分辨率渲染动画，通过传递Python表达式：

`blender --background {{path/to/file.blend}} --python-expr '{{import bpy; bpy.data.scenes[0].render.resolution_percentage = 25}}' --render-anim`

- 在终端中启动交互式Blender会话，并打开Python控制台（启动后执行`import bpy`）：

`blender --background --python-console`