# pio update

> 설치된 PlatformIO Core 패키지, 개발 플랫폼 및 전역 라이브러리를 업데이트.
> 같이 보기: `pio platform update`, `pio lib update`.
> 더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/cmd_update.html>.

- 모든 패키지, 개발 플랫폼 및 전역 라이브러리를 완전히 업데이트:

`pio update`

- 코어 패키지만 업데이트 (플랫폼 및 라이브러리는 건너뜀):

`pio update --core-packages`

- 패키지, 플랫폼 및 라이브러리의 새 버전을 확인하되 실제로 업데이트하지는 않음:

`pio update --dry-run`
