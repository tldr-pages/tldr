# reuse

> REUSE 권장 사항의 라이선스 및 저작권 규정 준수를 지원하는 도구.
> 더 많은 정보: <https://reuse.readthedocs.io/en/stable/man/index.html>.

- 현재 프로젝트가 REUSE 규정을 준수하는지 검사 (버전 관리 시스템 인식):

`reuse lint`

- 지정한 디렉터리에서 REUSE 규정 준수 여부 검사:

`reuse --root {{경로/대상/디렉터리}} lint`

- 파일에 저작권 정보 추가:

`reuse annotate {{[-c|--copyright]}} "{{대상_이름}} <{{대상_이메일}}>" --fallback-dot-license {{경로/대상/파일}}`

- 파일에 라이선스 정보 추가:

`reuse annotate {{[-l|--license]}} {{spdx_식별자}} --fallback-dot-license {{경로/대상/파일}}`

- SPDX 식별자로 라이선스를 다운로드하여 LICENSES 디렉터리에 저장:

`reuse download {{spdx-식별자}}`

- 프로젝트에서 누락된 모든 라이선스 다운로드:

`reuse download --all`
