# pmset

> 配置 macOS 电源管理设置，就像在系统偏好设置 > 节能器中所做的那样。
> 修改设置的命令必须以 `sudo` 开头。
> 更多信息：<https://keith.github.io/xcode-man-pages/pmset.1.html>。

- 显示当前电源管理设置：

`pmset -g`

- 显示当前电源源和电池电量：

`pmset -g batt`

- 立即使显示器进入睡眠状态：

`pmset displaysleepnow`

- 设置在充电时显示器永不进入睡眠：

`sudo pmset -c displaysleep 0`

- 设置在电池供电时显示器在 15 分钟后进入睡眠：

`sudo pmset -b displaysleep 15`

- 安排计算机在每个工作日早上 9 点自动唤醒：

`sudo pmset repeat wake MTWRF 09:00:00`

- 恢复到系统默认设置：

`sudo pmset -a displaysleep 10 disksleep 10 sleep 30 womp 1`