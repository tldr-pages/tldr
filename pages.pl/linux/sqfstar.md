# sqfstar

> Utwórz system plików squashfs z archiwum tar.
> Więcej informacji: <https://manned.org/sqfstar>.

- Utwórz system plików squashfs (domyślnie kompresując za pomocą `gzip`) z nieskompresowanego archiwum tar:

`sqfstar {{system_plików.squashfs}} < {{archiwum.tar}}`

- Utwórz system plików squashfs z archiwum tar skompresowanego za pomocą `gzip`, i skompresuj system plików używając podanego algorytmu:

`zcat {{archiwum.tar.gz}} | sqfstar -comp {{gzip|lzo|lz4|xz|zstd|lzma}} {{system_plików.squashfs}}`

- Utwórz system plików squashfs z archiwum tar skompresowanego za pomocą `xz`, pomijając niektóre pliki:

`xzcat {{archiwum.tar.xz}} | sqfstar {{system_plików.squashfs}} {{plik1 plik2 ...}}`

- Utwórz system plików squashfs z archiwum tar skompresowanego za pomocą `zstd`, pomijając pliki kończące się na `.gz`:

`zstdcat {{archiwum.tar.zst}} | sqfstar {{system_plików.squashfs}} "{{*.gz}}"`

- Utwórz system plików squashfs z archiwum tar skompresowanego za pomocą `lz4`, pomijając pliki pasujące do wyrażenia regularnego:

`lz4cat {{archiwum.tar.lz4}} | sqfstar {{system_plików.squashfs}} -regex "{{wyrażenie_regularne}}"`
