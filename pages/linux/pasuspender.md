# pasuspender

> Temporarily suspends `pulseaudio` while another command is running to allow access to alsa.

- Suspend pulseaudio while running `jackd`:

`pasuspender -- {{jackd -d alsa --device hw:0}}`
