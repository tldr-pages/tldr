# podman մուտք

> Մուտք գործեք կոնտեյների ռեեստր:.
> Նշում. Linux-ում վավերագրման ֆայլի կանխադրված ուղին `$XDG_RUNTIME_DIR/containers/auth.json` է, որը սովորաբար պահվում է `tmpfs`-ում (RAM-ում):.
> Լրացուցիչ տեղեկություններ. <https://docs.podman.io/en/latest/markdown/podman-login.1.html>:.

- Մուտք գործեք գրանցամատյան (ոչ մշտական Linux-ում, մշտական Windows/macOS-ում).:

`podman login {{registry.example.org}}`

- Համառորեն մուտք գործեք ռեեստր Linux-ով.:

`podman login --authfile $HOME/.config/containers/auth.json {{registry.example.org}}`

- Մուտք գործեք անապահով (HTTP) ռեեստր.:

`podman login --tls-verify false {{registry.example.org}}`
