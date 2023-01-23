# transcode

> Videó- és hangkódok átkódolása, valamint médiaformátumok közötti konvertálás. További információ: <https://manned.org/transcode>.

- Stabilizációs fájl létrehozása, hogy képes legyen eltávolítani a kamera rázkódását:

`transcode -J stabilize -i {{input_file}}`

- A stabilizációs fájl létrehozása után távolítsa el a kamera rázkódását, alakítsa át a videót XviD segítségével:

`transcode -J transform -i {{input_file}} -y xvid -o {{output_file}}`

- Méretezze át a videót 640x480 pixelre, és konvertálja MPEG4 kodekbe az XviD segítségével:

`transcode -Z 640x480 -i {{input_file}} -y xvid -o {{output_file}}`
