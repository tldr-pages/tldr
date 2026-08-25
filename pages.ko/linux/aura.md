# aura

> Aura 패키지 매니저(Aura Package Manager): Arch Linux 및 AUR를 위한 안전하고 다국어를 지원하는 패키지 관리자.
> 더 많은 정보: <https://github.com/fosskers/aura>.

- AUR에서 패키지 검색:

`aura {{[-As|--aursync --search]}} {{키워드|정규표현시}}`

- AUR에서 패키지 설치:

`aura {{[-A|--aursync]}} {{패키지}}`

- 모든 AUR 패키지를 상세 모드로 업데이트하고 make 의존성을 제거:

`aura {{[-Akua|--aursync --diff --sysupgrade --delmakedeps]}}`

- 공식 저장소에서 패키지 설치:

`aura {{[-S|--sync]}} {{패키지}}`

- 공식 저장소의 모든 패키지 동기화 및 업데이트:

`aura {{[-Syu|--sync --refresh --sysupgrade]}}`

- 패키지 및 의존성 제거:

`aura {{[-Rsu|--remove --recursive --unneeded]}} {{패키지}}`

- orphan 패키지 제거 (어떤 패키지도 필요로 하지 않는 의존성 패키지):

`aura {{[-Oj|--orphans --abandon]}}`
