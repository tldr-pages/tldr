# nvram

> 펌웨어 변수를 조작합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/nvram.8.html>.

- NVRAM에 저장된 모든 변수 [p]출력:

`nvram -p`

- NVRAM에 저장된 모든 변수를 [x]ML 형식으로 [p]출력:

`nvram -xp`

- 펌웨어 변수의 값 수정:

`sudo nvram {{이름}}="{{값}}"`

- 펌웨어 변수 [d]삭제:

`sudo nvram -d {{이름}}`

- 모든 펌웨어 변수 [c]지우기:

`sudo nvram -c`

- 특정 [x]ML [f]파일에서 펌웨어 변수 설정:

`sudo nvram -xf {{경로/대상/파일.xml}}`
