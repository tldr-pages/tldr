# rpmconf

> 패키지 업그레이드 후 남겨진 RPMNEW, RPMSAVE 및 RPMORIG 파일 처리.
> 같이 보기: `rpm`.
> 더 많은 정보: <https://manned.org/man/rpmconf.8>.

- 남겨진 파일을 나열하고 각 파일에 대해 수행할 작업을 인터랙티브하게 선택:

`sudo rpmconf --all`

- 고아가 된 RPMNEW 및 RPMSAVE 파일 삭제:

`sudo rpmconf --all --clean`
