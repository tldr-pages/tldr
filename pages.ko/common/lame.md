# lame

> WAV 파일을 MP3 파일로 인코딩.
> 더 많은 정보: <https://svn.code.sf.net/p/lame/svn/trunk/lame/USAGE>.

- CBR 320kbps를 사용하여 오디오 파일을 MP3로 인코딩:

`lame -b 320 {{경로/대상/파일}}.wav {{경로/대상/출력파일}}.mp3`

- V0 프리셋을 사용하여 오디오 파일을 MP3로 인코딩:

`lame -V 0 {{경로/대상/파일}}.wav {{경로/대상/출력파일}}.mp3`

- 오디오 파일을 AAC 형식으로 인코딩:

`lame {{경로/대상/파일}}.wav {{경로/대상/출력파일}}.aac`
