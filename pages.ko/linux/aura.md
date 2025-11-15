# aura

> Aura 패키지 관리자: Arch Linux 및 AUR를 위한 안전하고 다국어 지원 패키지 관리자.
> 더 많은 정보: <https://github.com/fosskers/aura>.

- 공식 저장소 및 AUR에서 패키지 검색:

`aura --aursync --both --search {{키워드|정규_표현식}}`

- AUR에서 패키지 설치:

`aura --aursync {{패키지}}`

- AUR 패키지를 자세히 모드로 업데이트하고 모든 make 의존성 제거:

`aura --aursync --diff --sysupgrade --delmakedeps --unsuppress`

- 공식 저장소에서 패키지 설치:

`aura --sync {{패키지}}`

- 공식 저장소에서 모든 패키지 동기화 및 업데이트:

`aura --sync --refresh --sysupgrade`

- 패키지 캐시를 사용하여 패키지 다운그레이드:

`aura --downgrade {{패키지}}`

- 패키지 및 의존성 제거:

`aura --remove --recursive --unneeded {{패키지}}`

- 고아 패키지(의존성으로 설치되었지만 더 이상 어떤 패키지도 필요로 하지 않는 패키지) 제거:

`aura --orphans --abandon`
