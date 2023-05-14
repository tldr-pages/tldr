# mksquashfs

> Utwórz lub dodaj pliki i katalogi do systemów plików squashfs.
> Więcej informacji: <https://manned.org/mksquashfs>.

- Utwórz lub dodaj pliki i katalogi do systemu plików squashfs (domyślnie kompresując za pomocą `gzip`):

`mksquashfs {{ścieżka/do/pliku_lub_katalogu1 ścieżka/do/pliku_lub_katalogu2 ...}} {{system_plików.squashfs}}`

- Utwórz lub dodaj pliki i katalogi do systemu plików squashfs, używając podanego algorytmu kompresji ([comp]ression):

`mksquashfs {{ścieżka/do/pliku_lub_katalogu1 ścieżka/do/pliku_lub_katalogu2 ...}} {{system_plików.squashfs}} -comp {{gzip|lzo|lz4|xz|zstd|lzma}}`

- Utwórz lub dodaj pliki i katalogi do systemu plików squashfs, pomijając ([e]xcluding) niektóre z nich:

`mksquashfs {{ścieżka/do/pliku_lub_katalogu1 ścieżka/do/pliku_lub_katalogu2 ...}} {{system_plików.squashfs}} -e {{plik|katalog1 plik|katalog2 ...}}`

- Utwórz lub dodaj pliki i katalogi do systemu plików squashfs, pomijając ([e]xcluding) te kończące się na `.gz`:

`mksquashfs {{ścieżka/do/pliku_lub_katalogu1 ścieżka/do/pliku_lub_katalogu2 ...}} {{system_plików.squashfs}} -wildcards -e "{{*.gz}}"`

- Utwórz lub dodaj pliki i katalogi do systemu plików squashfs, pomijając ([e]xcluding) te pasujące do wyrażenia regularnego:

`mksquashfs {{ścieżka/do/pliku_lub_katalogu1 ścieżka/do/pliku_lub_katalogu2 ...}} {{system_plików.squashfs}} -regex -e "{{wyrażenie_regularne}}"`
