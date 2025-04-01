# create_ap

> 创建一个接入点 (AP)，可以在任意信道上。
> 更多信息：<https://github.com/oblique/create_ap>.

- 创建一个无密码的开放网络：

`create_ap {{wlan0}} {{eth0}} {{access_point_ssid}}`

- 使用 WPA + WPA2 密码：

`create_ap {{wlan0}} {{eth0}} {{access_point_ssid}} {{passphrase}}`

- 创建一个不共享互联网的接入点：

`create_ap -n {{wlan0}} {{access_point_ssid}} {{passphrase}}`

- 创建一个桥接网络并共享互联网：

`create_ap -m bridge {{wlan0}} {{eth0}} {{access_point_ssid}} {{passphrase}}`

- 使用预配置的桥接接口创建一个桥接网络并共享互联网：

`create_ap -m bridge {{wlan0}} {{br0}} {{access_point_ssid}} {{passphrase}}`

- 从同一 Wi-Fi 接口创建一个用于互联网共享的接入点：

`create_ap {{wlan0}} {{wlan0}} {{access_point_ssid}} {{passphrase}}`

- 选择不同的 Wi-Fi 适配器驱动程序：

`create_ap --driver {{wifi_adapter}} {{wlan0}} {{eth0}} {{access_point_ssid}} {{passphrase}}`
