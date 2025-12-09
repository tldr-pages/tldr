# ffplay

> FFmpeg 라이브러리와 SDL 라이브러리를 사용하는 간단하고 휴대 간으한 미디어 플레이어.
> 더 많은 정보: <https://ffmpeg.org/ffplay-all.html>.

- 미디어 파일 재생:

`ffplay {{경로/대상/파일}}`

- GUI 없이 미디어 파일에서 오디오 재생:

`ffplay -nodisp {{경로/대상/파일}}`

- `stdin`을 통해 `ffmpeg`에 의해 전달된 미디어 재생:

`ffmpeg -i {{경로/대상/파일}} -c {{copy}} -f {{미디어_포맷}} - | ffplay -`

- 실시간으로 비디오를 재생하고 모션 벡터를 표시:

`ffplay -flags2 +export_mvs -vf codecview=mv=pf+bf+bb {{경로/대상/파일}}`

- 비디오 키프레임만 표시:

`ffplay -vf select="{{eq(pict_type\,PICT_TYPE_I)}}" {{경로/대상/파일}}`
