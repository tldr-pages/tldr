# distccd

> Kiszolgáló démon a distcc elosztott fordítóprogramhoz. További információ: <https://distcc.github.io>.

- Indítson el egy démont az alapértelmezett beállításokkal:

`distccd --daemon`

- Indítson el egy démont, amely IPv4-es magánhálózati tartományokból fogad kapcsolatokat:

`distccd --daemon --allow-private`

- Indítson el egy démont, amely egy adott hálózati címről vagy címtartományból fogad kapcsolatokat:

`distccd --daemon --allow {{ip_address|network_prefix}}`

- Indítson el egy démont csökkentett prioritással, amely egyszerre legfeljebb 4 feladatot tud futtatni:

`distccd --daemon --jobs {{4}} --nice {{5}}`

- Démon indítása és regisztrálása az mDNS/DNS-SD (Zeroconf) segítségével:

`distccd --daemon --zeroconf`
