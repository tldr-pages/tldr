# docker rmi

> Bir veya daha fazla Docker imgesini sil.
> Daha fazla bilgi: <https://docs.docker.com/engine/reference/commandline/rmi/>.

- Yardım göster:

`docker rmi`

- Bir veya daha fazla imgeyi isimlerini belirterek sil:

`docker rmi {{imge1 imge2 ...}}`

- Bir imgeyi zorla sil:

`docker rmi --force {{imge}}`

- Bir imgeyi etiketlenmemiş ana yollarını silmeden sil:

`docker rmi --no-prune {{imge}}`
