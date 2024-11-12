# dmesg

> कर्नेल संदेशों को `stdout` पर लिखें।
> अधिक जानकारी: <https://www.unix.com/man-page/sunos/1m/dmesg>।

- कर्नेल संदेश दिखाएं:

`dmesg`

- इस सिस्टम पर कितनी भौतिक मेमोरी उपलब्ध है दिखाएं:

`dmesg | grep -i memory`

- कर्नेल संदेश 1 पृष्ठ में एक बार दिखाएं:

`dmesg | less`
