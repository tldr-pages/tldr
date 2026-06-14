# svgr

> Փոխակերպեք SVG-ները React բաղադրիչների:.
> Լրացուցիչ տեղեկություններ. <https://react-svgr.com/docs/options/>:.

- Փոխակերպեք SVG ֆայլը React բաղադրիչի՝ `stdout`-ի:

`svgr -- {{path/to/file.svg}}`

- Փոխակերպեք SVG ֆայլը React բաղադրիչի, օգտագործելով TypeScript-ը `stdout`:

`svgr --typescript -- {{path/to/file.svg}}`

- Փոխակերպեք SVG ֆայլը React բաղադրիչի, օգտագործելով JSX փոխակերպումը `stdout`:

`svgr --jsx-runtime automatic -- {{path/to/file.svg}}`

- Բոլոր SVG ֆայլերը գրացուցակից փոխակերպեք React բաղադրիչներին հատուկ գրացուցակի մեջ.:

`svgr --out-dir {{path/to/output_directory}} {{path/to/input_directory}}`

- Բոլոր SVG ֆայլերը գրացուցակից փոխակերպեք React բաղադրիչներին հատուկ գրացուցակի՝ բաց թողնելով արդեն փոխակերպված ֆայլերը.:

`svgr --out-dir {{path/to/output_directory}} --ignore-existing {{path/to/input_directory}}`

- Բոլոր SVG ֆայլերը գրացուցակից վերածեք React բաղադրիչների որոշակի գրացուցակի՝ օգտագործելով ֆայլերի անունների հատուկ պատյան.:

`svgr --out-dir {{path/to/output_directory}} --filename-case {{camel|kebab|pascal}} {{path/to/input_directory}}`

- Բոլոր SVG ֆայլերը գրացուցակից վերածեք React բաղադրիչների որոշակի գրացուցակի՝ առանց ինդեքսային ֆայլ ստեղծելու.:

`svgr --out-dir {{path/to/output_directory}} --no-index {{path/to/input_directory}}`
