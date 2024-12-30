# gocr

> 光学字符识别工具。
> 利用其引擎识别字符，并提示用户输入未知模式以将其存储在数据库中。
> 更多信息：<https://manned.org/gocr.1>。

- 识别输入图像中的字符并将其输出到指定文件中。将数据库放在 `path/to/db_directory`（请验证文件夹是否存在，否则数据库使用将被静默跳过）。模式 130 意味着创建 + 使用 + 扩展数据库：

`gocr -m 130 -p {{path/to/db_directory}} -i {{path/to/input_image.png}} -o {{path/to/output_file.txt}}`

- 识别字符并假设所有字符都是数字：

`gocr -m 130 -p {{path/to/db_directory}} -i {{path/to/input_image.png}} -o {{path/to/output_file.txt}} -C "{{0..9}}"`

- 以 100% 的确定性识别字符（字符更有可能被视为未知）：

`gocr -m 130 -p {{path/to/db_directory}} -i {{path/to/input_image.png}} -o {{path/to/output_file.txt}} -a 100`