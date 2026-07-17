# GetHelpCmd OfficeActivationScenario

> Microsoft Office / Microsoft 365 Apps for Enterprise의 정품 인증 관련 문제를 자동으로 복구.
> Part of `GetHelpCmd.exe`, formerly `SaRAcmd.exe` (Microsoft Support and Recovery Assistant).
> 참고: 이 도구는 더 이상 사용되지 않으며, 새로운 OneNote 및 Outlook 애플리케이션에서는 동작하지 않음.
> 참고: 이 명령은 현재 설치된 Office 제품의 볼륨 라이선스를 변경, 비활성화 또는 제거할 수 있으므로 주의해서 사용해야 함.
> 관련 항목: `ospp.vbs`.
> 더 많은 정보: <https://learn.microsoft.com/troubleshoot/microsoft-365/admin/miscellaneous/get-help-office-activation>.

- Office를 종료하고, 최종 사용자 사용권 계약(End-User License Agreement, EULA)에 동의한 후 정품 인증 관련 오류를 자동으로 복구(관리자 권한이 필요):

`GetHelpCmd.exe -S OfficeActivationScenario -AcceptEula -CloseOffice`

- 현재 설치된 Office 라이선스를 공유 컴퓨터 정품 인증(Shared Computer Activation, SCA)에서 분리하고, 제품을 개별적으로 정품 인증(관리자 권한이 필요):

`GetHelpCmd.exe -S OfficeActivationScenario -AcceptEula -CloseOffice -RemoveSCA`
