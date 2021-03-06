import librosa
import numpy as np
import soundfile as sf
import pretty_midi as pm

import settings
from composer.instruments import Instruments
import composer.get_tempo as get_tempo


# MIDIによってサウンドエフェクトを設定する必要のあるパラメータ
NEED_MIDI_EFFECTS_LIST = ['sea','japanese','scandinavian','tropical','outdoor','drama','rock','electronic','jazz','gun','history']

def get_effect_times(prime_value, positive_param):
    """
    サウンドエフェクトを発生させるタイミングを格納したリストを返す

    Parameters
    ----------
    prime_value : str
        言語分析の結果、一番使用頻度の高かったパラメータ
    positive_param : float
        ネガポジ判別の結果(0~1)

    Returns
    -------
    effect_times : 長さ2のリスト(int)
        サウンドエフェクトを発生させるタイミングを格納したリスト
    """
    effect_times = (0,0)
    if prime_value == 'sea':
        if positive_param < 0.33:
            effect_times = (7,13)
        elif positive_param < 0.66:
            effect_times = (7,13)
        else:
            effect_times = (5,9)
    elif prime_value == 'cherry':
        if positive_param < 0.5:
            effect_times = (7,13)
        else:
            effect_times = (7,13)
    elif prime_value == 'cat':
        effect_times = (5,9)
    elif prime_value == 'dog':
        effect_times = (7,13)
    elif prime_value == 'train':
        effect_times = (7,13)
    elif prime_value == 'pc':
        effect_times = (7,13)
    elif prime_value == 'gourmet':
        effect_times = (7,13)
    elif prime_value == 'sport':
        effect_times = (7,13)
    elif prime_value == 'soccer':
        effect_times = (7,13)
    elif prime_value == 'baseball':
        effect_times = (7,13)
    elif prime_value == 'tabletennis':
        effect_times = (7,13)
    elif prime_value == 'japanese':
        effect_times = (7,13)
    elif prime_value == 'scandinavian':
        effect_times = (8,16)
    elif prime_value == 'tropical':
        effect_times = (7,13)
    elif prime_value == 'school':
        effect_times = (7,15)
    elif prime_value == 'idol':
        effect_times = (7,13)
    elif prime_value == 'outdoor':
        effect_times = (7,13)
    elif prime_value == 'car':
        effect_times = (7,13)
    elif prime_value == 'bike':
        effect_times = (7,13)
    elif prime_value == 'drama':
        effect_times = (7,13)
    elif prime_value == 'picture':
        effect_times = (7,13)
    elif prime_value == 'rock':
        effect_times = (7,13)
    elif prime_value == 'electronic':
        effect_times = (7,13)
    elif prime_value == 'jazz':
        effect_times = (9,17)
    elif prime_value == 'ghost':
        effect_times = (7,13)
    elif prime_value == 'sword':
        effect_times = (7,13)
    elif prime_value == 'gun':
        effect_times = (7,13)
    elif prime_value == 'history':
        effect_times = (7,13)
    elif prime_value == 'chuni':
        effect_times = (7,13)
    elif prime_value == 'fairy':
        effect_times = (7,13)
    elif prime_value == 'child':
        effect_times = (5,9)
    elif prime_value == 'mystery':
        effect_times = (9,17)
    elif prime_value == 'shopping':
        effect_times = (5,9)
    else:
        effect_times = (0,0)
    return effect_times


def add_sea_effect(instruments_list, effect_time):
    """
    波の音のサウンドエフェクトを追加する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    effect_time : int
        サウンドエフェクトを発生させるタイミング
    """
    seashore = pm.Instrument(Instruments.SEASHORE)
    note = pm.Note(velocity = 100, pitch = pm.note_name_to_number('C4'),start = effect_time, end = effect_time+2)
    seashore.notes.append(note)
    instruments_list.append(seashore)


def add_japanese_effect(instruments_list, effect_time):
    """
    和風の音のサウンドエフェクトを追加する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    effect_time : int
        サウンドエフェクトを発生させるタイミング
    """
    koto = pm.Instrument(Instruments.KOTO)
    add_notes = [(100,'D4',effect_time,effect_time+0.125),(100,'E4',effect_time+0.125,effect_time+0.25),(100,'G4',effect_time+0.25,effect_time+0.375),(100,'A4',effect_time+0.375,effect_time+0.5),(100,'C5',effect_time+0.5,effect_time+0.625),(100,'D5',effect_time+0.625,effect_time+0.75),(100,'E5',effect_time+0.75,effect_time+0.875),(100,'G5',effect_time+0.875,effect_time+1),(100,'A5',effect_time+1,effect_time+2)]
    for i in add_notes:
        velocity, pitch, start, end = i
        note = pm.Note(velocity=velocity, pitch=pm.note_name_to_number(pitch),start=start,end=end)
        koto.notes.append(note)
    instruments_list.append(koto)


def add_scandinavian_effect(instruments_list, effect_time):
    """
    フィドルの音のサウンドエフェクトを追加する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    effect_time : int
        サウンドエフェクトを発生させるタイミング
    """
    fiddle = pm.Instrument(Instruments.FIDDLE)
    add_notes = [(100,'F4',effect_time,effect_time+0.25),(100,'E4',effect_time+0.25,effect_time+0.5),(100,'D4',effect_time+0.5,effect_time+0.75),(100,'C4',effect_time+0.75,effect_time+1),(100,'E4',effect_time+1,effect_time+2)]
    for i in add_notes:
        velocity, pitch, start, end = i
        note = pm.Note(velocity=velocity, pitch=pm.note_name_to_number(pitch),start=start,end=end)
        fiddle.notes.append(note)
    instruments_list.append(fiddle)


def add_tropical_effect(instruments_list, effect_time):
    """
    ウクレレ(はなかったのでギター)の音のサウンドエフェクトを追加する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    effect_time : int
        サウンドエフェクトを発生させるタイミング
    """
    acostic_guitar = pm.Instrument(Instruments.ACOSTIC_GUITAR_NYLON)
    add_notes = [(100,'F4',effect_time, effect_time+0.25),(100,'A4',effect_time, effect_time+0.25),(100,'C5',effect_time, effect_time+0.25),(100,'F4',effect_time+0.25, effect_time+1),(100,'A4',effect_time+0.25, effect_time+1),(100,'C5',effect_time+0.25, effect_time+1)]
    for i in add_notes:
        velocity, pitch, start, end = i
        note = pm.Note(velocity=velocity, pitch=pm.note_name_to_number(pitch),start=start,end=end)
        acostic_guitar.notes.append(note)
    instruments_list.append(acostic_guitar)


def add_outdoor_effect(instruments_list, effect_time):
    """
    鳥のさえずりの音のサウンドエフェクトを追加する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    effect_time : int
        サウンドエフェクトを発生させるタイミング
    """
    bird_tweet = pm.Instrument(Instruments.BIRD_TWEET)
    add_notes = [(100,'C4',effect_time,effect_time+1),(100,'C4',effect_time+1,effect_time+2)]
    for i in add_notes:
        velocity, pitch, start, end = i
        note = pm.Note(velocity=velocity, pitch=pm.note_name_to_number(pitch),start=start,end=end)
        bird_tweet.notes.append(note)
    instruments_list.append(bird_tweet)


def add_drama_effect(instruments_list, effect_time):
    """
    バイオリンの音のサウンドエフェクトを追加する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    effect_time : int
        サウンドエフェクトを発生させるタイミング
    """
    violin = pm.Instrument(Instrument.VIOLIN)
    note = pm.Note(velocity=100,pitch=pm.note_name_to_number('F4'),start=effect_time,end=effect_time+2)
    violin.notes.append(note)
    instruments_list.append(violin)


def add_rock_effect(instruments_list, effect_time):
    """
    エレキの音のサウンドエフェクトを追加する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    effect_time : int
        サウンドエフェクトを発生させるタイミング
    """
    electric_guitar = pm.Instrument(Instruments.ELECTRIC_GUITAR_CLEAN)
    add_notes = [(100,'F4',effect_time,effect_time+2),(100,'A#4',effect_time,effect_time+2),(100,'E5',effect_time,effect_time+2)]
    for i in add_notes:
        velocity, pitch, start, end = i
        note = pm.Note(velocity=velocity, pitch=pm.note_name_to_number(pitch),start=start,end=end)
        electric_guitar.notes.append(note)
    instruments_list.append(electric_guitar)


def add_electronic_effect(instruments_list, effect_time):
    """
    シンセサイザーの音のサウンドエフェクトを追加する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    effect_time : int
        サウンドエフェクトを発生させるタイミング
    """
    synth_brass = pm.Instrument(Instruments.SYNTH_BRASS_2)
    note = pm.Note(velocity=100,pitch=pm.note_name_to_number('F4'),start=effect_time,end=effect_time+1)
    synth_brass.notes.append(note)
    instruments_list.append(synth_brass)


def add_jazz_effect(instruments_list, effect_time):
    """
    jazzの音のサウンドエフェクトを追加する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    effect_time : int
        サウンドエフェクトを発生させるタイミング
    """
    piano = pm.Instrument(Instruments.ACOSTIC_GRAND_PIANO)
    add_notes = [(100,'F5',effect_time,effect_time+0.75),(100,'A5',effect_time,effect_time+0.75),(100,'C6',effect_time,effect_time+0.75),(100,'F5',effect_time+0.75,effect_time+0.8),(100,'A5',effect_time+0.75,effect_time+0.8),(100,'C6',effect_time+0.75,effect_time+0.8)]
    for i in add_notes:
        velocity, pitch, start, end = i
        note = pm.Note(velocity=velocity, pitch=pm.note_name_to_number(pitch),start=start,end=end)
        piano.notes.append(note)
    instruments_list.append(piano)


def add_gun_effect(instruments_list, effect_time):
    """
    銃の音のサウンドエフェクトを追加する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    effect_time : int
        サウンドエフェクトを発生させるタイミング
    """
    gun = pm.Instrument(Instruments.GUN_SHOT)
    note = pm.Note(velocity=100,pitch=pm.note_name_to_number('C4'),start=effect_time,end=effect_time+1)
    gun.notes.append(note)
    instruments_list.append(gun)


def add_history_effect(instruments_list, effect_time):
    """
    歴史の音のサウンドエフェクトを追加する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    effect_time : int
        サウンドエフェクトを発生させるタイミング
    """
    shanai = pm.Instrument(Instruments.SHANAI)
    add_notes = [(100,'F4',effect_time,effect_time+0.25),(100,'G4',effect_time+0.25,effect_time+0.5),(100,'C5',effect_time+0.5,effect_time+0.75),(100,'A4',effect_time+0.75,effect_time+1)]
    for i in add_notes:
        velocity, pitch, start, end = i
        note = pm.Note(velocity=velocity, pitch=pm.note_name_to_number(pitch),start=start,end=end)
        shanai.notes.append(note)
    instruments_list.append(shanai)


def add_midi_effect(instruments_list, effect_time, value):
    """
    MIDI音源にサウンドエフェクトを追加する

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    effect_time : int
        サウンドエフェクトを発生させるタイミング
    value : str
        発生させるサウンドエフェクトを示すパラメータ
    """
    if value == 'sea':
        add_sea_effect(instruments_list, effect_time)
    elif value == 'japanese':
        add_japanese_effect(instruments_list, effect_time)
    elif value == 'scandinavian':
        add_scandinavian_effect(instruments_list, effect_time)
    elif value =='tropical':
        add_tropical_effect(instruments_list, effect_time)
    elif value =='outdoor':
        add_outdoor_effect(instruments_list, effect_time)
    elif value =='drama':
        add_drama_effect(instruments_list, effect_time)
    elif value =='rock':
        add_rock_effect(instruments_list, effect_time)
    elif value =='electronic':
        add_electronic_effect(instruments_list, effect_time)
    elif value =='jazz':
        add_jazz_effect(instruments_list, effect_time)
    elif value =='gun':
        add_gun_effect(instruments_list, effect_time)
    elif value =='history':
        add_history_effect(instruments_list, effect_time)

def by_midi(instruments_list, positive_param, prime_value, secondary_value, third_value):
    """
    MIDIによってサウンドエフェクトを追加する(追加できるものはNEED_MIDI_EFFECTS_LISTにある項目のみ)

    Parameters
    ----------
    instruments_list : pretty_midi.Pretty_midi.instruments
        pretty_midi.Instrumentインスタンスを格納するリスト
    positive_param : float
        Tweetから算出されたポジティブ度
    prime_value : str
        言語分析の結果、一番使用頻度の高かったパラメータ
    secondary_value : str
        言語分析の結果、二番目に使用頻度の高かったパラメータ
    third_value : str
        言語分析の結果、三番目に使用頻度の高かったパラメータ
    """
    NEED_MIDI_SECOND = secondary_value in NEED_MIDI_EFFECTS_LIST
    NEED_MIDI_THIRD = third_value in NEED_MIDI_EFFECTS_LIST
    effect_times1, effect_times2 = get_effect_times(prime_value, positive_param)
    if NEED_MIDI_SECOND and effect_times1 > 0:
        add_midi_effect(instruments_list, effect_times1, secondary_value)
    if NEED_MIDI_THIRD and effect_times2 > 0:
        add_midi_effect(instruments_list, effect_times2, third_value)


def add_wav_effect(music_path, effect_time, value, BPM):
    """
    WAV音源(曲)にWAV音源(効果音)を加える

    Parameters
    ----------
    music_path : str
        元となる曲のパス
    effect_time : int
        効果音を加える拍
    value : str
        発生させるサウンドエフェクトを示すパラメータ
    BPM : int
        元の曲のはやさ
    """
    SE_FOLDER_PATH = 'composer/soundEffect/'
    effect_time_second = effect_time / (BPM / 60)
    se_wav_file_path = ''
    if value == 'cherry':
        se_wav_file_path = f'{SE_FOLDER_PATH}uguisu.wav'
    elif value == 'cat':
        se_wav_file_path = f'{SE_FOLDER_PATH}cat.wav'
    elif value == 'dog':
        se_wav_file_path = f'{SE_FOLDER_PATH}dog.wav'
    elif value == 'train':
        se_wav_file_path = f'{SE_FOLDER_PATH}train.wav'
    elif value == 'pc':
        se_wav_file_path = f'{SE_FOLDER_PATH}pc.wav'
    elif value == 'gourmet':
        se_wav_file_path = f'{SE_FOLDER_PATH}sumiyaki.wav'
    elif value == 'sport':
        se_wav_file_path = f'{SE_FOLDER_PATH}sport.wav'
    elif value == 'soccer':
        se_wav_file_path = f'{SE_FOLDER_PATH}soccer.wav'
    elif value == 'baseball':
        se_wav_file_path = f'{SE_FOLDER_PATH}bat.wav'
    elif value == 'tabletennis':
        se_wav_file_path = f'{SE_FOLDER_PATH}tabletennis.wav'
    elif value == 'school':
        se_wav_file_path = f'{SE_FOLDER_PATH}school_wei.wav'
    elif value == 'idol':
        se_wav_file_path = f'{SE_FOLDER_PATH}idle.wav'
    elif value == 'car':
        se_wav_file_path = f'{SE_FOLDER_PATH}car_engine1.wav'
    elif value == 'bike':
        se_wav_file_path = f'{SE_FOLDER_PATH}bike.wav'
    elif value == 'picture':
        se_wav_file_path = f'{SE_FOLDER_PATH}shutter.wav'
    elif value == 'ghost':
        se_wav_file_path = f'{SE_FOLDER_PATH}kerakera.wav'
    elif value == 'sword':
        se_wav_file_path = f'{SE_FOLDER_PATH}sword.wav'
    elif value == 'chuni':
        se_wav_file_path = f'{SE_FOLDER_PATH}chuni.wav'
    elif value == 'fairy':
        se_wav_file_path = f'{SE_FOLDER_PATH}merchen.wav'
    elif value == 'child':
        se_wav_file_path = f'{SE_FOLDER_PATH}child.wav'
    elif value == 'mystery':
        se_wav_file_path = f'{SE_FOLDER_PATH}hirameki.wav'
    elif value == 'shopping':
        se_wav_file_path = f'{SE_FOLDER_PATH}shopping.wav'

    if len(se_wav_file_path) > 1:
        merge_wav(music_path, se_wav_file_path, effect_time_second)



def by_librosa(id, positive_param, prime_value, secondary_value, third_value):
    """
    WAVによってサウンドエフェクトを追加する

    Parameters
    ----------
    id : str
        フォルダ名(uuid)
    positive_param : float
        Tweetから算出されたポジティブ度
    prime_value : str
        言語分析の結果、一番使用頻度の高かったパラメータ
    secondary_value : str
        言語分析の結果、二番目に使用頻度の高かったパラメータ
    third_value : str
        言語分析の結果、三番目に使用頻度の高かったパラメータ
    """
    BPM = get_tempo.get_bpm([prime_value], positive_param)
    BASE_WAV_PATH = f'movie/{id}/{settings.WAV_FILE_NAME}'
    NEED_LIBROSA_SECOND = secondary_value not in NEED_MIDI_EFFECTS_LIST
    NEED_LIBROSA_THIRD = third_value not in NEED_MIDI_EFFECTS_LIST
    effect_times1, effect_times2 = get_effect_times(prime_value, positive_param)
    if NEED_LIBROSA_SECOND and effect_times1 > 0:
        add_wav_effect(BASE_WAV_PATH, effect_times1, secondary_value, BPM)
    if NEED_LIBROSA_THIRD and effect_times2 > 0:
        add_wav_effect(BASE_WAV_PATH, effect_times2, third_value, BPM)


def merge_wav(filename_1, filename_2, time, fs=44100):
    """
    2つのwavを合成して, filename_1に上書きする. 
    filename_2はtimeで指定された秒数の部分に合成する.

    Parameters
    ----------
    filename_1 : string
        合成元ファイル名(合成したファイルはここに上書きされる)
    filename_2 : string
        合成されるファイル名
    time : float
        filename_2を合成する地点
    fs : int
        wavのサンプリングレート
    """

    # wavの読み込み
    wav_1, _ = librosa.load(filename_1, sr=fs, mono=True)
    wav_2, _ = librosa.load(filename_2, sr=fs, mono=True)

    # 合成する開始地点のindex
    start_idx = int(time * fs)

    # 合成後にはみ出さないように長さを拡張
    total_length = np.max((len(wav_1), start_idx + len(wav_2)))
    if (total_length > len(wav_1)):
        wav_1 = np.append(wav_1, np.zeros(total_length - len(wav_1)))

    # 合成されるほうの長さをゼロ埋めで合わせる
    wav_2 = np.append(np.zeros(start_idx), wav_2)
    wav_2 = np.append(wav_2, np.zeros(total_length - len(wav_2)))

    # 合成
    wav_1 += wav_2

    # 音割れ対策
    max_amplitude = np.max(np.abs(wav_1))
    if max_amplitude > 0.99995:
        wav_1 = wav_1 * 0.99995 / max_amplitude
    
    # 出力
    sf.write(filename_1, wav_1, fs, subtype="PCM_16")

if __name__ == "__main__":
    merge_wav(
        "./movie/my_test/input.wav",
        "./movie/my_test/voice.wav",
        time = 2.3
    )