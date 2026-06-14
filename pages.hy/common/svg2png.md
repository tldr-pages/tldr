# svg2png

> Պատկերացրեք SVG պատկերը PNG պատկերին՝ օգտագործելով cairo:.
> Լրացուցիչ տեղեկություններ. <https://cairographics.org/>:.

- Փոխարկել SVG ֆայլը PNG:

`svg2png {{path/to/file.svg}} {{path/to/output.png}}`

- Փոխակերպեք SVG ֆայլը PNG-ի որոշակի լայնությամբ (պահպանելով կողմերի հարաբերակցությունը).:

`svg2png {{[-w|--width]}} {{800}} {{path/to/file.svg}} {{path/to/output.png}}`

- Փոխակերպեք SVG ֆայլը PNG-ի որոշակի բարձրությամբ (պահպանելով կողմերի հարաբերակցությունը).:

`svg2png {{[-h|--height]}} {{600}} {{path/to/file.svg}} {{path/to/output.png}}`

- Փոխարկեք SVG ֆայլը PNG ինչպես լայնությամբ, այնպես էլ բարձրությամբ (պատկերը կենտրոնացած է տարածության մեջ).:

`svg2png {{[-w|--width]}} {{800}} {{[-h|--height]}} {{600}} {{path/to/file.svg}} {{path/to/output.png}}`

- Փոխարկեք SVG ֆայլը PNG-ի, որը մասշտաբավորվում է գործակցով.:

`svg2png {{[-s|--scale]}} {{2.0}} {{path/to/file.svg}} {{path/to/output.png}}`

- Փոխակերպեք SVG-ն `stdin`-ից PNG `stdout`-ում:

`cat {{path/to/file.svg}} | svg2png - - > {{path/to/output.png}}`

- Շրջեք ելքային պատկերը հորիզոնական կամ ուղղահայաց.:

`svg2png --flipx {{path/to/file.svg}} {{path/to/output.png}}`
