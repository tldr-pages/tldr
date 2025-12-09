# xwinwrap

> 플레이어나 프로그램을 데스크탑 배경으로 실행.
> 더 많은 정보: <https://github.com/ujjwal96/xwinwrap>.

- mpv를 사용하여 비디오 실행:

`xwinwrap -b -nf -ov -- {{mpv}} -wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{경로/대상/비디오.mp4}}`

- mpv를 사용하여 전체 화면으로 비디오 실행:

`xwinwrap -b -nf -fs -ov -- {{mpv}} -wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{경로/대상/비디오.mp4}}`

- mpv를 사용하여 80% 투명도로 비디오 실행:

`xwinwrap -b -nf -ov -o 0.8 --- {{mpv}} -wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{경로/대상/비디오.mp4}}`

- mpv를 사용하여 두 번째 모니터에 1600x900 크기로 X축 1920 오프셋으로 비디오 실행:

`xwinwrap -g 1600x900+1920 -b -nf -ov -- {{mpv}} -wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{경로/대상/비디오.mkv}}`
