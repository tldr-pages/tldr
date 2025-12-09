# gbp

> Git을 사용하여 Debian 패키지 빌드 시스템과 통합하는 시스템.
> 더 많은 정보: <https://honk.sigxcpu.org/projects/git-buildpackage/manual-html/gbp.html>.

- 기존 Debian 패키지를 gbp로 변환:

`gbp import-dsc {{경로/대상/패키지.dsc}}`

- 현재 디렉토리에서 기본 빌더(`debuild`)를 사용하여 패키지 빌드:

`gbp buildpackage -jauto -us -uc`

- Debian Bullseye용 `pbuilder` 환경에서 패키지 빌드:

`DIST={{bullseye}} ARCH={{amd64}} gbp buildpackage -jauto -us -uc --git-builder={{git-pbuilder}}`

- `.changes` 파일에서 패키지를 소스 전용 업로드로 지정 (참조: <https://wiki.debian.org/SourceOnlyUpload>):

`gbp buildpackage -jauto -us -uc --changes-options={{-S}}`

- 새로운 업스트림 릴리스 가져오기:

`gbp import-orig --pristine-tar {{경로/대상/패키지.tar.gz}}`
