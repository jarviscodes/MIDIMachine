import time
import rtmidi
import random
from midimachine.statics import Scale, KeyToMidi, NoteAction, RhythmFactor, Mood


class MidiMachine():
    def __init__(self, portname_contains:str ="LMP", root_note = KeyToMidi.E3, bpm=128):
        self.midi_out = rtmidi.MidiOut()
        self.all_machine_midi_ports = self.midi_out.get_ports()
        self.root_note = root_note
        self.bpm = bpm
        self.beat_time = (self.bpm/60) # == 1 beat
        self.allowed_rhythms = [RhythmFactor.half]

        if len(portname_contains) < 3:
            print("Can't use 'portname contains' with less than 3 characters. Skipping.")
            self.ask_port_id_from_user()
        else:
            for i in range(0,len(self.all_machine_midi_ports)):
                if portname_contains in self.all_machine_midi_ports[i]:
                    self.midi_out.open_port(i)
                    print(f"Opened port: {self.all_machine_midi_ports[i]}")
                else:
                    print(f"No port found with {portname_contains}")

    def ask_port_id_from_user(self):
        if not self.all_machine_midi_ports:
            print("No MIDI Ports found!")
            exit()

        print("Pick a midi port from the list below:")
        for i in range(0, len(self.all_machine_midi_ports)):
            print(f"[{i}] - {self.all_machine_midi_ports[i]}")
        target_port = int(input("Which Port? > "))
        self.midi_out.open_port(target_port)

    def generate_scale(self, scale):
        root_value = self.root_note
        scale_notes = [root_value]
        last_note = self.root_note
        for i in range(len(scale)):
            new_note = last_note + scale[i]
            scale_notes.append(new_note)
            last_note = new_note

        return scale_notes

    def _generate_minor_scale(self):
        root_value = self.root_note
        scale_notes = [root_value]
        last_note = self.root_note
        for i in range(len(Scale.minor)):
            new_note = last_note + Scale.minor[i]
            scale_notes.append(new_note)
            last_note = new_note

        return scale_notes

    def _generate_major_scale(self):
        root_value = self.root_note
        scale_notes = [root_value]
        last_note = self.root_note
        for i in range(len(Scale.major)):
            new_note = last_note + Scale.major[i]
            scale_notes.append(new_note)
            last_note = new_note

        return scale_notes

    def draw_progression(self, nbr_of_notes=4, scale=Scale.minor, mood=Mood.Happy):
        scale_notes = self.generate_scale(scale)
        selected_notes = []
        for i in range(0, nbr_of_notes):
            v = scale_notes[mood[i]]
            selected_notes.append(v)
        for x in selected_notes:
            on = NoteAction.note_on
            on[1] = x
            off = NoteAction.note_off
            off[1] = x
            self.midi_out.send_message(on)
            sleeptime = self.beat_time / random.choice(self.allowed_rhythms)
            time.sleep(sleeptime)
            self.midi_out.send_message(off)


    def spam_notes(self, nbr_of_notes=8):
        scale_notes = self.generate_scale(Scale.minor)
        # Select 32 Notes randomly
        selected_notes = []
        for i in range(0,nbr_of_notes):
            v = random.randint(0, len(scale_notes) - 1)
            selected_notes.append(scale_notes[v])

        for x in selected_notes:
            on = NoteAction.note_on
            on[1] = x
            off = NoteAction.note_off
            off[1] = x
            self.midi_out.send_message(on)
            sleeptime = self.beat_time / random.choice(self.allowed_rhythms)
            time.sleep(sleeptime)
            self.midi_out.send_message(off)

