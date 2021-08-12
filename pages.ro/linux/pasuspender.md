# pasuspender

> Suspendează temporar `pulseaudio` în timp ce o altă comandă rulează pentru a permite accesul la alsa.

- Suspendați pulseaudio în timp ce rulați `jackd`:

`pasuspender -- {{jackd -d alsa --device hw:0}}`
