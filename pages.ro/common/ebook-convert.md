# ebook-convert

> Poate fi folosit pentru a converti cărți electronice între formate comune, de exemplu, pdf, epub și mobi.
> O parte a instrumentului de bibliotecă de cărți electronice Calibre.
> Mai multe informaţii: <https://manual.calibre-ebook.com/generated/en/ebook-convert.html>

- Conversia unei cărți electronice într-un alt format:

`ebook-convert {{source}} {{destination}}`

- Convertiți Markdown sau HTML în e-book cu TOC, titlu și autor:

`ebook-convert {{source}} {{destination}} --level1-toc="//h:h1" --level2-toc="//h:h2" --level3-toc="//h:h3" --title={{title}} --authors={{author}}`
