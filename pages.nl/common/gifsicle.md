# gifsicle

> Maak, bewerk, manipuleer en verkrijg informatie over GIF-bestanden.
> Meer informatie: <https://www.lcdf.org/gifsicle/>.

- Optimaliseer een GIF als een nieuw bestand:

`gifsicle {{pad/naar/invoer.gif}} {{[-O|--optimize=]}}3 {{[-o|--output]}} {{pad/naar/uitvoer.gif}}`

- Gebruik batchmodus (wijzig elk opgegeven bestand direct) en de-optimaliseer een GIF:

`gifsicle {{[-b|--batch]}} {{pad/naar/invoer.gif}} {{[-U|--unoptimize]}}`

- Extraheer een frame uit een GIF:

`gifsicle {{pad/naar/invoer.gif}} '#{{0}}' > {{pad/naar/eerste_frame.gif}}`

- Maak een GIF-animatie van geselecteerde GIFs:

`gifsicle {{*.gif}} {{[-d|--delay]}} {{10}} {{[-l|--loop]}} > {{pad/naar/uitvoer.gif}}`

- Verklein de bestandsgrootte met behulp van lossy-compressie:

`gifsicle {{[-b|--batch]}} {{pad/naar/invoer.gif}} {{[-O|--optimize=]}}3 --lossy={{100}} {{[-k|--colors]}} {{16}} {{[-f|--dither]}}`

- Verwijder de eerste 10 frames en alle frames na frame 20 uit een GIF:

`gifsicle {{[-b|--batch]}} {{pad/naar/invoer.gif}} --delete '#{{0-9}}' '#{{20-}}'`

- Wijzig alle frames door ze bij te snijden tot een rechthoek, hun schaal te wijzigen, ze te spiegelen en te roteren:

`gifsicle {{[-b|--batch]}} --crop {{start_x}},{{start_y}}+{{rechthoek_breedte}}x{{rechthoek_hoogte}} --scale {{0.25}} --flip-horizontal --rotate-{{90|180|270}} {{pad/naar/invoer.gif}}`
