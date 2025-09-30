# llvd

> Descarga videos del sistema de aprendizaje de Linkedin.
> Más información: <https://github.com/knowbee/llvd>.

- Descarga un [c]urso utilizando la autenticación basada en cookies:

`llvd -c {{nombre-de-curso}} --cookies`

- Descarga un curso en una [r]esolución específica:

`llvd -c {{nombre-de-curso}} -r 720`

- Descarga un curso con subtítulos:

`llvd -c {{nombre-de-curso}} --caption`

- Descarga un [p]lan de curso con espera entre 10 y 30 segundos:

`llvd -p {{nombre-de-plan}} -t {{10,30}} --cookies`
