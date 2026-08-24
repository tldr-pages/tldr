# GetHelpCmd ExpertExperienceAdminTask

> 기존 Microsoft Outlook with Microsoft Office 및 Windows의 설치 및 구성 정보를 자세히 수집.
> `GetHelpCmd.exe`의 일부, 이전 명칭은 `SaRAcmd.exe` (Microsoft Support and Recovery Assistant).
> 참고: 이 도구는 더 이상 사용되지 않으며, 새로운 Outlook 애플리케이션에서는 동작하지 않음.
> 더 많은 정보: <https://learn.microsoft.com/troubleshoot/microsoft-365/admin/miscellaneous/get-help-outlook-scan>.

- 최종 사용자 사용권 계약(End-User License Agreement, EULA)에 동의하고 상세 정보 수집:

`GetHelpCmd.exe -S ExpertExperienceAdminTask -AcceptEula`

- 상세 정보를 수집하고 로그를 지정한 디렉터리에 저장:

`GetHelpCmd.exe -S ExpertExperienceAdminTask -AcceptEula -LogFolder {{경로\대상\디렉터리}}`

- 진행 상황을 표시하지 않고 상세 정보 수집:

`GetHelpCmd.exe -S ExpertExperienceAdminTask -AcceptEula -HideProgress`
