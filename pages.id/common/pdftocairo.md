# pdftocairo

> Konversi berkas PDF ke PNG/JPEG/TIFF/PDF/PS/EPS/SVG menggunakan cairo.
> Informasi lebih lanjut: <https://manned.org/pdftocairo>.

- Konversi sebuah berkas PDF ke JPEG:

`pdftocairo {{jalan/ke/berkas.pdf}} -jpeg`

- Konversi ke PDF dengan memperluas keluaran hingga memenuhi kertas:

`pdftocairo {{jalan/ke/berkas.pdf}} {{keluaran.pdf}} -pdf -expand`

- Konversi ke SVG dengan menentukan halaman pertama/terakhir yang akan dikonversi:

`pdftocairo {{jalan/ke/berkas.pdf}} {{keluaran.svg}} -svg -f {{halaman_pertama}} -l {{halaman_terakhir}}`

- Konversi ke PNG dengan resolusi 200ppi:

`pdftocairo {{jalan/ke/berkas.pdf}} {{keluaran.png}} -png -r 200`

- Konversi ke TIFF skala abu-abu (grayscale) dengan mengatur ukuran kertas ke A3:

`pdftocairo {{jalan/ke/berkas.pdf}} -tiff -gray -paper A3`

- Konversi ke PNG dengan memotong (crop) piksel x dan y dari pojok kiri atas:

`pdftocairo {{jalan/ke/berkas.pdf}} -png -x {{piksel_x}} -y {{piksel_y}}`
