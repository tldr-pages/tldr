# inkscape

> SVG (Scalable Vector Graphics) խմբագրման ծրագիր:.
> Inkscape-ի մինչև 0.92.x տարբերակների համար օգտագործեք -e-ի փոխարեն:.
> Լրացուցիչ տեղեկություններ. <https://inkscape.org/doc/inkscape-man.html>:.

- Բացեք SVG ֆայլ Inkscape GUI-ում.:

`inkscape {{path/to/file.svg}}`

- Արտահանեք SVG ֆայլը bitmap-ի մեջ լռելյայն ձևաչափով (PNG) և լռելյայն լուծաչափով (96 DPI):

`inkscape {{path/to/file.svg}} {{[-o|--export-filename]}} {{path/to/file.png}}`

- Արտահանել SVG ֆայլը 600x400 պիքսել բիթքարտեզի մեջ (կարող է առաջանալ կողմերի հարաբերակցության աղավաղում).:

`inkscape {{path/to/file.svg}} {{[-o|--export-filename]}} {{path/to/file.png}} {{[-w|--export-width]}} 600 {{[-h|--export-height]}} 400`

- Արտահանել SVG ֆայլի գծագիրը (բոլոր օբյեկտների սահմանային տուփը) բիթքարտեզի մեջ.:

`inkscape {{path/to/file.svg}} {{[-o|--export-filename]}} {{path/to/file.png}} {{[-D|--export-area-drawing]}}`

- Արտահանել մեկ օբյեկտ, հաշվի առնելով դրա ID-ն, բիթքարտեզ.:

`inkscape {{path/to/file.svg}} {{[-i|--export-id]}} {{id}} {{[-o|--export-filename]}} {{object.png}}`

- Արտահանեք SVG փաստաթուղթը PDF՝ բոլոր տեքստերը փոխակերպելով ուղիների.:

`inkscape {{path/to/file.svg}} {{[-o|--export-filename]}} {{path/to/file.pdf}} {{[-T|--export-text-to-path]}}`

- Կրկնօրինակեք օբյեկտը id="path123-ով", պտտեք կրկնօրինակը 90 աստիճանով, պահպանեք ֆայլը և դուրս եկեք Inkscape-ից:

`inkscape {{path/to/file.svg}} --select=path123 --verb="{{EditDuplicate;ObjectRotate90;FileSave;FileQuit}}"`
