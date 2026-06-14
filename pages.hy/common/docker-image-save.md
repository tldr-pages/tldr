# docker պատկերի պահպանում

> Արտահանել Docker պատկերները արխիվ:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/image/save/>:.

- Պահպանեք պատկերը՝ վերահղելով `stdout` `.tar` արխիվը՝:

`docker {{[save|image save]}} {{image}}:{{tag}} > {{path/to/file.tar}}`

- Պահպանեք պատկերը `.tar` արխիվում.:

`docker {{[save|image save]}} {{[-o|--output]}} {{path/to/file.tar}} {{image}}:{{tag}}`

- Պահպանեք պատկերի բոլոր պիտակները.:

`docker {{[save|image save]}} {{[-o|--output]}} {{path/to/file.tar}} {{image_name}}`

- Cherry-ընտրեք պատկերի հատուկ պիտակները փրկելու համար.:

`docker {{[save|image save]}} {{[-o|--output]}} {{path/to/file.tar}} {{image_name:tag1 image_name:tag2 ...}}`
