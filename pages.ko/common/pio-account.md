# pio account

> 명령줄에서 PlatformIO 계정을 관리.
> 더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/account/>.

- 새 PlatformIO 계정 등록:

`pio account register --username {{사용자이름}} --email {{이메일}} --password {{비밀번호}} --firstname {{이름}} --lastname {{성}}`

- PlatformIO 계정 및 관련 데이터 영구 삭제:

`pio account destroy`

- PlatformIO 계정에 로그인:

`pio account login --username {{사용자이름}} --password {{비밀번호}}`

- PlatformIO 계정에서 로그아웃:

`pio account logout`

- PlatformIO 프로필 업데이트:

`pio account update --username {{사용자이름}} --email {{이메일}} --firstname {{이름}} --lastname {{성}} --current-password {{비밀번호}}`

- PlatformIO 계정에 대한 자세한 정보 표시:

`pio account show`

- 사용자 이름이나 이메일을 사용하여 비밀번호 재설정:

`pio account forgot --username {{사용자이름_또는_이메일}}`
