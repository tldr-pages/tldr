# aplay

> Konsolowy odtwarzacz dźwięku dla drivera dźwiękowego ALSA.
> Więcej informacji: <https://manned.org/aplay>.

- Odtwórz określony plik (częstotliwość próbkowania, ilość bitów, itd. będą określone automatycznie na podstawie formatu):

`aplay {{ścieżka/do/pliku}}`

- Odtwórz pierwsze 10 sekund określonego pliku z częstotliwością 2500 Hz::

`aplay --duration={{10}} --rate={{2500}} {{ścieżka/do/pliku}}`

- Odtwórz surowy plik jako plik `.au` 22050 Hz, mono, 8-bit, Mu-Law:

`aplay --channels={{1}} --file-type {{raw}} --rate={{22050}} --format={{mu_law}} {{ścieżka/do/pliku}}`
