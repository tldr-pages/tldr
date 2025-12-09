# steamcmd

> Steam 클라이언트의 커맨드라인 버전.
> 더 많은 정보: <https://manned.org/steamcmd>.

- 익명으로 애플리케이션 설치 또는 업데이트:

`steamcmd +login {{익명}} +app_update {{앱ID}} +quit`

- 지정된 자격 증명을 사용하여 애플리케이션 설치 또는 업데이트:

`steamcmd +login {{사용자명}} +app_update {{앱ID}} +quit`

- 특정 플랫폼용 애플리케이션 설치:

`steamcmd +@sSteamCmdForcePlatformType {{windows}} +login {{anonymous}} +app_update {{앱ID}} validate +quit`
