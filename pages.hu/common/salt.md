# salt

> Parancsok végrehajtása és állapotmegállapítás távoli salt minionokon. További információ: <https://docs.saltstack.com/ref/cli/salt.html>.

- Kapcsolódó minionok listája:

`salt '*' test.ping`

- Highstate végrehajtása az összes csatlakoztatott minionon:

`salt '*' state.highstate`

- Csomagok frissítése az operációs rendszer csomagkezelőjének (apt, yum, brew) segítségével a minionok egy részhalmazán:

`salt '*.example.com' pkg.upgrade`

- Tetszőleges parancs végrehajtása egy adott minionon:

`salt '{{minion_id}}' cmd.run "ls "`
