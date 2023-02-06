# ngrep

> A hálózati forgalmi csomagok szűrése szabályos kifejezések segítségével. További információ: <https://github.com/jpr5/ngrep>.

- Az összes interfész forgalmának rögzítése:

`ngrep -d any`

- Egy adott interfész forgalmának rögzítése:

`ngrep -d {{eth0}}`

- Az eth0 interfész 22-es portján áthaladó forgalom rögzítése:

`ngrep -d {{eth0}} port {{22}}`

- Egy állomásról érkező vagy oda irányuló forgalom rögzítése:

`ngrep host {{www.example.com}}`

- Az eth0 interfész 'User-Agent:' kulcsszava:

`ngrep -d {{eth0}} '{{User-Agent:}}'`
