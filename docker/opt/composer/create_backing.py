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
import numpy as np

from instruments import Instruments, DrumInstruments

INDEX_TO_NOTENUMBER = 20 #1から88にこれを足すとmidiのノートナンバーになる
# 例：よくある左手のF=20+21

#ダイアトニックコードリスト
F_DIATONIC = \
    [
        [21,25,28], #Ⅰ
        [23,26,30], #Ⅱm
        [25,28,32], #Ⅲm
        [26,30,33], #Ⅳ
        [16,20,23], #Ⅴ
        [18,21,25], #Ⅵm
        [20,23,26], #Ⅶdim

        #ここから7th
        [21,25,28,31], #Ⅰ7
        [23,26,30,33], #Ⅱm7
        [25,28,32,35], #Ⅲm7
        [26,30,33,36], #Ⅳ7
        [16,20,23,26], #Ⅴ7
        [18,21,25,28], #Ⅵm7
        [20,23,26,30], #Ⅶdim7

        [21,24, 28], #Ⅰsus4
    ]
CHORDS_DICT = [

        "Ⅰ",
        "Ⅱm",
        "Ⅲm",
        "Ⅳ",
        "Ⅴ",
        "Ⅵm",
        "Ⅶdim",

        #ここから7th
        "Ⅰ7",
        "Ⅱm7",
        "Ⅲm7",
        "Ⅳ7",
        "Ⅴ7",
        "Ⅵm7",
        "Ⅶdim7",

        "Ⅰsus4",
]

def craete_backing(related_value_list, key_note_list, rhythm_denominator):
    """
    入力されたパラメータを基に曲を作成する
    Parameters
    ----------
    related_value_list : [str]
        言語分析の結果を格納したリスト
    key_note_list : [int/float]
        great_oceanの21個の音の開始地点を入れたリスト
    rhythm_denominator : int
        何拍子か? 3or4を想定
    """
    if (len(key_note_list) != 21):
        raise ValueError(f"length of related_value_list must be 21, but input was {len(key_note_list)}")
    b = 5
    chords_candidate_list = [
        {
            # candidate: 使えるコード 
            # -1: 前のコードを継続することを意味する
            # -2: N.C.
            "candidate":   [-2], # C
            # probability: 重み 数値が大きいほど選ばれやすい
            "probability": [1],
        }, 
        {
            "candidate":   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,], # D, 
            "probability": [b, b, b, b, b, b, 1, b, b, b, b, b, b, 1, b,],
        },
        {
            "candidate":   [-1], # C
            "probability": [1],
        }, 
        {
            "candidate":   [0, 1, 3, 5, 6, 7, 9 ,11,12,], # F
            "probability": [b, b, b, b, 1, b, b, b, b,],
        }, 
        {
            "candidate":   [0, 2, 4, 6, 7, 9 ,11,13,], # E
            "probability": [b, b, b, 1, b, b, b, 1, ],
        }, 
        {
            "candidate":   [-2], # C
            "probability": [1],
        }, 
        {
            "candidate":   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,], # D
            "probability": [b, b, b, b ,b ,b ,1 ,b ,b ,b ,b ,b ,b ,1 ,b ,],
        }, 
        {
            "candidate":   [-2], # C
            "probability": [1],
        }, 
        {
            "candidate":   [0, 1, 3, 4, 7, 8, 9 ,11], # G
            "probability": [b, b, 1 ,b ,b ,b ,b ,b ,],
        }, 
        {
            "candidate":   [0, 1, 3, 5, 8, 10,12], # F
            "probability": [b, b, b ,b ,b ,b ,b ,],
        }, 
        {
            "candidate":   [-2], # C
            "probability": [1],
        }, 
        {
            "candidate":   [0, 2, 3, 4, 5, 9 ,10,11], # C(hi)
            "probability": [b, b, 1 ,b, b ,b ,b ,b, ],
        }, 
        {
            "candidate":   [-1,0, 1, 2, 5, 8, 9 ,10,12], # A
            "probability": [8 * b, b, b, b, b, b, b, b, b,],
        }, 
        {
            "candidate":   [-1,0, 3, 5, 8, 10,12,], # F
            "probability": [8 * b, b, b, b, b, b, b,],
        }, 
        {
            "candidate":   [-1,0,], # E
            "probability": [b, b,],
        }, 
        {
            "candidate":   [1, 3, 8, 10,], # D
            "probability": [b, b, b, b, ],
        }, 
        {
            "candidate":   [-2,1, 3, 8,], # B♭
            "probability": [3 * b ,b, b, b,],
        }, 
        {
            "candidate":   [1, 2, 3, 4, 8, 10,11,12], # A
            "probability": [b, b, b, b ,b ,b ,b ,b, ],
        }, 
        {
            "candidate":   [-1,1, 3, 8, 10,], # F
            "probability": [4* b, b, b ,b ,b ,],
        }, 
        {
            "candidate":   [4, 11], # G
            "probability": [3 * b, b,],
        }, 
        {
            "candidate":   [0, 7, 14,], # F
            "probability": [3 * b, 2 * b, 1 * b],
        }, 
    ] # コード進行の候補と確率

    chords_progression = []

    # コード進行を作る
    for i in range(len(key_note_list)):
        candidate = []
        for probability_idx in range(len(chords_candidate_list[i]["probability"])):
            for pb in range(chords_candidate_list[i]["probability"][probability_idx]):
                candidate.append(chords_candidate_list[i]["candidate"][probability_idx])

            # ドミナントモーションの発生確率を上げるための処理
            if (len(chords_progression) != 0 and chords_progression[-1] != -1 and chords_progression[-1] != -2):
                if ( chords_candidate_list[i]["candidate"][probability_idx] in [chords_progression[-1] - 4, chords_progression[-1] + 3, chords_progression[-1] - 11]):
                    # とりあえず発生確率を+2してみる
                    candidate.append(chords_candidate_list[i]["candidate"][probability_idx])
                    candidate.append(chords_candidate_list[i]["candidate"][probability_idx])
        
        chords_progression.append(np.random.choice(candidate))
    
    # ----テスト出力用-----
    for i in range(21):
        if (chords_progression[i] != -1 and chords_progression[i] != -2):
            print(CHORDS_DICT[chords_progression[i]], end=" ")
        else: print(chords_progression[i], end=" ")
    print("")
    # print(chords_progression)
    # ----テスト出力用ここまで-----


    # key_note_list があれば拍子を考える必要ないかも
    #if (rhythm_denominator == 3):
    #    pass
    #elif (rhythm_denominator == 4):
    #    pass

    # コード進行 chords_progression をもとに伴奏を作る

def create_chord_rhythm(chord_duration):
    """
    コードをじゃかじゃか弾く場合のリズムを決定
    Parameters
    chord_duration: int/float
        そのコードを継続する時間
        0.5→1拍

    Rerturns
    list(int/float)
        コードのストロークの継続時間の配列
    """
    duration_fixed = chord_duration * 2

    chords_durations = np.array([])
    while True:
        if np.sum(chords_durations) == duration_fixed:
            break
        max_duration = np.min((duration_fixed - np.sum(chords_durations)) * 4 , 4)
        chords_durations = np.append(chords_durations, 0.25 * np.random.randint(1, max_duration + 1))
    
    return (chords_durations / 2).tolist()

def create_chord_arpeggio(chords_duration, notes_lsit, density):
    """
    コードをアルペジオで弾く場合のリズムと音を決定
    Parameters
    chord_duration: int/float
        そのコードを継続する時間
        0.5→1拍
    notes_lsit: list[int]
        コードの構成音
    density: 0 or 1
        0: 密度低め
        1: 密度高め

    Rerturns
    list(tuple(int, int/float))
        音高と継続時間のタプルのリスト
    """
    
    if (density != 0 and density != 1):
        raise ValueError("argument [density] must be 0 or 1")

    # ひとつひとつの音の長さの候補
    note_duration = [0.125, 0.25]
    arpeggio = [(notes_lsit[0], note_duration[density])] # (音高, 長さ)のタプルのリスト
    for i in range((chords_duration // note_duration[density]) - 1):
        # 同じ音が連続しないための処理

        t = np.random.choice(notes_lsit)
        while t != arpeggio[-1][0]:
            t = np.random.choice(notes_lsit)
        arpeggio.append((t, note_duration[density]))
    return arpeggio

# 動作テスト
if __name__ == "__main__":
    back = craete_backing(
        related_value_list=["key1", "key2", "key3"],
        key_note_list=[
            2,3,4,5,6, #Happy Birthday to you
            8,9,10,11,12, #Happy Birthday to you
            14,15,16,17,18,19, #Happy Birthday dear ??
            21,22,23,24,25 #Happy Birthday to you
        ],
        rhythm_denominator=3
    )