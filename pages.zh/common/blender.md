# blender

> 命令行接口，用于 Blender 3D 计算机图形应用程序。
> 参数按给定的顺序执行。
> 更多信息：<https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html>.

- 在后台渲染动画的所有帧，不加载用户界面（输出保存到 `/tmp`）：

`blender {{[-b|--background]}} {{path/to/file.blend}} {{[-a|--render-anim]}}`

- 使用特定的图像命名模式，在与 .blend 文件相对的路径中渲染动画：

`blender {{[-b|--background]}} {{path/to/file.blend}} {{[-o|--render-output]}} //{{render/frame_###.png}} {{[-a|--render-anim]}}`

- 渲染动画的第 10 帧为单个图像，保存到现有目录（绝对路径）：

`blender {{[-b|--background]}} {{path/to/file.blend}} {{[-o|--render-output]}} {{/path/to/output_directory}} {{[-f|--render-frame]}} {{10}}`

- 渲染动画的倒数第二帧为 JPEG 图像，保存到现有目录（相对路径）：

`blender {{[-b|--background]}} {{path/to/file.blend}} {{[-o|--render-output]}} //{{output_directory}} {{[-f|--render-frame]}} {{JPEG}} {{[-f|--render-frame]}} {{-2}}`

- 渲染特定场景的动画，从第 10 帧开始至第 500 帧结束：

`blender {{[-b|--background]}} {{path/to/file.blend}} {{[-S|--scene]}} {{scene_name}} {{[-s|--frame-start]}} {{10}} {{[-e|--frame-end]}} {{500}} {{[-a|--render-anim]}}`

- 通过传递 Python 表达式以特定分辨率渲染动画：

`blender {{[-b|--background]}} {{path/to/file.blend}} --python-expr '{{import bpy; bpy.data.scenes[0].render.resolution_percentage = 25}}' {{[-a|--render-anim]}}`

- 以 Python 控制台启动交互式 Blender 会话（启动后执行 `import bpy`）：

`blender {{[-b|--background]}} --python-console`