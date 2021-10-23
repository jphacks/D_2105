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

from instruments import Instruments, DrumInstruments


def append_notes(notes,input_notes_list,raise_key = 0,sift_start = 0):
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
        velocity, code, start_time, end_time = i
        pitch = pm.note_name_to_number(code) + raise_key
        start = start_time + sift_start
        end = end_time + sift_start
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
    piano = pm.Instrument(Instruments.ACOSTIC_GRAND_PIANO)
    default_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,26) #Happy Birthday to you
    ]
    append_notes(notes = piano.notes, input_notes_list = default_melody_notes_list)
    instruments_list.append(piano)


def create_great_ocean_main_melody(instruments_list):
    """
    パラメータが海で、かつ大海原に該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    violin = pm.Instrument(Instruments.VIOLIN)
    great_ocean_melody_notes_list = \
    [
        (90,'C4',2,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,18),(95,'E4',18,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,26) #Happy Birthday to you
    ]
    append_notes(notes = violin.notes, input_notes_list = great_ocean_melody_notes_list)
    instruments_list.append(violin)


def create_summer_beach_melody(instruments_list):
    """
    パラメータが海で、かつ、真夏のビーチに該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    steel_drum = pm.Instrument(Instruments.STEEL_DRUMS)
    summer_beach_melody_notes_list = \
    [
        (90,'C4',2,2.25),(90,'C4',2.25,2.5),(100,'D4',2.5,2.75),(100,'C4',3,3.25),(100,'F4',3.5,3.75),(100,'E4',4,4.25), #Happy Birthday to you
        (90,'C4',6,6.25),(90,'C4',6.25,6.5),(100,'D4',6.5,6.75),(100,'C4',7,7.25),(100,'G4',7.5,7.75),(100,'F4',8,8.25), #Happy Birthday to you
        (90,'C4',10,10.25),(90,'C4',10.25,10.5),(100,'C5',10.5,10.75),(100,'A4',11,11.25),(100,'F4',11.5,11.75),(100,'F4',11.75,12),(95,'E4',12,12.25),(95,'E4',12.25,12.5),(90,'D4',12.75,13), #Happy Birthday dear ??
        (100,'A#4',14,14.25),(100,'A#4',14.25,14.5),(100,'A4',14.5,14.75),(100,'F4',15,15.25),(100,'G4',15.5,15.75),(100,'F4',16,16.25) #Happy Birthday to you
    ]
    append_notes(notes = steel_drum.notes, input_notes_list = summer_beach_melody_notes_list)
    instruments_list.append(steel_drum)


def create_moderate_beach_melody(instruments_list):
    """
    パラメータが海で、かつ、閑散期の静かなビーチに該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    vibraphone = pm.Instrument(Instruments.VIBRAPHONE)
    moderate_beach_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,26) #Happy Birthday to you
    ]
    append_notes(notes = vibraphone.notes, input_notes_list = moderate_beach_melody_notes_list)
    instruments_list.append(vibraphone)


def create_cherry_melody(instruments_list):
    """
    パラメータが桜に該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    organ = pm.Instrument(Instruments.DRAWBER_ORGAN)
    cherry_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',27,27.75),(100,'A#4',27.75,28),(100,'A4',28,29),(100,'F4',29,30),(100,'G4',31,32),(100,'F4',33,39) #Happy Birthday to you
    ]
    append_notes(notes = organ.notes, input_notes_list = peach_melody_notes_list)
    instruments_list.append(organ)


def create_cat_melody(instruments_list):
    """
    パラメータが猫に該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    orchestra_hit = pm.Instrument(Instruments.ORCHESTRA_HIT)
    cat_melody_notes_list = \
    [
        (90,'C4',2,2.25),(90,'C4',2.25,2.5),(100,'D4',2.5,2.75),(100,'C4',3,3.25),(100,'F4',3.5,3.75),(100,'E4',4,4.25), #Happy Birthday to you
        (90,'C4',6,6.25),(90,'C4',6.25,6.5),(100,'D4',6.5,6.75),(100,'C4',7,7.25),(100,'G4',7.5,7.75),(100,'F4',8,8.25), #Happy Birthday to you
        (90,'C4',10,10.25),(90,'C4',10.25,10.5),(100,'C5',10.5,10.75),(100,'A4',11,11.25),(100,'F4',11.5,11.75),(100,'F4',11.75,12),(95,'E4',12,12.25),(95,'E4',12.25,12.5),(90,'D4',12.75,13), #Happy Birthday dear ??
        (100,'A#4',14,14.25),(100,'A#4',14.25,14.5),(100,'A4',14.5,14.75),(100,'F4',15,15.25),(100,'G4',15.5,15.75),(100,'F4',16,17) #Happy Birthday to you
    ]
    append_notes(notes = orchestra_hit.notes, input_notes_list = cat_melody_notes_list)
    instruments_list.append(orchestra_hit)


def create_tropical_melody(instruments_list):
    """
    パラメータが南国に該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    xylophone = pm.Instrument(Instruments.XYLOPHONE)
    tropical_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,26) #Happy Birthday to you
    ]
    append_notes(notes = xylophone.notes, input_notes_list = tropical_melody_notes_list)
    instruments_list.append(xylophone)


def create_chunibyo_melody(instruments_list):
    """
    パラメータが厨二病に該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    trumpet = pm.Instrument(Instruments.TRUMPET)
    chunibyo_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,26) #Happy Birthday to you
    ]
    append_notes(notes = trumpet.notes, input_notes_list = chunibyo_melody_notes_list)
    instruments_list.append(trumpet)


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
        #でバックよう
        create_great_ocean_main_melody(instruments_list)
    elif prime_value == 'cherry':
        create_cherry_melody(instruments_list)
    elif prime_value == 'cat':
        cat_melody_notes_list(instruments_list)
    elif prime_value == 'dog':
        hoge = 'a'
    elif prime_value == 'train':
        hoge = 'a'
    elif prime_value == 'pc':
        hoge = 'a'
    elif prime_value == 'gourmet':
        hoge = 'a'
    elif prime_value == 'sport':
        hoge = 'a'
    elif prime_value == 'soccer':
        hoge = 'a'
    elif prime_value == 'baseball':
        hoge = 'a'
    elif prime_value == 'tabletennis':
        hoge = 'a'
    elif prime_value == 'japanese':
        hoge = 'a'
    elif prime_value == 'scandinavian':
        hoge = 'a'
    elif prime_value == 'tropical':
        tropical_melody_notes_list(instruments_list)
    elif prime_value == 'school':
        hoge = 'a'
    elif prime_value == 'idol':
        hoge = 'a'
    elif prime_value == 'outdoor':
        hoge = 'a'
    elif prime_value == 'car':
        hoge = 'a'
    elif prime_value == 'drama':
        hoge = 'a'
    elif prime_value == 'picture':
        hoge = 'a'
    elif prime_value == 'rock':
        hoge = 'a'
    elif prime_value == 'hiphop':
        hoge = 'a'
    elif prime_value == 'electronic':
        hoge = 'a'
    elif prime_value == 'jazz':
        hoge = 'a'
    elif prime_value == 'ghost':
        hoge = 'a'
    elif prime_value == 'sword':
        hoge = 'a'
    elif prime_value == 'gun':
        hoge = 'a'
    elif prime_value == 'history':
        hoge = 'a'
    elif prime_value == 'chuni':
        hoge = 'a'
    elif prime_value == 'fairy':
        hoge = 'a'
    elif prime_value == 'child':
        hoge = 'a'
    elif prime_value == 'mystery':
        hoge = 'a'
    elif prime_value == 'shopping':
        hoge = 'a'
    else:
        create_default_main_melody(instruments_list)


def midi_to_mp3(inputFileName):
	fs = FluidSynth('soundFont/MuseScore_General.sf3') #サウンドフォントを指定
	fs.midi_to_audio(inputFileName, 'sample.wav') #midiをmp3に変換、保存


def create_music(related_value_list):
    """
    入力されたパラメータを基に曲を作成する

    Parameters
    ----------
    related_value_list : [str]
        言語分析の結果を格納したリスト
    """

    NO_ITEM   = 0
    ONE_ITEMS = 1
    TWO_ITEMS = 2

    prime_value = 'none'
    secondary_value = 'none'
    third_value = 'none'

    tempo = 200 #曲のテンポ。可変
    PM = pm.PrettyMIDI() #Pretty_MIDIオブジェクトの生成

    if len(related_value_list)   == NO_ITEM:
        prime_value = 'none'
        secondary_value = 'none'
        third_value = 'none'
    elif len(related_value_list) == ONE_ITEMS:
        prime_value     = related_value_list[0]
    elif len(related_value_list) == TWO_ITEMS:
        prime_value     = related_value_list[0]
        secondary_value = related_value_list[1]
    else:
        prime_value     = related_value_list[0]
        secondary_value = related_value_list[1]
        third_value     = related_value_list[2]

    create_main_melody(PM.instruments,prime_value,secondary_value)
    PM.write('sample.mid')
    mid = MidiFile('sample.mid')
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(MetaMessage('set_tempo',tempo=mido.bpm2tempo(tempo)))
    mid.save('sample2.mid')
    os.remove('sample.mid')
    midi_to_mp3('sample2.mid')