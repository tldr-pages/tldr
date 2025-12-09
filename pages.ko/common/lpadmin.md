# lpadmin

> CUPS 프린터 및 클래스를 구성.
> 같이 보기: `lpoptions`.
> 더 많은 정보: <https://openprinting.github.io/cups/doc/man-lpadmin.html>.

- 기본 프린터 설정:

`lpadmin -d {{프린터}}`

- 특정 프린터 또는 클래스 삭제:

`lpadmin -x {{프린터|클래스}}`

- 프린터를 클래스에 추가:

`lpadmin -p {{프린터}} -c {{클래스}}`

- 프린터를 클래스에서 제거:

`lpadmin -p {{프린터}} -r {{클래스}}`
