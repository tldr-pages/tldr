# py-spy

> Mintavételi profilozó Python programokhoz. További információ: <https://github.com/benfred/py-spy>.

- Élő nézetben megmutatja azokat a függvényeket, amelyek a legtöbb végrehajtási időt veszik igénybe egy futó folyamatból:

`py-spy top --pid {{pid}}`

- Indítson el egy programot, és mutassa meg a legtöbb végrehajtási időt igénylő függvények élő nézetét:

`py-spy top -- python {{path/to/file.py}}`

- Készítsen SVG lánggráfot a függvényhívások végrehajtási idejéről:

`py-spy record -o {{path/to/profile.svg}} --pid {{pid}}`

- Egy futó folyamat hívási veremének kiürítése:

`py-spy dump --pid {{pid}}`
