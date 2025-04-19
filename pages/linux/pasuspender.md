# pasuspender

> Temporarily suspends `pulseaudio` while another command is running to allow access to alsa.
> More information: <https://manned.org/pasuspender>.

- Suspend PulseAudio while running `jackd`:

`pasuspender -- {{jackd {{[-d|--driver]}} alsa {{[-d|--device]}} hw:0}}`
