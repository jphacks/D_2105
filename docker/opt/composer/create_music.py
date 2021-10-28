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


def append_notes(notes,input_notes_list,raise_key = 0,sift_start = 0,raise_velocity = 0):
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
        velocity += raise_velocity
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
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,27) #Happy Birthday to you
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
        (100,'A#4',21,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,27) #Happy Birthday to you
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
    append_notes(notes = organ.notes, input_notes_list = cherry_melody_notes_list)
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


def create_dog_melody(instruments_list):
    """
    パラメータが犬に該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    xylophone = pm.Instrument(Instruments.XYLOPHONE)
    dog_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,6.125),(100,'E4',6.125,6.25),(100,'E4',6.25,6.375),(100,'E4',6.375,6.5),(100,'E4',6.5,6.625),(100,'E4',6.625,6.75),(100,'E4',6.75,6.875),(100,'E4',6.875,7),(100,'E4',7,7.125),(100,'E4',7.125,7.25),(100,'E4',7.25,7.375),(100,'E4',7.375,7.5),(100,'E4',7.5,7.625),(100,'E4',7.625,7.75),(100,'E4',7.75,7.875),(100,'E4',7.875,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,12.125),(100,'F4',12.125,12.25),(100,'F4',12.25,12.375),(100,'F4',12.375,12.5),(100,'F4',12.5,12.625),(100,'F4',12.625,12.75),(100,'F4',12.75,12.875),(100,'F4',12.875,13),(100,'F4',13,13.125),(100,'F4',13.125,13.25),(100,'F4',13.25,13.375),(100,'F4',13.375,13.5),(100,'F4',13.5,13.625),(100,'F4',13.625,13.75),(100,'F4',13.75,13.875),(100,'F4',13.875,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,19.125),(100,'D4',19.125,19.25),(100,'D4',19.25,19.375),(100,'D4',19.375,19.5),(100,'D4',19.5,19.625),(100,'D4',19.625,19.75),(100,'D4',19.75,19.875),(100,'D4',19.875,20),(100,'D4',20,20.125),(100,'D4',20.125,20.25),(100,'D4',20.25,20.375),(100,'D4',20.375,20.5),(100,'D4',20.5,20.625),(100,'D4',20.625,20.75),(100,'D4',20.75,20.875),(100,'D4',20.875,21), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,25.125),(100,'F4',25.125,25.25),(100,'F4',25.25,25.375),(100,'F4',25.375,25.5),(100,'F4',25.5,25.625),(100,'F4',25.625,25.75),(100,'F4',25.75,25.875),(100,'F4',25.875,26),(100,'F4',26,26.125),(100,'F4',26.125,26.25),(100,'F4',26.25,26.375),(100,'F4',26.375,26.5),(100,'F4',26.5,26.625),(100,'F4',26.625,26.75),(100,'F4',26.75,26.875),(100,'F4',26.875,27) #Happy Birthday to you
    ]
    append_notes(notes = xylophone.notes, input_notes_list = dog_melody_notes_list, raise_key = 12)
    instruments_list.append(xylophone)


def create_PC_melody(instruments_list):
    """
    パラメータがPCに該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    synth_bass1 = pm.Instrument(Instruments.SYNTH_BASS_1)
    PC_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,27) #Happy Birthday to you
    ]
    append_notes(notes = synth_bass1.notes, input_notes_list = PC_melody_notes_list)
    instruments_list.append(synth_bass1)


def create_sport_melody(instruments_list):
    """
    パラメータがスポーツに該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    trombone = pm.Instrument(Instruments.TROMBONE)
    trumpet = pm.Instrument(Instruments.TRUMPET)
    baseball_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,27) #Happy Birthday to you
    ]
    append_notes(notes = trombone.notes, input_notes_list = baseball_melody_notes_list, raise_key = -12)
    append_notes(notes = trumpet.notes, input_notes_list = baseball_melody_notes_list)
    instruments_list.append(trombone)
    instruments_list.append(trumpet)


def create_soccer_melody(instruments_list):
    """
    パラメータがサッカーに該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    brass_ensemble = pm.Instrument(Instruments.BRASS_SECTION)
    soccer_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,27) #Happy Birthday to you
    ]
    append_notes(notes = brass_ensemble.notes, input_notes_list = soccer_melody_notes_list)
    instruments_list.append(brass_ensemble)


def create_baseball_melody(instruments_list):
    """
    パラメータが野球に該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    trombone = pm.Instrument(Instruments.TROMBONE)
    trumpet = pm.Instrument(Instruments.TRUMPET)
    baseball_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,27) #Happy Birthday to you
    ]
    append_notes(notes = trombone.notes, input_notes_list = baseball_melody_notes_list, raise_key = -12)
    append_notes(notes = trumpet.notes, input_notes_list = baseball_melody_notes_list)
    instruments_list.append(trombone)
    instruments_list.append(trumpet)


def create_baseball_melody(instruments_list):
    """
    パラメータがアイドルで、かつ、真夏のビーチに該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    brass_ensemble = pm.Instrument(Instruments.BRASS_SECTION)
    baseball_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,27) #Happy Birthday to you
    ]
    append_notes(notes = brass_ensemble.notes, input_notes_list = baseball_melody_notes_list)
    instruments_list.append(brass_ensemble)


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
    

def create_school_melody(instruments_list):
    """
    パラメータが学校に該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    electric_guitar = pm.Instrument(Instruments.ELECTRIC_GUITAR_JAZZ)
    shcool_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,7), #Happy Birthday to you
        (90,'C4',10,10.75),(90,'C4',10.75,11),(100,'D4',11,12),(100,'C4',12,13),(100,'G4',13,14),(100,'F4',14,15), #Happy Birthday to you
        (90,'C4',18,18.75),(90,'C4',18.75,19),(100,'C5',19,20),(100,'A4',20,21),(100,'F4',21,21.75),(100,'F4',21.75,22),(95,'E4',22,22.75),(90,'D4',22.75,23),(95,'E4',23,23.75),(90,'D4',23.75,26), #Happy Birthday dear ??
        (100,'A#4',26,26.75),(100,'A#4',26.75,27),(100,'A4',27,28),(100,'F4',28,29),(100,'G4',29,30),(100,'F4',30,32) #Happy Birthday to you
    ]
    append_notes(notes = electric_guitar.notes, input_notes_list = shcool_melody_notes_list)
    instruments_list.append(electric_guitar)


def create_idol_melody(instruments_list):
    """
    パラメータがアイドルで、かつ、真夏のビーチに該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    synth_brass = pm.Instrument(Instruments.SYNTH_BRASS_1)
    applause = pm.Instrument(Instruments.APPLAUSE)
    idol_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,27) #Happy Birthday to you
    ]
    backing_param = [(60,'C4',i-0.75,i+0.15) for i in range(3,26)]
    append_notes(notes = synth_brass.notes, input_notes_list = idol_melody_notes_list,raise_velocity = -20)
    append_notes(notes = applause.notes, input_notes_list = backing_param)
    instruments_list.append(synth_brass)
    instruments_list.append(applause)


def create_outdoor_melody(instruments_list):
    """
    パラメータがアウトドアに該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    acostic_guitar = pm.Instrument(Instruments.ACOSTIC_GUITAR_NYLON)
    outdoor_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,27) #Happy Birthday to you
    ]
    append_notes(notes = acostic_guitar.notes, input_notes_list = outdoor_melody_notes_list)
    instruments_list.append(acostic_guitar)


def create_rock_melody(instruments_list):
    """
    パラメータがロックに該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    distortion_guitar = pm.Instrument(Instruments.DISTORTION_GUITAR)
    rock_melody_notes_list = \
    [
        (90,'C4',2,2.25),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,7), #Happy Birthday to you
        (90,'C4',8,8.25),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,13), #Happy Birthday to you
        (90,'C4',14,14.25),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,20), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,27) #Happy Birthday to you
    ]
    append_notes(notes = distortion_guitar.notes, input_notes_list = rock_melody_notes_list)
    instruments_list.append(distortion_guitar)


def create_electronics_melody(instruments_list):
    """
    パラメータがエレクトロニクスに該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    lead2_sawtooth = pm.Instrument(Instruments.LEAD2_SAWTOOTH)
    electronics_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,27) #Happy Birthday to you
    ]
    append_notes(notes = lead2_sawtooth.notes, input_notes_list = electronics_melody_notes_list)
    instruments_list.append(lead2_sawtooth)


def create_jazz_melody(instruments_list):
    """
    パラメータがジャズに該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    piano = pm.Instrument(Instruments.ACOSTIC_GRAND_PIANO)
    jazz_melody_notes_list = \
    [
        (90,'C4',2,2.25),(90,'C4',3,3.25),(100,'D4',4,6),(100,'C4',6,6.25),(100,'F4',7,7.75),(100,'E4',7.75,10), #Happy Birthday to you
        (90,'C4',11,11.25),(100,'D4',12,14),(100,'C4',14,14.25),(100,'G4',15,15.75),(100,'F4',15.75,18), #Happy Birthday to you
        (90,'C4',18,18.25),(90,'C4',19,19.25),(100,'C5',20,22),(100,'A4',22,23),(100,'F4',23,24),(95,'E4',24,25),(90,'D4',25,26), #Happy Birthday dear ??
        (100,'A#4',26.5,27.5),(100,'A#4',27.5,27.75),(100,'A4',28,29),(100,'F4',29,30),(100,'G4',31,32),(100,'F4',32,32.5) #Happy Birthday to you
    ]
    append_notes(notes = piano.notes, input_notes_list = jazz_melody_notes_list)
    instruments_list.append(piano)


def create_ghost_melody(instruments_list):
    """
    パラメータが妖怪に該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    goblins = pm.Instrument(Instruments.FX_GOBLINS)
    ghost_melody_notes_list = \
    [
        (90,'C4',2,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,18),(95,'E4',18,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,28) #Happy Birthday to you
    ]
    append_notes(notes = goblins.notes, input_notes_list = ghost_melody_notes_list)
    instruments_list.append(goblins)


def create_sword_melody(instruments_list):
    """
    パラメータが刀に該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    shakuhachi = pm.Instrument(Instruments.SHAKUHACHI)
    sword_melody_notes_list = \
    [
        (90,'C4',2,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,18),(95,'E4',18,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,27) #Happy Birthday to you
    ]
    append_notes(notes = shakuhachi.notes, input_notes_list = sword_melody_notes_list)
    instruments_list.append(shakuhachi)


def create_gun_melody(instruments_list):
    """
    パラメータが銃に該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    music_box = pm.Instrument(Instruments.MUSIC_BOX)
    gun_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'E4',5,5.2),(100,'F4',5.2,6),(100,'D4',6,6.2),(100,'E4',6.2,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'F4',11,11.2),(100,'G4',11.2,12),(100,'E4',12,12.2),(100,'F4',12.2,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,26) #Happy Birthday to you
    ]
    append_notes(notes = music_box.notes, input_notes_list = gun_melody_notes_list)
    instruments_list.append(music_box)


def create_history_melody(instruments_list):
    """
    パラメータが歴史に該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    shanai = pm.Instrument(Instruments.SHANAI)
    history_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,5),(100,'F4',5,6),(100,'E4',6,6.15),(100,'F4',6.15,6.3),(100,'E4',6.3,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,11),(100,'G4',11,12),(100,'F4',12,12.15),(100,'G4',12.15,12.3),(100,'F4',12.3,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,27) #Happy Birthday to you
    ]
    append_notes(notes = shanai.notes, input_notes_list = history_melody_notes_list)
    instruments_list.append(shanai)


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
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,28) #Happy Birthday to you
    ]
    append_notes(notes = trumpet.notes, input_notes_list = chunibyo_melody_notes_list)
    instruments_list.append(trumpet)


def create_fairy_melody(instruments_list):
    """
    パラメータがメルヘンに該当した場合の主旋律を作成する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    bowed = pm.Instrument(Instruments.PAD5_BOWED)
    fairy_melody_notes_list = \
    [
        (90,'C4',2,2.75),(90,'C4',2.75,3),(100,'D4',3,4),(100,'C4',4,4.8),(100,'C4',4.8,5),(100,'E4',5,5.2),(100,'F4',5.2,6),(100,'E4',6,8), #Happy Birthday to you
        (90,'C4',8,8.75),(90,'C4',8.75,9),(100,'D4',9,10),(100,'C4',10,10.8),(100,'C4',10.8,11),(100,'E4',11,11.2),(100,'G4',11.2,12),(100,'F4',12,14), #Happy Birthday to you
        (90,'C4',14,14.75),(90,'C4',14.75,14.81),(90,'F4',14.81,14.87),(90,'A4',14.87,15),(100,'C5',15,16),(100,'A4',16,17),(100,'F4',17,17.75),(100,'F4',17.75,18),(95,'E4',18,18.75),(95,'E4',18.75,19),(90,'D4',19,21), #Happy Birthday dear ??
        (100,'A#4',21,21.75),(100,'A#4',21.75,22),(100,'A4',22,23),(100,'F4',23,24),(100,'G4',24,25),(100,'F4',25,28) #Happy Birthday to you
    ]
    append_notes(notes = bowed.notes, input_notes_list = fairy_melody_notes_list)
    instruments_list.append(bowed)


def create_child_melody(instruments_list):
    """
    パラメータが子供に該当した場合の主旋律を作成する(jazzと同じ)

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    piccolo = pm.Instrument(Instruments.PICCOLO)
    xylophone = pm.Instrument(Instruments.XYLOPHONE)
    child_melody_notes_list = \
    [
        (90,'C4',2,2.25),(90,'C4',2.25,2.5),(100,'D4',2.5,2.75),(100,'C4',3,3.25),(100,'F4',3.5,3.75),(100,'E4',4,4.25), #Happy Birthday to you
        (90,'C4',6,6.25),(90,'C4',6.25,6.5),(100,'D4',6.5,6.75),(100,'C4',7,7.25),(100,'G4',7.5,7.75),(100,'F4',8,8.25), #Happy Birthday to you
        (90,'C4',10,10.25),(90,'C4',10.25,10.5),(100,'C5',10.5,10.75),(100,'A4',11,11.25),(100,'F4',11.5,11.75),(100,'F4',11.75,12),(95,'E4',12,12.25),(95,'E4',12.25,12.5),(90,'D4',12.75,13), #Happy Birthday dear ??
        (100,'A#4',14,14.25),(100,'A#4',14.25,14.5),(100,'A4',14.5,14.75),(100,'F4',15,15.25),(100,'G4',15.5,15.75),(100,'F4',16,17) #Happy Birthday to you
    ]
    append_notes(notes = piccolo.notes, input_notes_list = child_melody_notes_list, raise_key = 24)
    append_notes(notes = xylophone.notes, input_notes_list = child_melody_notes_list)
    instruments_list.append(piccolo)
    instruments_list.append(xylophone)


def create_mystery_melody(instruments_list):
    """
    パラメータがミステリーに該当した場合の主旋律を作成する(jazzと同じ)

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    create_jazz_melody(instruments_list)


def create_shopping_melody(instruments_list):
    """
    パラメータがショッピングに該当した場合の主旋律を作成する(jazzと同じ)

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    """
    handbell = pm.Instrument(Instruments.PAD1_NEW_AGE)
    shopping_melody_notes_list = \
    [
        (90,'C4',2,2.25),(90,'C4',2.25,2.5),(100,'D4',2.5,2.75),(100,'C4',3,3.25),(100,'F4',3.5,3.75),(100,'E4',4,4.25), #Happy Birthday to you
        (90,'C4',6,6.25),(90,'C4',6.25,6.5),(100,'D4',6.5,6.75),(100,'C4',7,7.25),(100,'G4',7.5,7.75),(100,'F4',8,8.25), #Happy Birthday to you
        (90,'C4',10,10.25),(90,'C4',10.25,10.5),(100,'C5',10.5,10.75),(100,'A4',11,11.25),(100,'F4',11.5,11.75),(100,'F4',11.75,12),(95,'E4',12,12.25),(95,'E4',12.25,12.5),(90,'D4',12.75,13), #Happy Birthday dear ??
        (100,'A#4',14,14.25),(100,'A#4',14.25,14.5),(100,'A4',14.5,14.75),(100,'F4',15,15.25),(100,'G4',15.5,15.75),(100,'F4',16,18) #Happy Birthday to you
    ]
    append_notes(notes = handbell.notes, input_notes_list = shopping_melody_notes_list)
    instruments_list.append(handbell)


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
        create_cat_melody(instruments_list)
    elif prime_value == 'dog':
        hoge = 'a'
    elif prime_value == 'train':
        hoge = 'a'
    elif prime_value == 'pc':
        create_PC_melody(instruments_list)
    elif prime_value == 'gourmet':
        hoge = 'a'
    elif prime_value == 'sport':
        create_sport_melody(instruments_list)
    elif prime_value == 'soccer':
        create_soccer_melody(instruments_list)
    elif prime_value == 'baseball':
        create_baseball_melody(instruments_list)
    elif prime_value == 'tabletennis':
        hoge = 'a'
    elif prime_value == 'japanese':
        hoge = 'a'
    elif prime_value == 'scandinavian':
        hoge = 'a'
    elif prime_value == 'tropical':
        create_tropical_melody(instruments_list)
    elif prime_value == 'school':
        create_school_melody(instruments_list)
    elif prime_value == 'idol':
        create_idol_melody(instruments_list)
    elif prime_value == 'outdoor':
        create_outdoor_melody(instruments_list)
    elif prime_value == 'car':
        hoge = 'a'
    elif prime_value == 'drama':
        hoge = 'a'
    elif prime_value == 'picture':
        hoge = 'a'
    elif prime_value == 'rock':
        create_rock_melody(instruments_list)
    elif prime_value == 'electronic':
        create_electronics_melody(instruments_list)
    elif prime_value == 'jazz':
        create_jazz_melody(instruments_list)
    elif prime_value == 'ghost':
        create_ghost_melody(instruments_list)
    elif prime_value == 'sword':
        create_sword_melody(instruments_list)
    elif prime_value == 'gun':
        create_gun_melody(instruments_list)
    elif prime_value == 'history':
        create_history_melody(instruments_list)
    elif prime_value == 'chuni':
        create_chunibyo_melody(instruments_list)
    elif prime_value == 'fairy':
        create_fairy_melody(instruments_list)
    elif prime_value == 'child':
        hoge = 'a'
    elif prime_value == 'mystery':
        create_mystery_melody(instruments_list)
    elif prime_value == 'shopping':
        create_shopping_melody(instruments_list)
    else:
        create_default_main_melody(instruments_list)


def midi_to_mp3(inputFileName):
	fs = FluidSynth('soundFont/MuseScore_General.sf3') #サウンドフォントを指定
	fs.midi_to_audio(inputFileName, 'sample.wav') #midiをmp3に変換、保存


def create_music(related_value_list, BPM=100):
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

    tempo = BPM * 2 #曲のテンポ
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