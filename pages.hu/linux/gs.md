# gs

> A GhostScript egy PDF- és PostScript-értelmező. További információ: <https://manned.org/gs>.

- Egy fájl megtekintése:

`gs -dQUIET -dBATCH {{file.pdf}}`

- A PDF-fájl méretének csökkentése 150 dpi-s képekre az e-könyves eszközön való olvasáshoz:

`gs -dNOPAUSE -dQUIET -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -sOutputFile={{output.pdf}} {{input.pdf}}`

- A PDF-fájl (1-3. oldal) átalakítása 150 dpi felbontású képpé:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=jpeg -r150 -dFirstPage={{1}} -dLastPage={{3}} -sOutputFile={{output_%d.jpg}} {{input.pdf}}`

- Oldalak kivonása PDF-fájlból:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={{output.pdf}} {{input.pdf}}`

- PDF-fájlok egyesítése:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={{output.pdf}} {{input1.pdf}} {{input2.pdf}}`

- PostScript fájlból PDF-fájlba konvertálás:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={{output.pdf}} {{input.ps}}`
