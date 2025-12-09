# mp4box

> MPEG-4 시스템 도구: 스트림을 MP4 컨테이너에 멀티플렉싱.
> 더 많은 정보: <https://gpac.wp.imt.fr/mp4box>.

- 기존 MP4 파일에 대한 정보 표시:

`mp4box -info {{경로/대상/파일}}`

- MP4 파일에 SRT 자막 파일 추가:

`mp4box -add {{입력_자막.srt}}:lang=eng -add {{입력.mp4}} {{출력.mp4}}`

- 한 파일에서 오디오와 다른 파일에서 비디오 결합:

`mp4box -add {{입력1.mp4}}#audio -add {{입력2.mp4}}#video {{출력.mp4}}`
