# podman բեռնում

> Բեռնել պատկեր oci-արխիվից կամ docker-արխիվից, որը ստեղծվել է `podman save`-ի միջոցով:.
> Տես նաև՝ `podman save`, `podman import`:.
> Լրացուցիչ տեղեկություններ. <https://docs.podman.io/en/latest/markdown/podman-load.1.html>:.

- Ներբեռնեք պատկեր `.tar` ֆայլից.:

`podman load {{[-i|--input]}} {{path/to/file.tar}}`

- Ներբեռնեք պատկեր սեղմված `.tar` ֆայլից.:

`podman load {{[-i|--input]}} {{path/to/file.tar[.gz|.bz2|.xz|.zst]}}`

- Ներբեռնեք պատկեր և ցուցադրեք հանգիստ արդյունքը (ցուցադրեք միայն պատկերի ID-ն):

`podman load {{[-q|--quiet]}} {{[-i|--input]}} {{path/to/file.tar}}`

- Բեռնել պատկեր `stdin`-ից:

`podman < {{path/to/file.tar}} load`
