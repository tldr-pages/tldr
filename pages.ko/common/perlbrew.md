# perlbrew

> 홈 디렉토리에서 Perl 설치를 관리.
> 같이 보기: `asdf`.
> 더 많은 정보: <https://github.com/gugod/App-perlbrew>.

- `perlbrew` 환경 초기화:

`perlbrew init`

- 사용 가능한 Perl 버전 나열:

`perlbrew available`

- Perl 버전 설치/제거:

`perlbrew {{install|uninstall}} {{버전}}`

- Perl 설치 목록:

`perlbrew list`

- 특정 설치로 전환하고 기본값으로 설정:

`perlbrew switch perl-{{버전}}`

- 시스템 Perl 다시 사용:

`perlbrew off`

- 사용 중인 설치에 대해 설치된 CPAN 모듈 나열:

`perlbrew list-modules`

- 한 설치에서 다른 설치로 CPAN 모듈 복제:

`perlbrew clone-modules {{소스_설치}} {{대상_설치}}`
