# ffmpeg

> Ferramenta de conversão de vídeo.
> Mais informações: <https://ffmpeg.org>.

- Extrair o som de um vídeo e salvá-lo como MP3:

`ffmpeg -i {{vídeo}} -vn {{som}}.mp3`

- Converter quadros de um vídeo ou GIF para imagens numeradas individuais:

`ffmpeg -i {{vídeo|gif}} {{quadro_%d.png}}`

- Combinar imagens numeradas (`quadro_1.jpg`, `quadro_2.jpg`, etc) em um vídeo ou GIF:

`ffmpeg -i {{quadro_%d.jpg}} -f image2 {{vídeo|gif}}`

- Extrair um único quadro de um vídeo no tempo mm:ss e salvá-lo como uma imagem de resolução 128x128:

`ffmpeg -ss {{mm:ss}} -i {{vídeo}} -frames 1 -s {{128x128}} -f image2 {{quadro.png}}`

- Cortar um vídeo de um dado tempo inicial mm:ss até um tempo final mm2:ss2 (omita a opção -to para cortar o vídeo até o final):

`ffmpeg -ss {{mm:ss}} -to {{mm2:ss2}} -i {{vídeo_entrada}} -codec copy {{vídeo_saída}}`

- Converter um vídeo AVI para MP4. AAC Áudio @ 128kbit, h264 Vídeo @ CRF 23:

`ffmpeg -i {{vídeo_entrada}}.avi -codec:audio aac -b:audio 128k -codec:video libx264 -crf 23 {{vídeo_saída}}.mp4`

- Remuxar um vídeo MKV para MP4 sem recodificar áudio ou vídeo:

`ffmpeg -i {{vídeo_entrada}}.mkv -codec copy {{vídeo_saída}}.mp4`

- Converter vídeo MP4 para o codec VP9. Para a melhor qualidade, use um valor CRF (faixa recomendada 15-35) e -b:video DEVE ser 0:

`ffmpeg -i {{vídeo_entrada}}.mp4 -codec:video libvpx-vp9 -crf {{30}} -b:video 0 -codec:audio libopus -vbr on -threads {{número_de_threads}} {{vídeo_saída}}.webm`
