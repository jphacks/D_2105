# LICENSE
"""
# MuseScore_General.sf2
---

Current version: 0.2  13th May 2020

This is a scaled-down version of **MuseScore_General-HQ.sf2** that replaces some of the larger instruments to save memory and CPU on older PCs. This SoundFont is currently a work-in-progress. Detailed information on presets and sample sources used can be found in "MuseScore_General_Sample_Sources.csv". All instruments without attribution are still using samples from FluidR3Mono.

FluidR3 (original version) by Frank Wen Copyright (c) 2000-02

Mono conversion (FluidR3Mono) by Michael Cowgill Copyright (c) 2014-17

Adaptation for MuseScore_General.sf2 by S. Christian Collins Copyright (c) 2018-19

Temple Blocks instrument provided by Ethan Winer Copyright (c) 2002

Drumline Cymbals provided by Michael Schorsch Copyright (c) 2016

MuseScore_General.sf2 is shared under the MIT license as described in COPYING, as was FluidR3Mono and FluidR3 before it.
ftp://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/MuseScore_General_License.md

"""

"""
pretty_midi

Copyright (c) 2014 Colin Raffel

Released under the MIT License (MIT)
https://github.com/craffel/pretty-midi/blob/main/LICENSE.txt

"""

"""
midi2audio

Copyright (c) 2016 Bohumír Zámečník

Released under the MIT License (MIT)
https://github.com/bzamecnik/midi2audio/blob/master/LICENSE
"""

"""
mido

Copyright (c) 2013-infinity Ole Martin Bjørndalen

Released under the MIT License (MIT)
https://mido.readthedocs.io/en/latest/license.html

"""

import os

import pretty_midi as pm
from midi2audio import FluidSynth
import mido
from mido import MidiFile, MidiTrack, MetaMessage

import instruments


def append_notes(notes,input_notes_list,raise_key = 0):
    """
    引数のnotesにnotes_listの中身を追加する

    Parameters
    ----------
    notes : pretty_midi.Instrument.notes
        pretty_midi.Noteインスタンスを格納するリスト
    input_notes_list : list[tuple(velocity, pitch, start, end)]
        Noteインスタンス作成に使うパラメータ
    """
    for i in input_notes_list:
        velocity, code, start, end = i
        pitch = pm.note_name_to_number(code) + raise_key
        note = pm.Note(velocity = velocity, pitch = pitch, start = start, end = end)
        notes.append(note)


def create_default_main_melody(instruments_list):
    """
    パラメータがなかった場合の主旋律を作成

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    piano = pm.Instrument(instruments.Instruments.ACOSTIC_GRAND_PIANO)
    default_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,26) #Happy Birthday to you
    ]
    append_notes(notes = piano.notes, default_melody_notes_list)
    instruments_list.append(piano)


def create_main_melody(instruments_list, prime_value, secondary_value):
    """
    prime_valueに対応した主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    prime_value : str
        言語分析の結果、一番使用頻度の高かったパラメータ
    secondary_value : str
        言語分析の結果、二番目に使用頻度の高かったパラメータ
    """
    if prime_value == 'sea':
    elif prime_value == 'cherry':
    elif prime_value == 'cat':
    elif prime_value == 'dog':
    elif prime_value == 'train':
    elif prime_value == 'pc':
    elif prime_value == 'gourmet':
    elif prime_value == 'sport':
    elif prime_value == 'soccer':
    elif prime_value == 'baseball':
    elif prime_value == 'tabletennis':
    elif prime_value == 'japanese':
    elif prime_value == 'scandinavian':
    elif prime_value == 'tropical':
    elif prime_value == 'school':
    elif prime_value == 'idol':
    elif prime_value == 'outdoor':
    elif prime_value == 'car':
    elif prime_value == 'drama':
    elif prime_value == 'picture':
    elif prime_value == 'rock':
    elif prime_value == 'hiphop':
    elif prime_value == 'electronic':
    elif prime_value == 'jazz':
    elif prime_value == 'ghost':
    elif prime_value == 'sword':
    elif prime_value == 'gun':
    elif prime_value == 'history':
    elif prime_value == 'chuni':
    elif prime_value == 'fairy':
    elif prime_value == 'child':
    elif prime_value == 'mystery':
    elif prime_value == 'shopping':
    else:
        create_default_main_melody(instruments_list)



def create_music(value_list):
    """
    入力されたパラメータを基に曲を作成する

    Parameters
    ----------
    value_list : [str]
        言語分析の結果を格納したリスト
    """

    NO_ITEM = 0
    ONE_ITEMS = 1
    TWO_ITEMS = 2

    prime_value = 'none'
    secondary_value = 'none'
    third_value = 'none'

    tempo = 200 #曲のテンポ。可変
    PM = pm.PrettyMIDI() #Pretty_MIDIオブジェクトの生成

    if len(value_list)   == NO_ITEM:
    elif len(value_list) == ONE_ITEMS:
        prime_value     = value_list[0]
    elif len(value_list) == TWO_ITEMS:
        prime_value     = value_list[0]
        secondary_value = value_list[1]
    else:
        prime_value     = value_list[0]
        secondary_value = value_list[1]
        third_value     = value_list[2]

    create_main_melody(PM.instruments,prime_value)
    PM.write('sample.mid')
    mid = MidiFile('sample.mid')
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(MetaMessage('set_tempo',tempo=mido.bpm2tempo(tempo)))
    mid.save('sample2.mid')
    os.remove('sample.mid')