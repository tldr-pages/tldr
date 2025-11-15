# arduino

> Arduino Studio - 为 Arduino 平台准备的集成开发环境。
> 更多信息：<https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>.

- 构建一个草稿：

`arduino --verify {{路径/到/文件.ino}}`

- 构建草稿，并上传至设备：

`arduino --upload {{路径/到/文件.ino}}`

- 构建草稿，并上传至带有一个 Atmega328p CPU 的 Arduino Nano（连接到端口 `/dev/ttyACM0`）：

`arduino --board {{arduino:avr:nano:cpu=atmega328p}} --port {{/dev/ttyACM0}} --upload {{路径/到/文件.ino}}`

- 将首选项 `名称` 设定为特定 `值`：

`arduino --pref {{名称}}={{值}}`

- 构建草稿，将输出保存在输出文件夹，同时重复利用该文件夹中，在此之前已经输出的文件：

`arduino --pref build.path={{路径/到/输出_文件夹}} --verify {{路径/到/文件.ino}}`

- 保存任意（修改过的）首选项到 `preferences.txt`:

`arduino --save-prefs`

- 安装最新的 SAM 开发板：

`arduino --install-boards "{{arduino:sam}}"`

- 安装 Bridge 和 Servo 库：

`arduino --install-library "{{Bridge:1.0.0,Servo:1.2.0}}"`
