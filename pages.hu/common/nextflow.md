# nextflow

> Eszköz számítási csővezetékek futtatásához. Leginkább bioinformatikai munkafolyamatokhoz használják. További információ: <https://www.nextflow.io>.

- Futtasson egy csővezetéket, használja a korábbi futtatások gyorsítótárazott eredményeit:

`nextflow run {{main.nf}} -resume`

- Egy távoli munkafolyamat egy adott kiadásának futtatása a GitHubról:

`nextflow run {{user/repo}} -revision {{release_tag}}`

- Futtatás egy adott munkakönyvtárral a közbenső fájlok számára, végrehajtási jelentés mentése:

`nextflow run {{workflow}} -work-dir {{path/to/directory}} -with-report {{report.html}}`

- Korábbi futtatások részleteinek megjelenítése az aktuális könyvtárban:

`nextflow log`

- A gyorsítótár és a közbenső fájlok eltávolítása egy adott futtatáshoz:

`nextflow clean -force {{run_name}}`

- Az összes letöltött projekt listázása:

`nextflow list`

- Egy távoli munkafolyamat legújabb verziójának lehívása a Bitbucketről:

`nextflow pull {{user/repo}} -hub bitbucket`

- Nextflow frissítése:

`nextflow self-update`
