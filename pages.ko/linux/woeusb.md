# woeusb

> Windows 미디어 생성 도구.
> 더 많은 정보: <https://manned.org/woeusb>.

- USB를 포맷하고 부팅 가능한 Windows 설치 드라이브 생성:

`woeusb --device {{경로/대상/windows.iso}} {{/dev/sdX}}`

- USB 저장 장치의 기존 파티션에 Windows 파일을 복사하고 부팅 가능하게 만들기 (현재 데이터 삭제 없이):

`woeusb --partition {{경로/대상/windows.iso}} {{/dev/sdXN}}`
