# yt-dlp

> A youtube-dl fork további funkciókkal és javításokkal. Videók letöltése a YouTube-ról és más weboldalakról. További információ: <https://github.com/yt-dlp/yt-dlp>.

- Videó vagy lejátszási lista letöltése (az alábbi parancs alapértelmezett beállításaival):

`yt-dlp "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Videó letöltése egy meghatározott formátumban, ebben az esetben a legjobb elérhető mp4 videót (alapértelmezett "bv\*+ba/b"):

`yt-dlp --format "{{bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]}}" "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Hang kivonása a videókból (szükséges ffmpeg vagy ffprobe):

`yt-dlp --extract-audio "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- A kinyert hang formátumának megadása (az alapértelmezett a "best"):

`yt-dlp --extract-audio --audio-format {{mp3}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- A kinyert hang hangminőségének megadása (0 (legjobb) és 10 (legrosszabb) között, alapértelmezett = 5):

`yt-dlp --extract-audio --audio-format {{mp3}} --audio-quality {{0}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- A YouTube-csatorna/felhasználó összes lejátszási listájának letöltése, minden egyes lejátszási listát külön könyvtárban tartva:

`yt-dlp -o "{{%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s}}" "{{https://www.youtube.com/user/TheLinuxFoundation/playlists}}"`

- Az Udemy kurzus letöltése, minden fejezetet külön könyvtárban tartva az otthoni MyVideos könyvtár alatt:

`yt-dlp -u {{user}} -p {{password}} -P "{{~/MyVideos}}" -o "{{%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s}}" "{{https://www.udemy.com/java-tutorial}}"`

- A teljes sorozat évad letöltése, minden sorozat és minden évad külön könyvtárban tartása a C:/MyVideos alatt:

`yt-dlp -P "{{C:/MyVideos}}" -o "{{%(series)s/%(season_number)s - %(season)s/%(episode_number)s - %(episode)s.%(ext)s}}" "{{https://videomore.ru/kino_v_detalayah/5_sezon/367617}}"`
