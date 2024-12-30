# crackle

> 破解和解密蓝牙低能耗（BLE）加密。
> 更多信息：<https://github.com/mikeryan/crackle>。

- 检查记录的BLE通信是否包含恢复临时密钥（TK）所需的数据包：

`crackle -i {{path/to/input.pcap}}`

- 使用暴力破解恢复记录的配对事件的TK，并用它解密所有后续通信：

`crackle -i {{path/to/input.pcap}} -o {{path/to/decrypted.pcap}}`

- 使用指定的长期密钥（LTK）解密记录的通信：

`crackle -i {{path/to/input.pcap}} -o {{path/to/decrypted.pcap}} -l {{81b06facd90fe7a6e9bbd9cee59736a7}}`