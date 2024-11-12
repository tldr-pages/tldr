# Set-Volume

> 기존 볼륨의 파일 시스템 레이블을 설정하거나 변경합니다.
> 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/storage/set-volume>.

- 드라이브 문자로 식별되는 볼륨의 파일 시스템 레이블 변경:

`Set-Volume -DriveLetter "D" -NewFileSystemLabel "DataVolume"`

- 시스템 레이블로 식별되는 볼륨의 파일 시스템 레이블 변경:

`Set-Volume -FileSystemLabel "OldLabel" -NewFileSystemLabel "NewLabel"`

- 볼륨 개체의 속성 수정:

`Set-Volume -InputObject $(Get-Volume -DriveLetter "E") -NewFileSystemLabel "Backup"`

- 볼륨에 대한 데이터 중복 제거 모드 지정:

`Set-Volume -DriveLetter "D" -DedupMode Backup`
