# amixer

> ALSA声卡驱动的混音器。
> 更多信息：<https://manned.org/amixer>。

- 将主音量提高10%：

`amixer -D pulse sset Master {{10%+}}`

- 将主音量降低10%：

`amixer -D pulse sset Master {{10%-}}`