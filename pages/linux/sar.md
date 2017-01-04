# sar

> 查询linux历史负载.

- 查询一段时间网络流量:

`sar -n DEV -s 15:00:00 -e 18:00:00 -f /var/log/sa/sa03 | grep "eth1"

