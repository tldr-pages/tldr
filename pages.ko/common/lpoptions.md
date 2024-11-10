# lpoptions

> 프린터 옵션 및 기본값 표시 또는 설정.
> 같이 보기: `lpadmin`.
> 더 많은 정보: <https://openprinting.github.io/cups/doc/man-lpoptions.html>.

- 기본 프린터 설정:

`lpoptions -d {{프린터[/인스턴스]}}`

- 특정 프린터의 프린터 전용 옵션 나열:

`lpoptions -d {{프린터}} -l`

- 특정 프린터에 새 옵션 설정:

`lpoptions -d {{프린터}} -o {{옵션}}`

- 특정 프린터의 옵션 제거:

`lpoptions -d {{프린터}} -x`
