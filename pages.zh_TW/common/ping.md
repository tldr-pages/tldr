# ping

> 向網路主機發送 ICMP ECHO_REQUEST 封包。
> 更多資訊：<https://manned.org/ping>.

- Ping 主機：

`ping {{主機}}`

- 對主機執行特定次數的 ping 操作：

`ping -c {{次數}} {{主機}}`

- Ping 主機，指定發送間隔（以秒為單位）（預設為 1 秒）：

`ping -i {{秒數}} {{主機}}`

- Ping 主機，只以數字形式輸出，不嘗試查找名稱：

`ping -n {{主機}}`

- Ping 主機並在收到封包時響鈴（如果您的終端支援）：

`ping -a {{主機}}`

- 如果未收到回應，也會顯示訊息：

`ping -O {{host}}`
