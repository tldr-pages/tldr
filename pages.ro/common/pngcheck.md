# pngcheck

> Imprimați informații detaliate despre și verificați fișierele PNG, JNG și MNG.
> Mai multe informaţii: <http://www.libpng.org/pub/png/apps/pngcheck.html>

- Arată un rezumat pentru o imagine (lăţime, înălţime şi adâncime de culoare):

`pngcheck {{image.png}}`

- Arată informații pentru o imagine folosind o reprezentare în [c]ulori:

`pngcheck -c {{image.png}}`

- Arată informații cu [v]erbositate (detaliate) pentru o imagine:

`pngcheck -cvt {{image.png}}`

- Primiți o imagine de la stdin și afișați informații detaliate:

`cat {{path/to/image.png}} | pngcheck -cvt`

- [s] caută PNG-uri într-un anumit fișier și afișează informații despre ele:

`pngcheck -s {{image.png}}`

- Căutați PNG-uri într-un alt fișier și e[x]trage-le:

`pngcheck -x {{image.png}}`
