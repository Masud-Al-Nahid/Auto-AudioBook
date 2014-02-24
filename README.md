# Auto Audiobook

*Bot that reads various works of fiction and posts them on the internet*

This bot reads through works of fiction by selecting a range of lines and running those lines through 
[espeak](http://espeak.sourceforge.net/). It then uses an image of the author and the WAV output to create an MP4 video 
file which is uploaded to [Youtube](http://www.youtube.com/channel/UCedRPx3POGLFfIIaishqZTg) and after processing posted 
to [Twitter](https://twitter.com/auto_audiobook). Book texts downloaded from [Project Gutenberg](http://www.gutenberg.org/).

 * [@Auto_Audiobook](https://twitter.com/auto_audiobook)
 * [Auto Audiobook Youtube Channel](http://www.youtube.com/channel/UCedRPx3POGLFfIIaishqZTg)

**Dependencies**
 * [python-twitter](https://code.google.com/p/python-twitter/)
 * [Twitter API keys](https://dev.twitter.com/)
 * [Google API keys](https://code.google.com/apis)
 * Uses a modified version of the [sample Youtube upload script](https://developers.google.com/youtube/v3/code_samples/python) on Google's API site
