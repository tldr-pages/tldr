# docker rmi

> Bir veya daha fazla Docker imgesini sil.
> Daha fazla bilgi için: <https://docs.docker.com/reference/cli/docker/image/rm/>.

- Yardım göster:

`docker rmi`

- Bir veya daha fazla imgeyi isimlerini belirterek sil:

`docker rmi {{imge1 imge2 ...}}`

- Bir imgeyi zorla sil:

`docker rmi {{[-f|--force]}} {{imge}}`

- Bir imgeyi etiketlenmemiş ana yollarını silmeden sil:

`docker rmi --no-prune {{imge}}`
