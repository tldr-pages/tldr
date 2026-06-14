# rkdeveloptool

> Flash, թափել և կառավարել բեռնման որոնվածը Rockchip-ի վրա հիմնված համակարգչային սարքերի համար:.
> Դուք պետք է սարքը միացնեք Maskrom/Bootrom ռեժիմին՝ նախքան այն USB-ի միջոցով միացնելը:.
> Որոշ ենթահրամաններ կարող են պահանջել գործարկել որպես արմատ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/rockchip-linux/rkdeveloptool>:.

- [l] թվարկեք Rockchip-ի վրա հիմնված բոլոր միացված ֆլեշ [d] սարքերը՝:

`rkdeveloptool ld`

- Նախաձեռնեք սարքը՝ ստիպելով նրան [d]ներբեռնել և տեղադրել [b]ootloader-ը նշված ֆայլից.:

`rkdeveloptool db {{path/to/bootloader.bin}}`

- [u] թարմացրեք boot[l]oader ծրագրաշարը նորով.:

`rkdeveloptool ul {{path/to/bootloader.bin}}`

- Գրեք պատկեր GPT ձևաչափով ֆլեշ բաժանման մեջ՝ նշելով պահեստավորման սկզբնական հատվածը (սովորաբար `0x0` կեղծանունը՝ `0`):

`rkdeveloptool wl {{initial_sector}} {{path/to/image.img}}`

- Ֆլեշ միջնորմում գրեք օգտագործողի համար հարմար անունով.:

`rkdeveloptool wlx {{partition_name}} {{path/to/image.img}}`

- [r]set/վերագործարկեք [d]սարքը, դուրս եկեք Maskrom/Bootrom ռեժիմից՝ ընտրված ֆլեշ միջնորմը բեռնելու համար.:

`rkdeveloptool rd`
