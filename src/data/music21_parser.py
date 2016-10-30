import csv
from music21 import *

c = converter.parse('Sonate_No._14_Moonlight_3rd_Movement.xml')
# print(c)
# staff1 = c[4].elements
# staff2 = c[5].elements

# staff1 = c[4].getElementsByClass(stream.Measure).elements
# print(staff1measure[193].elements)
# print(staff1measure[0].getElementsByClass(note.Note)[0].__dict__)

# '_activeSiteStoredOffset'


FIELDNAMES = ['instrument', 'staff', 'measureNumber', 'offset', 'duration', 'frequency', 'step', 'octave']
OUT_DICT = dict()
OUT_FILE = open('moonlight.csv', 'w')

csvwriter = csv.DictWriter(OUT_FILE, fieldnames=FIELDNAMES, extrasaction='ignore')
csvwriter.writeheader()

for staff in c.parts:
    OUT_DICT['instrument'] = staff.getInstrument().instrumentName
    for note in staff.recurse().notesAndRests.stream():
        OUT_DICT['measureNumber'] = note.measureNumber
        OUT_DICT['offset'] = note.offset
        OUT_DICT['duration'] = note.duration.quarterLength
        if(note.isNote):
            OUT_DICT['frequency'] = note.pitch.frequency
            OUT_DICT['step'] = note.step
            OUT_DICT['octave'] = note.octave
            csvwriter.writerow(OUT_DICT)
        elif(note.isRest):
            OUT_DICT['frequency'] = 0.0
            csvwriter.writerow(OUT_DICT)
        elif(note.isChord):
            for p in note.pitches:
                OUT_DICT['frequency'] = p.frequency
                OUT_DICT['step'] = p.step
                OUT_DICT['octave'] = p.octave
                csvwriter.writerow(OUT_DICT)
        else:
            print(note)

# measure, offset, note,
