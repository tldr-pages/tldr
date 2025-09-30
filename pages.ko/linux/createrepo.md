# createrepo

> 디렉터리에 RPM 저장소를 초기화하고 모든 XML 및 SQLite 파일을 포함합니다.
> 더 많은 정보: <https://manned.org/createrepo>.

- 기본 저장소를 디렉터리에서 초기화:

`createrepo {{경로/대상/폴더}}`

- 저장소를 초기화하고, 테스트 RPM을 제외하고, 자세한 로그를 표시:

`createrepo -v -x {{test_*.rpm}} {{경로/대상/폴더}}`

- SHA1을 체크섬 알고리즘으로 사용하고, 심볼릭 링크를 무시하여 저장소를 초기화:

`createrepo -S -s {{sha1}} {{경로/대상/폴더}}`
