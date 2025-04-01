# arduino

> Arduino Studio - Arduino 平台的集成开发环境。
> 更多信息：<https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>。

- 编译一个草图：

`arduino --verify {{path/to/file.ino}}`

- 编译并上传一个草图：

`arduino --upload {{path/to/file.ino}}`

- 编译并上传一个草图到连接在 `/dev/ttyACM0` 端口的带有 Atmega328p CPU 的 Arduino Nano：

`arduino --board {{arduino:avr:nano:cpu=atmega328p}} --port {{/dev/ttyACM0}} --upload {{path/to/file.ino}}`

- 将偏好设置 `name` 设置为指定的 `value`：

`arduino --pref {{name}}={{value}}`

- 编译一个草图，将编译结果放入构建目录，并在该目录中重用任何先前的构建结果：

`arduino --pref build.path={{path/to/build_directory}} --verify {{path/to/file.ino}}`

- 将任何（已更改的）偏好设置保存到 `preferences.txt`：

`arduino --save-prefs`

- 安装最新的 SAM 开发板：

`arduino --install-boards "{{arduino:sam}}"`

- 安装 Bridge 和 Servo 库：

`arduino --install-library "{{Bridge:1.0.0,Servo:1.2.0}}"`