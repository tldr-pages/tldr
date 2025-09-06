# flips

> IPS 및 BPS 파일용 패치를 생성하고 적용.
> 더 많은 정보: <https://github.com/Alcaro/Flips>.

- 대화형으로 패치를 생성하고 적용하려면 Flips를 시작:

`flips`

- 패치를 적용하고 새 ROM 파일을 만듬:

`flips --apply {{patch.bps}} {{rom.smc}} {{hack.smc}}`

- 두 개의 ROM에서 패치를 만듬:

`flips --create {{rom.smc}} {{hack.smc}} {{patch.bps}}`
