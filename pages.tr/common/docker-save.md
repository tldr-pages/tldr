# docker save

> Bir veya daha fazla docker imgesini arşivlemek için dışa aktar.
> Daha fazla bilgi için: <https://docs.docker.com/engine/reference/commandline/save/>.

- Bir imgeyi, stdout'u tar arşivine yönlendirerek kaydet:

`docker save {{imge}}:{{etiket}} > {örnek/dosya.tar}}`

- Bir imgeyi, bir tar arşivine kaydet:

`docker save --output {{örnek/dosya.tar}} {{imge}}:{{etiket}}`

- Bir imgenin tüm etiketlerini kaydet:

`docker save --output {{örnek/dosya.tar}} {{imge_ismi}}`

- Bir imgenin belirli etiketlerini kaydetmek için elle seç:

`docker save --output {{örnek/dosya.tar}} {{imge_ismi:etiket1 imge_ismi:etiket2 ...}}`
