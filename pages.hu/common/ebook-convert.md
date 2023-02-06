# ebook-convert

> Használható e-könyvek konvertálására a leggyakoribb formátumok között, pl. PDF, EPUB és MOBI. A Calibre e-könyvtár eszköz része. További információ: <https://manual.calibre-ebook.com/generated/en/ebook-convert.html>.

- Egy e-könyv átalakítása egy másik formátumba:

`ebook-convert {{path/to/input_file}} {{output_file}}`

- Markdown vagy HTML konvertálása e-könyvvé TOC, cím és szerző megjelölésével:

`ebook-convert {{path/to/input_file}} {{output_file}} --level1-toc="//h:h1" --level2-toc="//h:h2" --level3-toc="//h:h3" --title={{title}} --authors={{author}}`
