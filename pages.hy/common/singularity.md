#եզակիություն

> Կառավարեք Singularity բեռնարկղերը և պատկերները:.
> Լրացուցիչ տեղեկություններ. <https://singularity-docs.readthedocs.io/en/latest/#commands>:.

- Ներբեռնեք հեռավոր պատկեր Sylabs Cloud-ից.:

`singularity pull --name {{image.sif}} {{library://godlovedc/funny/lolcow:latest}}`

- Վերակառուցեք հեռավոր պատկեր՝ օգտագործելով Singularity պատկերի վերջին ձևաչափը.:

`singularity build {{image.sif}} {{docker://godlovedc/lolcow}}`

- Սկսեք կոնտեյներ պատկերից և ստացեք դրա ներսում պատյան.:

`singularity shell {{image.sif}}`

- Սկսեք կոնտեյներ պատկերից և գործարկեք հրաման.:

`singularity exec {{image.sif}} {{command}}`

- Սկսեք կոնտեյներ պատկերից և գործարկեք ներքին տեքստը.:

`singularity run {{image.sif}}`

- Ստեղծեք եզակիության պատկեր բաղադրատոմսի ֆայլից.:

`sudo singularity build {{image.sif}} {{recipe}}`
