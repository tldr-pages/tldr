# pasuspender

> Ideiglenesen felfüggeszti a `pulseaudio` címet, amíg egy másik parancs fut, hogy hozzáférést biztosítson az alsa-hoz. További információ: <https://manned.org/pasuspender>.

- A PulseAudio felfüggesztése a `jackd` futása közben:

`pasuspender -- {{jackd -d alsa --device hw:0}}`
