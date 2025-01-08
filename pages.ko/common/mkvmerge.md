# mkvmerge

> 멀티미디어 스트림을 병합하고 추출.
> 더 많은 정보: <https://mkvtoolnix.download/doc/mkvmerge.html>.

- Matroska 파일 정보 표시:

`mkvmerge --identify {{경로/대상/파일.mkv}}`

- 특정 파일의 트랙 1에서 오디오 추출:

`mkvextract tracks {{경로/대상/파일.mkv}} {{1}}:{{경로/대상/출력.webm}}`

- 특정 파일의 트랙 3에서 자막 추출:

`mkvextract tracks {{경로/대상/파일.mkv}} {{3}}:{{경로/대상/자막.srt}}`

- 파일에 자막 트랙 추가:

`mkvmerge --output {{경로/대상/출력.mkv}} {{경로/대상/파일.mkv}} {{경로/대상/자막.srt}}`
