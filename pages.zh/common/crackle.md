# crackle

> 破解和解密蓝牙低功耗 (BLE) 加密。
> 更多信息：<https://github.com/mikeryan/crackle>。

- 检查记录的 BLE 通信是否包含用于恢复临时密钥 (TKs) 所需的数据包：

`crackle -i {{path/to/input.pcap}}`

- 使用暴力破解方法恢复记录配对事件的临时密钥 (TK)，并使用该密钥解密所有后续通信：

`crackle -i {{path/to/input.pcap}} -o {{path/to/decrypted.pcap}}`

- 使用指定的长期密钥 (LTK) 解密记录的通信：

`crackle -i {{path/to/input.pcap}} -o {{path/to/decrypted.pcap}} -l {{81b06facd90fe7a6e9bbd9cee59736a7}}`