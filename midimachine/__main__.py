from midimachine.classes import MidiMachine
from midimachine.statics import KeyToMidi, Mood


x = MidiMachine(root_note=KeyToMidi.A3, bpm=128)
x.draw_progression(mood=Mood.Happy)
