# redshift

> 주변 환경에 따라 화면의 색온도를 조정.
> 더 많은 정보: <https://manned.org/redshift>.

- 낮 동안 특정 [t]온도(예: 5700K)와 밤 동안 특정 온도(예: 3600K)로 Redshift 켜기:

`redshift -t {{5700}}:{{3600}}`

- 수동으로 지정한 맞춤 [l]위치로 Redshift 켜기:

`redshift -l {{위도}}:{{경도}}`

- 낮 동안 특정 화면 [b]밝기(예: 70%)와 밤 동안 특정 밝기(예: 40%)로 Redshift 켜기:

`redshift -b {{0.7}}:{{0.4}}`

- 맞춤 [g]감마 수준(0과 1 사이)으로 Redshift 켜기:

`redshift -g {{red}}:{{green}}:{{blue}}`

- 기존의 온도 변화를 [P]제거하고 [O]ne-shot 모드에서 일정한 색온도를 설정:

`redshift -PO {{온도}}`
