# snyk

> Keresse meg a sebezhetőségeket a kódjában, és orvosolja a kockázatokat. További információ [: https://snyk.io](https://snyk.io).

- Jelentkezzen be a Snyk-fiókjába:

`snyk auth`

- Tesztelje kódját az ismert sebezhetőségek szempontjából:

`snyk test`

- Teszteljen egy helyi Docker-képet az ismert sebezhetőségekre:

`snyk test --docker {{docker_image}}`

- Rögzítse a függőségek állapotát és az esetleges sebezhetőségeket a snyk.io oldalon:

`snyk monitor`

- Automatikus javítás és a sebezhetőségek figyelmen kívül hagyása:

`snyk wizard`
