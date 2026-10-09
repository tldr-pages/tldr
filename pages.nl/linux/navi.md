# navi

> Een interactieve cheatsheet-tool voor de command-line en applicatielaunchers.
> Zie ook: `tldr`, `cheatshh`, `navi`.
> Meer informatie: <https://github.com/denisidoro/navi>.

- Blader door alle beschikbare cheatsheets:

`navi`

- Blader door de cheatsheet voor `navi` zelf:

`navi fn welcome`

- Print een commando uit de cheatsheet zonder het uit te voeren:

`navi --print`

- Geef de broncode van de shell-widget weer (dit detecteert automatisch je shell indien mogelijk, maar kan ook handmatig gespecificeerd worden):

`navi widget {{shell}}`

- Selecteer en voer automatisch het snippet uit dat het beste overeenkomt met een zoekopdracht:

`navi {{[-q|--query]}} '{{query}}' --best-match`
