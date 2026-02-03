# ffprobe

> マルチメディアストリームを解析します。
> もっと詳しく: <https://ffmpeg.org/ffprobe.html>。

- メディアファイルの利用可能なストリーム情報を全て表示:

`ffprobe {{[-v|-loglevel]}} error -show_streams {{input.mp4}}`

- メディアの継続時間(尺)を表示:

`ffprobe {{[-v|-loglevel]}} error -show_entries format=duration {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- 動画のフレームレートを表示:

`ffprobe {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream=avg_frame_rate {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- 動画の幅または高さを表示:

`ffprobe {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream={{width|height}} {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- 動画の平均ビットレートを表示:

`ffprobe {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream=bit_rate {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{input.mp4}}`
