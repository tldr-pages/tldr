# repair-bde

> 손상된 BitLocker 암호화 볼륨을 복구하거나 해독하려고 시도합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/repair-bde>.

- 지정된 볼륨을 복구하려고 시도:

`repair-bde {{C:}}`

- 지정된 볼륨을 복구하려고 시도하고 다른 볼륨에 출력:

`repair-bde {{C:}} {{D:}}`

- 제공된 복구 키 파일 사용하여 지정된 볼륨을 복구하려고 시도:

`repair-bde {{C:}} -RecoveryKey {{경로\대상\파일.bek}}`

- 제공된 숫자 복구 암호 사용하여 지정된 볼륨을 복구하려고 시도:

`repair-bde {{C:}} -RecoveryPassword {{암호}}`

- 제공된 암호 사용하여 지정된 볼륨을 복구하려고 시도:

`repair-bde {{C:}} -Password {{암호}}`

- 제공된 키 패키지 사용하여 지정된 볼륨을 복구하려고 시도:

`repair-bde {{C:}} -KeyPackage {{경로\대상\디렉토리}}`

- 모든 출력을 특정 파일에 기록:

`repair-bde {{C:}} -LogFile {{경로\대상\파일}}`

- 도움말 표시:

`repair-bde /?`
