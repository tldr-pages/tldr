# Arduino

> Arduino Studio - Arduino 平台的集成开发环境。
> 更多信息：<https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>。

- 构建一个草图：

`arduino --verify {{path/to/file.ino}}`

- 构建并上传一个草图：

`arduino --upload {{path/to/file.ino}}`

- 将草图构建并上传到连接在端口 `/dev/ttyACM0` 的 Atmega328p CPU 的 Arduino Nano：

`arduino --board {{arduino:avr:nano:cpu=atmega328p}} --port {{/dev/ttyACM0}} --upload {{path/to/file.ino}}`

- 将偏好设置 `name` 设置为给定的 `value`：

`arduino --pref {{name}}={{value}}`

- 构建一个草图，将构建结果放在构建目录中，并重用该目录中的任何先前构建结果：

`arduino --pref build.path={{path/to/build_directory}} --verify {{path/to/file.ino}}`

- 将任何（更改的）偏好设置保存到 `preferences.txt`：

`arduino --save-prefs`

- 安装最新的 SAM 板：

`arduino --install-boards "{{arduino:sam}}"`

- 安装 Bridge 和 Servo 库：

`arduino --install-library "{{Bridge:1.0.0,Servo:1.2.0}}"`