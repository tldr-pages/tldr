# choco push

> 컴파일된 NuGet 패키지(`nupkg`)를 패키지 피드에 푸시합니다.
> 더 많은 정보: <https://docs.chocolatey.org/en-us/create/commands/push>.

- 컴파일된 `nupkg`를 지정된 피드에 푸시:

`choco push --source {{https://push.chocolatey.org/}}`

- 지정된 피드에 컴파일된 `nupkg`를 푸시하며, 초 단위로 타임아웃 설정 (기본값은 2700):

`choco push --source {{https://push.chocolatey.org/}} --execution-timeout {{500}}`
