# amass enum

> 도메인의 하위 도메인 찾기.
> 더 많은 정보: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- 도메인([d]omain)의 하위 도메인을 (수동적으로) 찾기:

`amass enum -d {{도메인_이름}}`

- 도메인([d]omain)의 하위 도메인을 찾아 발견된 하위 도메인을 해결하려고 시도하면서, 적극적으로 확인:

`amass enum -active -d {{도메인_이름}} -p {{80,443,8080}}`

- 하위 도메인(sub[d]omains)에 대한 무차별 대입 검색을 수행:

`amass enum -brute -d {{도메인_이름}}`

- 결과를 텍스트 파일에 저장:

`amass enum -o {{출력_파일}} -d {{도메인_이름}}`

- 터미널 출력을 파일에 저장하고 기타 자세한 출력을 디렉터리에 저장:

`amass enum -o {{출력_파일}} -dir {{경로/대상/디렉터리}} -d {{도메인_이름}}`

- 사용 가능한 모든 데이터 소스 나열:

`amass enum -list`
