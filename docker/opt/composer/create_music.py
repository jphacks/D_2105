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