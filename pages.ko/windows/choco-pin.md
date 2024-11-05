# choco pin

> Chocolatey로 특정 버전의 패키지를 고정.
> 고정된 패키지는 업그레이드 시 자동으로 건너뜁니다.
> 더 많은 정보: <https://chocolatey.org/docs/commands-pin>.

- 고정된 패키지 및 해당 버전을 나열:

`choco pin list`

- 현재 버전으로 패키지를 고정:

`choco pin add --name {{패키지}}`

- 특정 버전으로 패키지를 고정:

`choco pin add --name {{패키지}} --version {{버전}}`

- 특정 패키지에 대한 고정을 제거:

`choco pin remove --name {{패키지}}`
