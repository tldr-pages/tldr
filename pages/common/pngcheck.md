# pngcheck

> Pngcheck verifies the integrity of PNG, JNG and MNG files (by checking the internal 32-bit CRCs, a.k.a. checksums, and decompressing the image data).
> It can optionally dump almost all of the chunk-level information in the image in human-readable form.
> More information: <http://www.libpng.org/pub/png/apps/pngcheck.html>.

- Print summary (width & height & color depth):

`pngcheck foo.png`

- Print colorized output:

`pngcheck -c foo.png`

- Print most chuck data (IHDR & PLTE & IDAT & etc):

`pngcheck -cvt foo.png`
