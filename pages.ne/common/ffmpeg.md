# ffmpeg

> भिडियो रूपान्तरण उपकरण.
> थप जानकारी: <https://ffmpeg.org>.

-भिडियोबाट ध्वनि निकाल्नुहोस् र MP3 को रूपमा सेभ गर्नुहोस:

`ffmpeg -i {{video.mp4}} -vn {{sound}}.mp3`

-भिडियोको उचाइ 1000px मा स्केल गर्दै र फ्रेमरेटलाई 15 राखेर GIF को रूपमा सेभ गर्नुहोस :

`ffmpeg -i {{video.mp4}} -vf 'scale=-1:{{1000}}' -r {{15}} {{output.gif}}`

- अंकित छविहरूलाइ(`frame_1.jpg`, `frame_2.jpg`, आदि) भिडियो वा GIF मा जोड्नुहोस:

`ffmpeg -i {{frame_%d.jpg}} -f image2 {{video.mpg|video.gif}}`

-भिडियोको mm:ss बाट एकल फ्रेम निकाल्नुहोस् र यसलाई 128x128 रिजोल्युसन छविको रूपमा सेभ गर्नुहोस् :

`ffmpeg -ss {{mm:ss}} -i {{video.mp4}} -frames 1 -s {{128x128}} -f image2 {{image.png}}`

- दिइएको सुरु समय mm:ss देखि अन्त्यसमय mm2:ss2 सम्म भिडियोलाइ काट्नुहोस (अन्त्य सम्म नै  काट्नलाई  -to फ्ल्याग हटाउनुहोस्):

`ffmpeg -ss {{mm:ss}} -to {{mm2:ss2}} -i {{video.mp4}} -codec copy {{output.mp4}}`

- AVI भिडियोलाई MP4 मा रूपान्तरण गर्नुहोस्। अडियोको 128kbit बिटरेट राखेर AAC मा ,भिडियोको CRF 23 राखेर h264 मा :

`ffmpeg -i {{input_video}}.avi -codec:audio aac -b:audio 128k -codec:video libx264 -crf 23 {{output_video}}.mp4`

- MKV भिडियोको अडियो वा भिडियो स्ट्रिमहरू पुन: एन्कोडिङ नगरी हानिरहित ढाँचामा MP4 मा बदल्नुहोस :

`ffmpeg -i {{input_video}}.mkv -codec copy {{output_video}}.mp4`

- MP4 भिडियोलाई VP9 कोडेकमा रूपान्तरण गर्नुहोस्। उत्कृष्ट गुणस्तरको लागि, CRF फ्ल्यागको प्रयोग गर्नुहोस् (सिफारिस गरिएको दायरा 15-35) र -b:video 0 पनि प्रयोग गर्नुहोस् :

`ffmpeg -i {{input_video}}.mp4 -codec:video libvpx-vp9 -crf {{30}} -b:video 0 -codec:audio libopus -vbr on -threads {{number_of_threads}} {{output_video}}.webm`
