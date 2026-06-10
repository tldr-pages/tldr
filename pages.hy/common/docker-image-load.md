# docker պատկերի բեռնում

> Բեռնել Docker պատկերները ֆայլերից կամ `stdin`:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/image/load/>:.

- Ներբեռնեք Docker պատկերը `stdin`-ից:

`docker < {{path/to/image_file.tar}} {{[load|image load]}}`

- Բեռնել Docker պատկերը որոշակի ֆայլից.:

`docker {{[load|image load]}} {{[-i|--input]}} {{path/to/image_file.tar}}`

- Բեռնել Docker պատկերը կոնկրետ ֆայլից հանգիստ ռեժիմով.:

`docker {{[load|image load]}} {{[-q|--quiet]}} {{[-i|--input]}} {{path/to/image_file.tar}}`
