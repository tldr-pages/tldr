# pasuspender

> 다른 명령이 실행되는 동안 `pulseaudio`를 일시 중지하여 alsa에 접근할 수 있도록 합니다.
> 더 많은 정보: <https://manned.org/pasuspender>.

- `jackd`를 실행하는 동안 PulseAudio 일시 중지:

`pasuspender -- {{jackd -d alsa --device hw:0}}`
