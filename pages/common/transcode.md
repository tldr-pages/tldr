# transcode

> Video stream processing with huge number of options.

- remove shaking from videos

```
transcode -J stabilize -i {{source}}
transcode -J transform -i {{source}} -y xvid -o {{target}}
```

- video resizing

`transcode -Z 640x480 -i {{source}} -y xvid -o {{target}}`
