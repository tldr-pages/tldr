# satis

> Satis 정적 Composer 저장소를 위한 명령줄 도구.
> 더 많은 정보: <https://github.com/composer/satis>.

- Satis 구성 초기화:

`satis init {{satis.json}}`

- Satis 구성에 VCS 저장소 추가:

`satis add {{저장소_주소}}`

- 구성에서 정적 출력 생성:

`satis build {{satis.json}} {{경로/대상/출력_폴더}}`

- 지정된 저장소만 업데이트하여 정적 출력 생성:

`satis build --repository-url {{저장소_주소}} {{satis.json}} {{경로/대상/출력_폴더}}`

- 불필요한 아카이브 파일 제거:

`satis purge {{satis.json}} {{경로/대상/출력_폴더}}`
