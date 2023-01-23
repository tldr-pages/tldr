# chafa

> Képnyomtatás a terminálban Lásd még: `catimg`, `pixterm`. További információ: [https://hpjansson.org/chafa.](https://hpjansson.org/chafa)

- Egy kép közvetlenül a terminálban történő renderelése:

`chafa {{path/to/file}}`

- Kép renderelése 24 bites \[c\]olorral:

`chafa -c full {{path/to/file}}`

- Kis színpalettával rendelkező képek renderelésének javítása dithering használatával:

`chafa -c 16 --dither ordered {{path/to/file}}`

- Egy kép renderelése, pixeles megjelenítéssel:

`chafa --symbols vhalf {{path/to/file}}`

- Monokróm kép renderelése csak Braille-írással:

`chafa -c none --symbols braille {{path/to/file}}`
