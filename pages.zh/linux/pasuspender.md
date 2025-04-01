# pasuspender

> 临时暂停 `pulseaudio`，以便另一个命令运行时访问 alsa。
> 更多信息：<https://manned.org/pasuspender>。

- 在运行 `jackd` 时暂停 PulseAudio：

`pasuspender -- {{jackd -d alsa --device hw:0}}`
