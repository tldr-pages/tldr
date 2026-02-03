# neo

> Simulate the digital rain from "The Matrix".
> More information: <https://github.com/st3w/neo>.

- Run the default digital rain:

`neo`

- Set scroll speed ([S]) and asynchronous columns ([a]):

`neo -S 12 -a`

- Change text color ([c]) and color mode:

`neo --color=green3 --colormode=256`

- Display a centered message ([m]):

`neo -m "Hello World"`

- Set droplet density ([d]) and glitch percentage ([G]):

`neo -d 2.0 --glitchpct=5.0`

- Use a specific charset (ASCII, Cyrillic, Greek, Katakana, Braille):

`neo --charset=ascii`  

- Disable glitching ([noglitch]) and colors ([colormode=0]) for performance:

`neo --noglitch --colormode=0`

- Show Unicode characters in a custom range ([chars]):

`neo --chars=0x1F030,0x1F093 --fullwidth`

- Key controls while running:

`SPACE`      - clear screen  
`UP`         - increase speed  
`DOWN`       - decrease speed  
`LEFT`       - decrease glitchiness  
`RIGHT`      - increase glitchiness  
`+`          - increase droplets  
`-`          - decrease droplets  
`ESC / q`  - quit
