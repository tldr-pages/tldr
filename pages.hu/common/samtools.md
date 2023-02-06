# samtools

> Nagy áteresztőképességű szekvenálási (genomikai) adatok kezelésére szolgáló eszközök. SAM/BAM/CRAM/CRAM formátumú adatok olvasására/írására/szerkesztésére/indexelésére/megjelenítésére szolgál. További információ: <https://www.htslib.org>.

- SAM bemeneti fájl átalakítása BAM folyamattá és mentése fájlba:

`samtools view -S -b {{input.sam}} > {{output.bam}}`

- A `stdin` (-) bemenetét veszi, és a SAM fejlécet és az egy adott régiót átfedő olvasatokat a `stdout` címre nyomtatja ki:

`{{other_command}} | samtools view -h - chromosome:start-end`

- Rendezze a fájlt és mentse BAM-ba (a kimeneti formátumot automatikusan meghatározza a kimeneti fájl kiterjesztése):

`samtools sort {{input}} -o {{output.bam}}`

- A rendezett BAM-fájl indexelése (létrehozza a {{sorted_input.bam.bam.bai}} fájlt):

`samtools index {{sorted_input.bam}}`

- Igazítási statisztikák nyomtatása egy fájlról:

`samtools flagstat {{sorted_input}}`

- Az egyes indexekhez (kromoszóma / kontig) tartozó igazítások számolása:

`samtools idxstats {{sorted_indexed_input}}`

- Több fájl egyesítése:

`samtools merge {{output}} {{input1 input2 …}}`

- A bemeneti fájl felosztása olvasási csoportok szerint:

`samtools split {{merged_input}}`
