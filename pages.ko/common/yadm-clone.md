# yadm clone

> `git clone`과 유사하게 작동하며, 추가 플래그를 통해 저장소를 구성할 수 있습니다.
> 저장소에 부트스트랩 파일이 있으면 실행 여부를 묻습니다.
> 같이 보기: `git clone`.
> 더 많은 정보: <https://yadm.io/docs/common_commands>.

- 기존 저장소 복제:

`yadm clone {{원격_저장소_위치}}`

- 기존 저장소를 복제하고 부트스트랩 파일 실행:

`yadm clone {{원격_저장소_위치}} --bootstrap`

- 기존 저장소를 복제한 후 부트스트랩 파일을 실행하지 않음:

`yadm clone {{원격_저장소_위치}} --no-bootstrap`

- 복제 중 `yadm`이 사용할 작업 트리 변경:

`yadm clone {{원격_저장소_위치}} --w {{작업_트리_파일}}`

- `yadm`이 파일을 가져오는 분기 변경:

`yadm clone {{원격_저장소_위치}} -b {{분기}}`

- 기존 저장소 로컬 분기 덮어쓰기:

`yadm clone {{원격_저장소_위치}} -f`
