# timedLyricsCreator.py
Synchronize embedded lyrics in mp3 songs with a push of a button.  :musical_note:


## What does it do.

This python program is used to synchronize embedded lyrics in mp3 songs.

## How to use it.

Download timedLyricsCreator.py and put it in a folder.

In the same folder add all the mp3 (with the lyrics embedded as id3 tag) you wish to work with.

Once the program is launched it will ask you which songs you want to work with.
As the song starts to play, all you need to do is press `Enter` at the right moment as the singer sings the following verse of the lyrics.

If you've messed up with timing and you wish to try again type `r` and press `Enter`. This will prompt you to repeat the current song.

When the procedure is over, lyrics are injected automatically into the corresponding song.

## Dependencies.

Make sure you have installed all the dependecies first.

Install them with:
`pip install python-vlc` and 
`pip install music-tag`
