# ebook-convert

> Kann verwendet werden, um E-Books zu geläufigen Dateiformaten umzuwandeln, z.B. PDF, EPUB und MOBI.
> Teil der Calibre e-book library.
> Weitere Informationen: <https://manual.calibre-ebook.com/generated/en/ebook-convert.html>.

- Konvertiere ein E-Book in ein anderes Format:

`ebook-convert {{pfad/zu/input_datei}} {{pfad/zu/output_datei}}`

- Konvertiere eine Markdown- oder HTML Datei zu einem E-Book inklusive Inhaltsverzeichnis, Titel und Autoren:

`ebook-convert {{pfad/zu/input_datei}} {{pfad/zu/output_datei}} --level1-toc="//h:h1" --level2-toc="//h:h2" --level3-toc="//h:h3" --title={{titel}} --authors={{autor}}`
