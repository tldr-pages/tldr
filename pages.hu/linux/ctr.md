# ctr

> A `containerd` konténerek és képek kezelése. További információ: <https://containerd.io>.

- Az összes (futó és leállított) konténer listázása:

`ctr containers list`

- Az összes kép listázása:

`ctr images list`

- Egy kép kihúzása:

`ctr images pull {{image}}`

- Kép megjelölése:

`ctr images tag {{source_image}}:{{source_tag}} {{target_image}}:{{target_tag}}`
