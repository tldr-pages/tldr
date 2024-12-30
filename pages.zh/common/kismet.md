# kismet

> 一个无线网络和设备检测器、嗅探器、战斗驱动工具和无线入侵检测框架。
> 更多信息：<https://www.kismetwireless.net/>。

- 从特定无线接口捕获数据包：

`sudo kismet -c {{wlan0}}`

- 在无线接口上监控多个频道：

`sudo kismet -c {{wlan0,wlan1}} -m`

- 捕获数据包并将其保存到特定目录：

`sudo kismet -c {{wlan0}} -d {{path/to/output}}`

- 使用特定配置文件启动 Kismet：

`sudo kismet -c {{wlan0}} -f {{path/to/config.conf}}`

- 监控并将数据记录到 SQLite 数据库：

`sudo kismet -c {{wlan0}} --log-to-db`

- 使用特定数据源进行监控：

`sudo kismet -c {{wlan0}} --data-source={{rtl433}}`

- 启用特定事件的警报：

`sudo kismet -c {{wlan0}} --enable-alert={{new_ap}}`

- 显示特定 AP 数据包的详细信息：

`sudo kismet -c {{wlan0}} --info {{BSSID}}`