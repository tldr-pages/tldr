# yt-dlp

> YouTube-dl պատառաքաղ՝ լրացուցիչ հնարավորություններով և ուղղումներով:.
> Ներբեռնեք տեսանյութեր YouTube-ից և այլ կայքերից:.
> Տես նաև՝ `ytfzf`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/yt-dlp/yt-dlp#usage-and-options>:.

- Ներբեռնեք տեսահոլովակ կամ երգացանկ (ստորև բերված հրամանի լռելյայն ընտրանքներով).:

`yt-dlp "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Թվարկեք տեսանյութի համար հասանելի ներբեռնվող ձևաչափերը.:

`yt-dlp {{[-F|--list-formats]}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Ներբեռնեք տեսանյութ կամ երգացանկ՝ օգտագործելով հասանելի լավագույն MP4 տեսանյութը (կանխադրվածը «bv\*+ba/b» է):

`yt-dlp {{[-f|--format]}} "{{bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]}}" "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Հանեք աուդիո տեսանյութից (պահանջվում է ffmpeg կամ ffprobe).:

`yt-dlp {{[-x|--extract-audio]}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Նշեք արդյունահանված ձայնի աուդիո ձևաչափը և ձայնի որակը (0 (լավագույն) և 10 (վատագույն) միջև, լռելյայն = 5):

`yt-dlp {{[-x|--extract-audio]}} --audio-format {{mp3}} --audio-quality {{0}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Ներբեռնեք երգացանկի միայն երկրորդ, չորրորդ, հինգերորդ, վեցերորդ և վերջին տարրերը (առաջին կետը 1 է, ոչ թե 0):

`yt-dlp {{[-I|--playlist-items]}} 2,4:6,-1 "{{https://youtube.com/playlist?list=PLbzoR-pLrL6pTJfLQ3UwtB-3V4fimdqnA}}"`

- Ներբեռնեք YouTube ալիքի/օգտատիրոջ բոլոր երգացանկերը, որոնք յուրաքանչյուր երգացանկը պահում են առանձին գրացուցակում.:

`yt-dlp {{[-o|--output]}} "{{%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s}}" "{{https://www.youtube.com/user/TheLinuxFoundation/playlists}}"`

- Ներբեռնեք Udemy դասընթաց՝ յուրաքանչյուր գլուխ պահելով առանձին գրացուցակում.:

`yt-dlp {{[-u|--username]}} {{user}} {{[-p|--password]}} {{password}} {{[-P|--paths]}} "{{path/to/directory}}" {{[-o|--output]}} "{{%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s}}" "{{https://www.udemy.com/java-tutorial}}"`
