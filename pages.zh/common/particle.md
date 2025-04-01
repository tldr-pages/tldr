# particle

> 与 Particle 设备交互。
> 更多信息：<https://docs.particle.io/tutorials/developer-tools/cli>.

- 登录或为 Particle CLI 创建账户：

`particle setup`

- 显示设备列表：

`particle list`

- 交互式创建新的 Particle 项目：

`particle project create`

- 编译 Particle 项目：

`particle compile {{device_type}} {{path/to/source_code.ino}}`

- 远程更新设备以使用特定应用：

`particle flash {{device_name}} {{path/to/program.bin}}`

- 通过串行端口更新设备以使用最新固件：

`particle flash --serial {{path/to/firmware.bin}}`

- 在设备上执行函数：

`particle call {{device_name}} {{function_name}} {{function_arguments}}`
