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