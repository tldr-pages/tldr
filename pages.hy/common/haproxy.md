#հապրոքսի

> Արագ և հուսալի HTTP հակադարձ վստահված անձ և բեռի հավասարակշռող:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/haproxy>:.

- Ստուգեք կազմաձևման ֆայլը վավերականության համար.:

`haproxy -c -f {{path/to/haproxy.cfg}}`

- Սկսեք HAProxy-ն կազմաձևման ֆայլով.:

`haproxy -f {{path/to/haproxy.cfg}}`

- Սկսեք daemon ռեժիմով.:

`haproxy -D -f {{path/to/haproxy.cfg}}`

- Սկսեք վարպետ-աշխատող ռեժիմով.:

`haproxy -W -f {{path/to/haproxy.cfg}}`

- Սկսեք միացված վրիպազերծման ռեժիմից (առաջին պլան, մանրամասն ելք).:

`haproxy -d -f {{path/to/haproxy.cfg}}`

- Վերբեռնեք կազմաձևը հին գործընթացի նրբագեղ անջատմամբ.:

`haproxy -f {{path/to/haproxy.cfg}} -sf {{pid}}`

- Սահմանեք միաժամանակյա միացումների առավելագույն քանակը.:

`haproxy -f {{path/to/haproxy.cfg}} -n {{maxconn}}`

- Վերալիցքավորեք զրոյական պարապուրդով՝ նորից օգտագործելով հին գործընթացի վարդակները.:

`haproxy -f {{path/to/haproxy.cfg}} -x {{path/to/haproxy.sock}} -sf {{pid}}`
