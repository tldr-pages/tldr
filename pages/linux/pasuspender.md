# pasuspender

> Temporarily suspends `pulseaudio` while another command is running to allow access to alsa.
> More information: <https://manned.org/pasuspender>.

- Suspend PulseAudio while running `jackd`:

`pasuspender -- {{jackd -d alsa --device hw:0}}`
