# Compress-Archive

> PowerShell에서 압축(zipped) 아카이브 파일을 생성하는 cmdlet.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.archive/compress-archive>.

- 단일 파일 압축:

`Compress-Archive -Path {{경로\대상\파일.txt}} -DestinationPath {{경로\대상\파일.zip}}`

- 여러 파일 압축:

`Compress-Archive -Path {{경로\대상\파일1, 경로\대상\파일2, ...}} -DestinationPath {{경로\대상\파일s.zip}}`

- 디렉터리 압축:

`Compress-Archive -Path {{경로\대상\디렉터리}} -DestinationPath {{경로\대상\디렉터리.zip}}`

- 기존 압축 파일 업데이트:

`Compress-Archive -Path {{경로\대상\파일}} -DestinationPath {{경로\대상\디렉터리.zip}} -Update`

- 압축 수준 설정 (`Optimal`: 최대 압축, `Fastest`: 빠른 압축, `NoCompression`: 압축 안 함):

`Compress-Archive -Path {{경로\대상\디렉터리}} -DestinationPath {{경로\대상\디렉터리.zip}} -CompressionLevel {{Optimal|Fastest|NoCompression}}`
