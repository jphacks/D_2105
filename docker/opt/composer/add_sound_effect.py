import librosa
import pretty_midi as pm

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
    effect_times = []
    if prime_value == 'sea':
        if positive_param < 0.33:
            effect_times = [7,13]
        elif positive_param < 0.66:
            effect_times = [7,13]
        else:
            effect_times = [5,9]
    elif prime_value == 'cherry':
        if positive_param < 0.5:
            effect_times = [7,13]
        else:
            effect_times = [7,13]
    elif prime_value == 'cat':
        effect_times = [5,9]
    elif prime_value == 'dog':
        effect_times = [7,13]
    elif prime_value == 'train':
        effect_times = [7,13]
    elif prime_value == 'pc':
        effect_times = [7,13]
    elif prime_value == 'gourmet':
        effect_times = [7,13]
    elif prime_value == 'sport':
        effect_times = [7,13]
    elif prime_value == 'soccer':
        effect_times = [7,13]
    elif prime_value == 'baseball':
        effect_times = [7,13]
    elif prime_value == 'tabletennis':
        effect_times = [7,13]
    elif prime_value == 'japanese':
        effect_times = [7,13]
    elif prime_value == 'scandinavian':
        effect_times = [8,16]
    elif prime_value == 'tropical':
        effect_times = [7,13]
    elif prime_value == 'school':
        effect_times = [7,15]
    elif prime_value == 'idol':
        effect_times = [7,13]
    elif prime_value == 'outdoor':
        effect_times = [7,13]
    elif prime_value == 'car':
        effect_times = [7,13]
    elif prime_value == 'bike':
        effect_times = [7,13]
    elif prime_value == 'drama':
        effect_times = [7,13]
    elif prime_value == 'picture':
        effect_times = [7,13]
    elif prime_value == 'rock':
        effect_times = [7,13]
    elif prime_value == 'electronic':
        effect_times = [7,13]
    elif prime_value == 'jazz':
        effect_times = [9,17]
    elif prime_value == 'ghost':
        effect_times = [7,13]
    elif prime_value == 'sword':
        effect_times = [7,13]
    elif prime_value == 'gun':
        effect_times = [7,13]
    elif prime_value == 'history':
        effect_times = [7,13]
    elif prime_value == 'chuni':
        effect_times = [7,13]
    elif prime_value == 'fairy':
        effect_times = [7,13]
    elif prime_value == 'child':
        effect_times = [5,9]
    elif prime_value == 'mystery':
        effect_times = [9,17]
    elif prime_value == 'shopping':
        effect_times = [5,9]
    else:
        effect_times = []
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
    effect_times = get_effect_times(prime_value, positive_param)
    if NEED_MIDI_SECOND and len(effect_times) > 0:
        add_midi_effect(instruments_list, effect_times[0], secondary_value)
    if NEED_MIDI_THIRD and len(effect_times) > 0:
        add_midi_effect(instruments_list, effect_times[1], third_value)



def by_librosa():
    """
    WAVによってサウンドエフェクトを追加する(追加できるものはNEED_MIDI_EFFECTS_LISTにある項目のみ)

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
    hoge = 'hoge'