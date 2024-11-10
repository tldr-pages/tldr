# rpmbuild

> RPM 패키지 빌드 도구.
> 더 많은 정보: <https://manned.org/rpmbuild>.

- 바이너리 및 소스 패키지 빌드:

`rpmbuild -ba {{경로/대상/spec_파일}}`

- 소스 패키지 없이 바이너리 패키지 빌드:

`rpmbuild -bb {{경로/대상/spec_파일}}`

- 패키지를 빌드할 때 추가 변수 지정:

`rpmbuild -bb {{경로/대상/spec_파일}} --define "{{변수1}} {{값1}}" --define "{{변수2}} {{값2}}"`
