# MIDIMachine

## What?
Sometimes it's hard to find inspiration when making music.
A small nudge in the right direction can help, so I decided to create a basic MIDI chord progression generator!

## Setup?
For easy use, I recommend [LoopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html), the tool is built with LoopMIDI in mind.
Other adaptions are very much possible, but will require some code :-)
The rest of it is just `python-rtmidi` based, so as usual just run `pip3 install -r requirements.txt` in your venv to get going.

I'm using Ableton and "recording" captured MIDI notes after they've been played. 

## Usage?
Currently it isn't much of a tool, so after git cloning and setting up LoopMIDI, edit your `__main__.py` and run `python -m midimachine`. 

The default is:
```
x = MidiMachine(root_note=KeyToMidi.A3, bpm=128)
x.draw_progression(mood=Mood.Happy)
```

Obviously, using a fixed key and a fixed mood will repeatedly generate the same pattern.

The logic behind this is that the "mood" is determined by the progression.

If you look at `Mood.Happy` in the `statics.py`

`Happy = [0,3,4,0]`

This is simply a I,IV,V,I progression. (Note that there's no difference between Minor or Major as we're just picking notes and not chords.)

## Have fun!
Have some fun and let me know what you made with this, or as usual, create issues or PR's for features and bug fixes!

