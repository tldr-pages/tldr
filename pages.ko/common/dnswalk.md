# dnswalk

> DNS 디버깅 도구.
> DNS 존을 따라가며("Walk") 데이터베이스의 일관성과 모범 사례를 검증.
> 더 많은 정보: <https://manned.org/dnswalk>.

- FQDN(정규화된 도메인 이름)에 대한 DNS 경로 디버깅:

`dnswalk {{도메인}}.`

- 서브 도메인을 재귀적으로([r]ecursively) 처리:

`dnswalk -r {{도메인}}.`

- 마지막 실행 이후 존이 수정된([m]odified)에만 `dnswalk` 수행:

`dnswalk -m {{도메인}}.`

- 디버깅([d]ebugging) 및 상태 정보를 `stdout` 대신 `stderr`로 출력:

`dnswalk -d {{도메인}}.`

- 도메인 이름의 잘못된([i]nvalid) 문자 검사 비활성화:

`dnswalk -i {{도메인}}.`

- 중복된 A 레코드 경고 활성화:

`dnswalk -a {{도메인}}.`

- A 레코드의 PTR 이름과 정방향 이름을 비교하여 불일치 시 보고하는 "[F]ascist checking" 활성화:

`dnswalk -F {{도메인}}.`

- 지정된 호스트가 권한 있는 응답을 반환하는지 테스트하는 "[l]ame delegation" 검사 활성화:

`dnswalk -l {{도메인}}.`
