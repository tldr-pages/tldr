# amixer

> ALSA 声卡驱动程序的混合器。
> 更多信息：<https://manned.org/amixer>.

- 增加 10% 的主音量：

`amixer -D pulse sset Master {{10%+}}`

- 降低 10% 的主音量：

`amixer -D pulse sset Master {{10%-}}`
