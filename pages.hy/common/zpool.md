# zpool

> Կառավարեք ZFS լողավազանները:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/zpool>:.

- Ցույց տալ բոլոր ZFS zpool-ների կազմաձևումն ու կարգավիճակը.:

`zpool status`

- Ստուգեք ZFS լողավազանը սխալների համար (ստուգում է ԱՄԵՆ բլոկի ստուգաչափը): Շատ պրոցեսոր և սկավառակի ինտենսիվ:

`zpool scrub {{pool_name}}`

- Ցուցակեք ներմուծման համար մատչելի zpool-ները.:

`zpool import`

- Ներմուծեք zpool.:

`zpool import {{pool_name}}`

- Արտահանել zpool (ապամոնտաժել բոլոր ֆայլային համակարգերը).:

`zpool export {{pool_name}}`

- Ցույց տալ լողավազանի բոլոր գործողությունների պատմությունը.:

`zpool history {{pool_name}}`

- Ստեղծեք հայելային լողավազան.:

`zpool create {{pool_name}} mirror {{disk1}} {{disk2}} mirror {{disk3}} {{disk4}}`

- Ավելացնել քեշ (L2ARC) սարք zpool-ում.:

`zpool add {{pool_name}} cache {{cache_disk}}`
