# pdfposter

> Egy nagyméretű PDF-et több A4-es oldalra alakíthat át nyomtatáshoz. További információ: <https://pdfposter.readthedocs.io>.

- Egy A2 méretű poszter átalakítása 4 A4-es oldalra:

`pdfposter --poster-size a2 {{input_file.pdf}} {{output_file.pdf}}`

- Egy A4-es poszter méretezése A3-as méretre, majd 2 A4-es oldal létrehozása:

`pdfposter --scale 2 {{input_file.pdf}} {{output_file.pdf}}`
