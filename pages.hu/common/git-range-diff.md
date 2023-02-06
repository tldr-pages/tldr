# git range-diff

> Két commit tartomány összehasonlítása (pl. egy ág két verziója). További információ: <https://git-scm.com/docs/git-range-diff>.

- Két egyedi commit változásainak diffúzálása:

`git range-diff {{commit_1}}^! {{commit_2}}^!`

- A mi és az övék közös őstől származó változásainak összehasonlítása, pl. egy interaktív újraindítás után:

`git range-diff {{theirs}}...{{ours}}`

- Két commit-tartomány változtatásainak összehasonlítása, pl. annak ellenőrzésére, hogy a konfliktusok megfelelően lettek-e megoldva, amikor a `base1` -tól a `base2`-ig terjedő commit-ok újraalapozására került sor:

`git range-diff {{base1}}..{{rev1}} {{base2}}..{{rev2}}`
