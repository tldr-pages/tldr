# podman արտահանում

> Արտահանեք կոնտեյների ֆայլային համակարգը և պահեք այն որպես tarball տեղական մեքենայի վրա:.
> Տես նաև՝ `podman import`, `podman save`:.
> Լրացուցիչ տեղեկություններ. <https://docs.podman.io/en/latest/markdown/podman-export.1.html>:.

- Արտահանել կոնտեյների ֆայլային համակարգը `.tar` ֆայլ՝:

`podman export {{[-o|--output]}} {{path/to/file.tar}} {{container_name_or_id}}`

- Արտահանել կոնտեյների ֆայլային համակարգը `stdout`:

`podman export {{container_name_or_id}} > {{path/to/file.tar}}`
