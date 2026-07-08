# GetHelpCmd OutlookCalendarCheckTask

> 기존 Microsoft Outlook 애플리케이션의 일정 구성 문제를 검사.
> `GetHelpCmd.exe`의 일부, 이전 명칭은 `SaRAcmd.exe` (Microsoft Support and Recovery Assistant).
> 참고: 이 도구는 더 이상 사용되지 않으며, 새로운 Outlook 애플리케이션에서는 동작하지 않음.
> 더 많은 정보: <https://learn.microsoft.com/troubleshoot/microsoft-365/admin/miscellaneous/get-help-outlook-calendar-scan>.

- 현재 활성 Outlook 프로필의 일정을 검사하고 최종 사용자 사용권 계약(End-User License Agreement, EULA)에 동의:

`GetHelpCmd.exe -S OutlookCalendarCheckTask -AcceptEula`

- 지정한 Outlook 프로필의 일정 검사:

`GetHelpCmd.exe -S OutlookCalendarCheckTask -AcceptEula -P {{프로필}}`

- 지정한 Outlook 프로필의 일정을 검사하고 로그를 지정한 디렉터리에 저장:

`GetHelpCmd.exe -S OutlookCalendarCheckTask -AcceptEula -P {{프로필}} -LogFolder {{경로\대상\디렉터리}}`

- 진행 상황을 표시하지 않고 지정한 Outlook 프로필의 일정 검사:

`GetHelpCmd.exe -S OutlookCalendarCheckTask -AcceptEula -P {{프로필}} -HideProgress`
