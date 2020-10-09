# aplay

> Command-line sound recorder (arecord) and player (aplay) for ALSA soundcard driver.

- Play file "foobar". Sampling rate, bit depth, and so forth will be automatically determined for supported soundfile formats:

`aplay {{foobar}}`

- Play the raw file "foobar" as a 22050-Hz, mono, 8-bit, Mu-Law .au file:

`aplay -c 1 -t raw -r 22050 -f mu_law {{foobar}}`

- Record foobar.wav as a 10-second, CD-quality wave file, using the PCM "copy":

`arecord -d 10 -f cd -t wav -D copy {{foobar.wav}}`

- Record  from  the  default  audio  source  in monaural, 8,000 samples per second, 8 bits per sample:

`arecord -t wav --max-file-time 30 {{mon.wav}}`

- Record in stereo from the default audio source. Create a new file every hour with filename autoformat:

`arecord -f cd -t wav --max-file-time 3600 --use-strftime {{%Y/%m/%d/listen-%H-%M-%v.wav}}`
