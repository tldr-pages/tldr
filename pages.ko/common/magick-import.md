# magick import

> X 서버 화면의 일부 또는 전체를 캡처하여 파일로 저장.
> 같이 보기: `magick`.
> 더 많은 정보: <https://imagemagick.org/script/import.php>.

- 전체 X 서버 화면을 PostScript 파일로 캡처:

`magick import -window root {{경로/대상/output.ps}}`

- 원격 X 서버 화면의 내용을 PNG 이미지로 캡처:

`magick import -window root -display {{remote_host}}:{{화면}}.{{디스플레이}} {{경로/대상/output.png}}`

- `xwininfo`로 표시된 ID를 가진 특정 창을 JPEG 이미지로 캡처:

`magick import -window {{window_id}} {{경로/대상/output.jpg}}`
