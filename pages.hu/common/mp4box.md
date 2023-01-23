# mp4box

> MPEG-4 Systems Toolbox - Muxolja a streameket MP4 konténerbe. További információ: <https://gpac.wp.imt.fr/mp4box>.

- Megjeleníti a meglévő MP4 fájlra vonatkozó információkat:

`mp4box -info {{path/to/file}}`

- SRT feliratfájl hozzáadása egy MP4 fájlhoz:

`mp4box -add {{input_subs.srt}}:lang=eng -add {{input.mp4}} {{output.mp4}}`

- Egy fájlból származó hang és egy másik fájlból származó videó kombinálása:

`mp4box -add {{input1.mp4}}#audio -add {{input2.mp4}}#video {{output.mp4}}`
