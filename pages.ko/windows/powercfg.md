# powercfg

> 전원 설정 구성 및 관리 계획 수립.
> 더 많은 정보: <https://learn.microsoft.com/windows-hardware/design/device-experiences/powercfg-command-line-options>.

- 현재 활성화된 전원 관리 계획 표시:

`powercfg /getactivescheme`

- 사용 가능한 모든 전원 관리 계획 목록 표시:

`powercfg {{[/L|/list]}}`

- GUID를 사용하여 활성 전원 관리 계획 설정:

`powercfg /setactive {{GUID}}`

- AC 전원 사용 시 지정한 분 후 디스플레이 끄기:

`powercfg {{[/X|/change]}} monitor-timeout-ac {{분}}`

- 배터리 사용 시 지정한 분 후 디스플레이 끄기:

`powercfg {{[/X|/change]}} monitor-timeout-dc {{분}}`

- AC 전원 사용 시 지정한 분 후 시스템 절전 모드로 전환:

`powercfg {{[/X|/change]}} standby-timeout-ac {{분}}`

- 시스템 절전 진단 보고서를 생성하여 파일로 저장:

`powercfg /sleepstudy /output {{경로\대상\보고서.html}}`

- 전체 전원 효율성 보고서를 생성하여 파일로 저장:

`powercfg /energy /output {{경로\대상\보고서.html}}`
