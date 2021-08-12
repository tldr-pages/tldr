# compare

> Vizualizaţi diferenţa dintre 2 imagini.
> Mai multe informaţii: <https://imagemagick.org/script/compare.php>

- Comparați 2 imagini:

`compare {{image1.png}} {{image2.png}} {{diff.png}}`

- Comparați 2 imagini folosind o valoare personalizată:

`compare -verbose -metric {{PSNR}} {{image1.png}} {{image2.png}} {{diff.png}}`
