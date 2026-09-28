# ananicy-cpp

> Linux용 Ananicy 자동 nicev 데몬을 C++로 다시 구현한 기능 확장 버전.
> 더 많은 정보: <https://gitlab.com/ananicy-cpp/ananicy-cpp>.

- 현재 파싱된 모든 규칙과 규칙 파일을 출력:

`ananicy-cpp dump rules`

- 설정된 모든 프로세스 유형을 출력:

`ananicy-cpp dump types`

- 현재 규칙을 JSON 형식으로 출력:

`ananicy-cpp dump rules --json`

- 사용자 지정 규칙 파일을 적용하지 않고 파싱 및 유효성 검사:

`ananicy-cpp parse {{경로/대상/파일.rules}}`
