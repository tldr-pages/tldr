# pngcheck

> Imprimați informații detaliate despre și verificați fișierele PNG, JNG și MNG.
> Mai multe informaţii: <http://www.libpng.org/pub/png/apps/pngcheck.html>

- Imprimaţi un rezumat pentru o imagine (lăţime, înălţime şi adâncime de culoare):

`pngcheck {{image.png}}`

- Imprimare informații pentru o imagine cu [c] ieșire olorizată:

`pngcheck -c {{image.png}}`

- Print [v] informații erbose pentru o imagine:

`pngcheck -cvt {{image.png}}`

- Primiți o imagine de la stdin și afișați informații detaliate:

`cat {{path/to/image.png}} | pngcheck -cvt`

- [s] earch pentru PNG-uri într-un anumit fișier și afișează informații despre ele:

`pngcheck -s {{image.png}}`

- Căutați PNG-uri într-un alt fișier și e [x] le traduce:

`pngcheck -x {{image.png}}`
