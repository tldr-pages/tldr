# Particle

> 与 Particle 设备进行交互。
> 更多信息：<https://docs.particle.io/tutorials/developer-tools/cli>。

- 登录或创建一个 Particle CLI 账户：

`particle setup`

- 显示设备列表：

`particle list`

- 交互式创建一个新的 Particle 项目：

`particle project create`

- 编译一个 Particle 项目：

`particle compile {{device_type}} {{path/to/source_code.ino}}`

- 远程更新设备以使用特定应用：

`particle flash {{device_name}} {{path/to/program.bin}}`

- 通过串行更新设备以使用最新固件：

`particle flash --serial {{path/to/firmware.bin}}`

- 在设备上执行一个函数：

`particle call {{device_name}} {{function_name}} {{function_arguments}}`