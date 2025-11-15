# ffmpeg

> 動画変換ツールです。
> もっと詳しく: <https://ffmpeg.org/ffmpeg.html#Options>。

- ビデオからサウンドを抽出し、MP3 として保存:

`ffmpeg -i {{path/to/video.mp4}} -vn {{path/to/sound.mp3}}`

- FLAC ファイルを Red Book CD フォーマット（44100kHz、16bit）にトランスコード:

`ffmpeg -i {{path/to/input_audio.flac}} -ar 44100 -sample_fmt s16 {{path/to/output_audio.wav}}`

- ビデオを GIF として保存する。高さを 1000px に拡大縮小し、フレームレートを 15 に設定:

`ffmpeg -i {{path/to/video.mp4}} {{[-vf|-filter:v]}} 'scale=-1:{{1000}}' -r {{15}} {{path/to/output.gif}}`

- 番号付けされた画像（`frame_1.jpg`, `frame_2.jpg` など）を動画または GIF に結合:

`ffmpeg -i {{path/to/frame_%d.jpg}} -f image2 {{video.mpg|video.gif}}`

- 指定した開始時刻 mm:ss から終了時刻 mm2:ss2 までの動画をトリミング (最後までトリミングするには -to フラグを省略):

`ffmpeg -i {{path/to/input_video.mp4}} -ss {{mm:ss}} -to {{mm2:ss2}} {{[-c|-codec]}} copy {{path/to/output_video.mp4}}`

- AAC Audio @ 128kbit、 h264 Video @ CRF 23 の設定で、 AVI 動画を MP4 に変換:

`ffmpeg -i {{path/to/input_video}}.avi {{[-c|-codec]}}:a aac -b:a 128k {{[-c|-codec]}}:v libx264 -crf 23 {{path/to/output_video}}.mp4`

- 音声やビデオストリームを再エンコードせずに、MKV ビデオを MP4 にリマックスする:

`ffmpeg -i {{path/to/input_video}}.mkv {{[-c|-codec]}} copy {{path/to/output_video}}.mp4`

- MP4 ビデオを VP9 コーデックに変換する。最高の画質を得るには、CRF 値（推奨範囲 15-35）を使用し、-b:v は 0 でなければならない:

`ffmpeg -i {{path/to/input_video}}.mp4 {{[-c|-codec]}}:v libvpx-vp9 -crf {{30}} -b:v 0 {{[-c|-codec]}}:a libopus -vbr on -threads {{number_of_threads}} {{path/to/output_video}}.webm`
