# էլեկտրոնային գրքերի փոխակերպում

> Կարող է օգտագործվել էլեկտրոնային գրքերը սովորական ձևաչափերի միջև փոխակերպելու համար, օրինակ. PDF, EPUB և MOBI:.
> Caliber էլեկտրոնային գրքերի գրադարանի գործիքի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://manual.calibre-ebook.com/generated/en/ebook-convert.html>:.

- Էլեկտրոնային գիրքը փոխակերպեք այլ ձևաչափի.:

`ebook-convert {{path/to/input_file}} {{output_file}}`

- Փոխակերպեք Markdown-ը կամ HTML-ը էլեկտրոնային գրքի՝ TOC-ով, վերնագրով և հեղինակով.:

`ebook-convert {{path/to/input_file}} {{output_file}} --level1-toc="//h:h1" --level2-toc="//h:h2" --level3-toc="//h:h3" --title={{title}} --authors={{author}}`
