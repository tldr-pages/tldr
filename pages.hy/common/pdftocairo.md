# pdftocairo

> Փոխարկեք PDF ֆայլերը PNG/JPEG/TIFF/PDF/PS/EPS/SVG՝ օգտագործելով Կահիրե:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/pdftocairo>:.

- Փոխարկել PDF ֆայլը JPEG:

`pdftocairo {{path/to/file.pdf}} -jpeg`

- Փոխակերպեք PDF-ի՝ ընդլայնելով ելքը՝ թուղթը լրացնելու համար.:

`pdftocairo {{path/to/file.pdf}} {{output.pdf}} -pdf -expand`

- Փոխակերպեք SVG-ին՝ նշելով փոխարկելու առաջին/վերջին էջը.:

`pdftocairo {{path/to/file.pdf}} {{output.svg}} -svg -f {{first_page}} -l {{last_page}}`

- Փոխարկել PNG-ի 200ppi լուծաչափով.:

`pdftocairo {{path/to/file.pdf}} {{output.png}} -png -r 200`

- Փոխարկել մոխրագույնի TIFF կարգավորող թղթի չափը A3-ի:

`pdftocairo {{path/to/file.pdf}} -tiff -gray -paper A3`

- Վերևի ձախ անկյունից վերափոխեք x և y պիքսելների կրճատման PNG.:

`pdftocairo {{path/to/file.pdf}} -png -x {{x_pixels}} -y {{y_pixels}}`
