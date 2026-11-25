# pasuspender

> تعلیق موقت `pulseaudio` در حین اجرای دستوری دیگر برای دسترسی به alsa.
> اطلاعات بیشتر: <https://manned.org/pasuspender>.

- تعلیق PulseAudio هنگام اجرای `jackd`:

`pasuspender -- {{jackd --driver alsa --device hw:0}}`
