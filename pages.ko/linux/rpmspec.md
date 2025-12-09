# rpmspec

> RPM 스펙 파일을 쿼리합니다.
> 더 많은 정보: <https://manned.org/rpmspec>.

- RPM 스펙 파일에서 생성될 바이너리 패키지 나열:

`rpmspec --query {{경로/대상/rpm.spec}}`

- `--queryformat`의 모든 옵션 나열:

`rpmspec --querytags`

- RPM 스펙 파일에서 생성된 단일 바이너리 패키지의 요약 정보 가져오기:

`rpmspec --query --queryformat "{{%{name}: %{summary}\n}}" {{경로/대상/rpm.spec}}`

- RPM 스펙 파일에서 생성될 소스 패키지 가져오기:

`rpmspec --query --srpm {{경로/대상/rpm.spec}}`

- RPM 스펙 파일을 `stdout`으로 파싱:

`rpmspec --parse {{경로/대상/rpm.spec}}`
