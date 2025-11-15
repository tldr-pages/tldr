# update-alternatives

> 심볼릭 링크를 편리하게 관리하여 기본 명령을 결정합니다.
> 더 많은 정보: <https://manned.org/update-alternatives>.

- 심볼릭 링크 추가:

`sudo update-alternatives --install {{경로/대상/심볼릭링크}} {{명령_이름}} {{경로/대상/명령_바이너리}} {{우선순위}}`

- `java`에 대한 심볼릭 링크 구성:

`sudo update-alternatives --config {{java}}`

- 심볼릭 링크 제거:

`sudo update-alternatives --remove {{java}} {{/opt/java/jdk1.8.0_102/bin/java}}`

- 지정된 명령에 대한 정보 표시:

`update-alternatives --display {{java}}`

- 모든 명령과 현재 선택된 항목 표시:

`update-alternatives --get-selections`
