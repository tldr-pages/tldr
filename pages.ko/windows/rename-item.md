# Rename-Item

> 항목의 이름을 변경하는 PowerShell 명령어.
> 참고: `ren`와 `rni` 모두 `Rename-Item`의 별칭으로 사용 가능.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/rename-item>.

- 파일 이름 변경:

`Rename-Item -Path "{{경로\대상\파일}}" -NewName "{{새로운_파일_이름}}"`

- 디렉터리 이름 변경:

`Rename-Item -Path "{{경로\대상\디렉터리}}" -NewName "{{새로운_디렉터리_이름}}"`

- 파일 이름 변경 및 이동:

`Rename-Item -Path "{{경로\대상\파일}}" -NewName "{{경로\대상\새로운_파일_이름}}"`

- 강제로 파일 이름 변경:

`Rename-Item -Path "{{경로\대상\파일}}" -NewName "{{새로운_파일_이름}}" -Force`

- 파일 이름 변경 전에 확인 메시지 표시:

`Rename-Item -Path "{{경로\대상\파일}}" -NewName "{{새로운_파일_이름}}" {{[-Confirm|-cf]}}`
