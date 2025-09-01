# fonttools subset

> Generate subsets of fonts or optimize file sizes.
> More information: <https://fonttools.readthedocs.io/en/latest/subset/index.html>.

- Subset a TTF font file to the Basic Latin Unicode block:

`fonttools subset {{path/to/font.ttf}} --unicodes=U+0000-007F`

- Change the file type to WOFF2:

`fonttools subset {{path/to/font.ttf}} --unicodes=U+0000-007F --flavor=woff2`

- Keep only the onum (oldstyle figures) and kern (kerning) OpenType font features:

`fonttools subset {{path/to/font.ttf}} --unicodes=U+0000-007F --layout-features=onum,kern`

- Set the output file's name:

`fonttools subset {{path/to/font.ttf}} --unicodes=U+0000-007F --output-file={{path/to/subset.ttf}}`
