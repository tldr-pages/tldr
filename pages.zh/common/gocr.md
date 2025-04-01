# gocr

> 光学字符识别工具。
> 使用其引擎识别字符，并提示用户输入未知模式以存储在数据库中。
> 更多信息：<https://manned.org/gocr.1>。

- 识别 [i]输入图像中的字符并 [o]输出到指定文件。将数据库 ([p]) 放在 `path/to/db_directory`（确认该文件夹存在，否则将跳过数据库使用）。[m]ode 130 表示创建 + 使用 + 扩展数据库：

`gocr -m 130 -p {{path/to/db_directory}} -i {{path/to/input_image.png}} -o {{path/to/output_file.txt}}`

- 识别字符并假设所有 [C]字符都是数字：

`gocr -m 130 -p {{path/to/db_directory}} -i {{path/to/input_image.png}} -o {{path/to/output_file.txt}} -C "{{0..9}}"`

- 以 100% 的确信度 [a]识别字符（字符有更高的几率被视为未知）：

`gocr -m 130 -p {{path/to/db_directory}} -i {{path/to/input_image.png}} -o {{path/to/output_file.txt}} -a 100`
