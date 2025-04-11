# urpmq

> Mageia에서 패키지 및 미디어에 대한 정보를 조회합니다.
> 같이 보기: `urpmi`, `urpmi.update`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpme`.
> 더 많은 정보: <https://man.linuxreviews.org/man8/urpmq.8.html>.

- 설치 가능한 패키지에 대한 정보 표시:

`urpmq -i {{패키지}}`

- 패키지의 직접적인 의존성 표시:

`urpmq --requires {{패키지}}`

- 패키지의 직접 및 간접 의존성 표시:

`urpmq --requires-recursive {{패키지}}`

- RPM [f]파일에 필요한 설치되지 않은 패키지 및 소스 나열:

`sudo urpmq --requires-recursive -m --sources {{경로/대상/파일.rpm}}`

- URL과 함께 모든 구성된 미디어 나열(비활성 미디어 포함):

`urpmq --list-media --list-url`

- 패키지 검색 시 [g]그룹, 버전 및 [r]릴리즈 출력:

`urpmq -g -r --fuzzy {{키워드}}`

- 패키지의 정확한 이름을 사용하여 검색:

`urpmq -g -r {{패키지}}`
