# particle

> Particle 장치를 조작.
> 더 많은 정보: <https://docs.particle.io/tutorials/developer-tools/cli>.

- Particle CLI에 로그인하거나 계정 생성:

`particle setup`

- 장치 목록 표시:

`particle list`

- 대화형으로 새 Particle 프로젝트 생성:

`particle project create`

- Particle 프로젝트 컴파일:

`particle compile {{장치_유형}} {{경로/대상/소스_코드.ino}}`

- 특정 앱을 원격으로 사용하도록 장치 업데이트:

`particle flash {{장치_이름}} {{경로/대상/프로그램.bin}}`

- 최신 펌웨어로 장치를 시리얼로 업데이트:

`particle flash --serial {{경로/대상/방화벽.bin}}`

- 장치에서 함수 실행:

`particle call {{장치_이름}} {{함수_이름}} {{함수_인자}}`
