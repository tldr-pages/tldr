# timg

> Display images, GIFs, PDFs, and videos directly in the terminal.
> Supports multiple protocols (sixel, iTerm2, kitty, etc.).
> More information: <https://github.com/hzeller/timg>.

- Show an image in the terminal:
`timg {{path/to/image.png}}`

- Show multiple images sequentially:
`timg {{image1.jpg}} {{image2.jpg}}`

- Display images in a grid layout:
`timg --grid {{columns}} {{image1.jpg}} {{image2.jpg}} {{image3.jpg}}`

- Play an animated GIF:
`timg {{animation.gif}}`

- Play a video file:
`timg {{video.mp4}}`

- Read image/video filenames from a text file:
`timg --filelist {{list.txt}}`