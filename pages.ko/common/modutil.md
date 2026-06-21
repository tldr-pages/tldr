# modutil

> NSS 보안 모듈 데이터베이스에서 PKCS #11 모듈 정보 관리.
> 더 많은 정보: <https://manned.org/modutil>.

- NSS 데이터베이스에 PKCS #11 모듈 추가 (예: Firefox 프로필 디렉터리: `$HOME/.mozilla/firefox/default-release`):

`modutil -dbdir sql:{{경로/대상/nss_데이터베이스_디렉터리}} -add "{{모듈_라벨}}" -libfile {{경로/대상/pkcs11_mod.so}}`

- NSS 데이터베이스에 등록된 PKCS #11 모듈 목록 조회:

`modutil -dbdir sql:{{경로/대상/nss_데이터베이스_디렉터리}} -list`
