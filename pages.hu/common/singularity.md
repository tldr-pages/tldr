# singularity

> Singularity konténerek és képek kezelése. További információ: <https://singularity-docs.readthedocs.io/en/latest/#commands>.

- Távoli kép letöltése a Sylabs Cloudból:

`singularity pull --name {{image.sif}} {{library://godlovedc/funny/lolcow:latest}}`

- Távoli lemezkép újrakészítése a legújabb Singularity lemezképformátummal:

`singularity build {{image.sif}} {{docker://godlovedc/lolcow}}`

- Indítson el egy konténert egy image-ről, és kapjon benne egy héjat:

`singularity shell {{image.sif}}`

- Konténer indítása egy image-ből és egy parancs futtatása:

`singularity exec {{image.sif}} {{command}}`

- Konténer indítása egy image-ből és a belső futtatószkript végrehajtása:

`singularity run {{image.sif}}`

- Singularity image építése egy receptfájlból:

`sudo singularity build {{image.sif}} {{recipe}}`
