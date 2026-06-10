# ffprobe

> Մուլտիմեդիա հոսքի անալիզատոր:.
> Լրացուցիչ տեղեկություններ. <https://ffmpeg.org/ffprobe.html>:.

- Ցուցադրել բոլոր հասանելի հոսքային տեղեկությունները մեդիա ֆայլի համար.:

`ffprobe {{[-v|-loglevel]}} error -show_streams {{input.mp4}}`

- Ցուցադրել լրատվամիջոցների տևողությունը.:

`ffprobe {{[-v|-loglevel]}} error -show_entries format=duration {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Ցուցադրել տեսանյութի կադրերի արագությունը.:

`ffprobe {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream=avg_frame_rate {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Ցուցադրել տեսանյութի լայնությունը կամ բարձրությունը.:

`ffprobe {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream={{width|height}} {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Ցուցադրել տեսանյութի միջին բիթային արագությունը.:

`ffprobe {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream=bit_rate {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{input.mp4}}`
