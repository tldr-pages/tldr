# flatpak

> flatpak 애플리케이션 및 런타임을 빌드, 설치, 실행.
> 더 많은 정보: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- 설치된 애플리케이션 실행:

`flatpak run {{com.example.app}}`

- 원격 소스로부터 애플리케이션 설치:

`flatpak install {{원격_소스_이름}} {{com.example.app}}`

- 설치된 애플리케이션 목록 보기 (런타임 제외):

`flatpak list --app`

- 설치된 모든 애플리케이션 및 런타임 업데이트:

`flatpak update`

- 원격 소스 추가:

`flatpak remote-add --if-not-exists {{원격_소스_이름}} {{원격_소스_URL}}`

- 설치된 애플리케이션 제거:

`flatpak remove {{com.example.app}}`

- 사용하지 않는 모든 애플리케이션 제거:

`flatpak remove --unused`

- 설치된 애플리케이션 정보 표시:

`flatpak info {{com.example.app}}`
