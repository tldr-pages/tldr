# mp4box

> MPEG-4 Systems Toolbox. muxe-ը հոսում է MP4 կոնտեյների մեջ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/gpac/gpac/wiki/Fragmentation,-segmentation,-splitting-and-interleaving>:.

- Ցուցադրել առկա MP4 ֆայլի մասին տեղեկատվություն.:

`mp4box -info {{path/to/file}}`

- Ավելացնել SRT ենթավերնագիր ֆայլ MP4 ֆայլի մեջ.:

`mp4box -add {{input_subs.srt}}:lang=eng -add {{input.mp4}} {{output.mp4}}`

- Միավորել աուդիոն մեկ ֆայլից և տեսանյութը մյուսից.:

`mp4box -add {{input1.mp4}}#audio -add {{input2.mp4}}#video {{output.mp4}}`
