# debuild

> 소스에서 Debian 패키지를 빌드합니다.
> 더 많은 정보: <https://manned.org/debuild.1>.

- 현재 디렉토리에서 패키지 빌드:

`debuild`

- 바이너리 패키지만 빌드:

`debuild -b`

- 패키지 빌드 후 lintian을 실행하지 않음:

`debuild --no-lintian`
