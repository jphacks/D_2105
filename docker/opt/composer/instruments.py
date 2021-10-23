class Instruments:
    # ピアノ系
    ACOSTIC_GRAND_PIANO   = 0
    BRIGHT_ACOSTIC_PIANO  = 1
    ELECTRIC_GRAND_PIANO  = 2
    HONKY_TONK_PIANO      = 3
    ELECTRIC_PIANO_1      = 4
    ELECTRIC_PIANO_2      = 5
    HARPSICORD            = 6
    CLAVI                 = 7

    # クロマチック・パーカッション系
    CELESTA               = 8
    GLOCKENSPIEL          = 9  #鉄琴
    MUSIC_BOX             = 10 #オルゴール
    VIBRAPHONE            = 11
    MARIMBA               = 12
    XYLOPHONE             = 13
    TUBULAR_BELLS         = 14
    DULCIMER              = 15 #ギターっぽいやつ

    #オルガン系
    DRAWBER_ORGAN         = 16 #オルガン
    PERCUSSIVE_ORGAN      = 17 #アタック強めのオルガン
    ROCK_ORGAN            = 18 #レスリーオルガン(?)
    CHURCH_ORGAN          = 19 #パイプオルガン
    REED_ORGAN            = 20 #足踏みオルガン
    ACCORDION             = 21
    HARMONICA             = 22
    TANGO_ACCORDION       = 23

    #ギター系
    ACOSTIC_GUITAR_NYLON  = 24 #ナイロン弦のアコギ
    ACOSTIC_GUITAR_STEEL  = 25 #スチール弦のアコギ
    ELECTRIC_GUITAR_JAZZ  = 26 #ジャズ用ギター
    ELECTRIC_GUITAR_CLEAN = 27 #クリーン用ギター
    ELECTRIC_GUITAR_MUTED = 28 #ミュートギター
    ORVERDRIVEN_GUITAR    = 29 #歪んだ音のギター
    DISTORTION_GUITAR     = 30 #さらに歪んだ音のギター
    GUITAR_HARMONIS       = 31 #ハーモニクス

    #ベース系
    ACOSIC_BASS           = 32
    ELECTRIC_BASS_FINGER  = 33 #指弾きベース
    ELECTRIC_BASS_PICK    = 34 #ピック弾きベース
    FRETLESS_BASS         = 35
    SLAP_BASS_1           = 36
    SLAP_BASS_2           = 37
    SYNTH_BASS_1          = 38
    SYNTH_BASS_2          = 39 #上のよりソフトらしい

    #ストリング系
    VIOLIN                = 40
    VIOLA                 = 41
    CELLO                 = 42
    CONTRABASS            = 43
    TREMORO_STRINGS       = 44 #トレモロ弾きのストリング
    PIZZICATO_STRINGS     = 45 #ピチカート(ミュート)弾きのストリングス
    ORCHESTRA_HARP        = 46 
    TIMPANI               = 47

    #アンサンブル系
    STRING_ENSAMBLE_1     = 48
    STRING_ENSAMBLE_2     = 49 #上のよりソフトらしい
    SYNTH_STRINGS_1       = 50
    SYNTH_STRINGS_2       = 51 #上のよりソフトらしい
    CHOIR_AAHS            = 52 #「あ〜」って感じのコーラスアンサンブル
    VOICE_OOHS            = 53 #「う〜」って感じのコーラスアンサンブル
    SYNTH_VOICE           = 54 #擬似的に作ったボイスアンサンブル(?)
    ORCHESTRA_HIT         = 55 #「ジャンっ！」って感じのやつ

    #ブラス系
    TRUMPET               = 56 
    TROMBONE              = 57
    TUBA                  = 58
    MUTED_TRUMPET         = 59
    FRENCH_HORN           = 60
    BRASS_SECTION         = 61 #ブラスアンサンブル
    SYNTH_BRASS_1         = 62
    SYNTH_BRASS_2         = 63

    #リード系
    SOPRANO_SAX           = 64
    ALTO_SAX              = 65
    TENOR_SAX             = 66
    BARITONE_SAX          = 67
    Oboe                  = 68
    ENGLISH_HONE          = 69
    BASSOON               = 70
    CLARINET              = 71

    #パイプ系
    PICCOLO               = 72
    FLUTE                 = 73
    RECORDER              = 74
    PAN_FLUTE             = 75
    BOTTLE_BLOW           = 76 #瓶の口に息を吹きかけて出る音
    SHAKUHACHI            = 77
    WHISTLE               = 78 #口笛
    OCARINA               = 79

    #シンセ・リード系
    LEAD1_SQUARE          = 80 #短形波のシンセリード
    LEAD2_SAWTOOTH        = 81 #鋸歯状波のシンセりーど
    LEAD3_CAILOPE         = 82 #カイロペ風シンセリード
    LEAD4_CHIFF           = 83 #柔らかめの音
    LEAD5_CHARANG         = 84 #硬めの音
    LEAD6_VOICE           = 85 #ヒューマンボイス
    LEAD7_FIFTH           = 86 #5度の和音つき
    LEAD8_BASS_AND_LEAD   = 87 #シンセベースつき

    #シンセパッド系
    PAD1_NEW_AGE          = 88 #ベル系
    PAD2_WARM             = 89 #温かみのある音
    PAD3_POLYSYNTH        = 90 #ポリムーグの擬似
    PAD4_COIR             = 91 #コーラス系
    PAD5_BOWED            = 92 #グラス破壊系
    PAD6_METALIC          = 93 #金属系
    PAD7_HALO             = 94 #明るい音
    PAD8_SWEEP            = 95 #うねり系

    #シンセ・エフェクト系
    FX_RAIN               = 96
    FX_SOUNDTRACK         = 97
    FX_CRYSTAL            = 98
    FX_ATMOSPHERE         = 99
    FX_BRIGHTNESS         = 100
    FX_GOBLINS            = 101
    FX_ECHOES             = 102
    FX_SCI_FI             = 103

    #エスニック系
    SITAR                 = 104
    BANJO                 = 105
    SHAMISEN              = 106
    KOTO                  = 107
    KALIMBA               = 108
    BAGPIPE               = 109
    FIDDLE                = 110
    SHANAI                = 111

    #パージカッシヴ系
    TINKLE_BELL           = 112
    AGOGO                 = 113 #大小のカウベル
    STEEL_DRUMS           = 114
    WOODBLOCK             = 115
    TAIKO_DRUM            = 116
    MELODIC_TOM           = 117 
    SYNTH_DRUM            = 118 #シンセタム
    REVERSE_CYMBAL        = 119

    #効果音
    GUITAR_FRET_NOISE     = 120 #フレットを擦る音　
    BREATH_NOISE          = 121 #息継ぎ音
    SEASHORE              = 122 #波の音
    BIRD_TWEET            = 123 #鳥の鳴き声
    TELEPHONE_RING        = 124 #黒電話のベル音
    HELICOPTER            = 125 #ヘリコプターのプロペラ音
    APPLAUSE              = 126 #拍手
    GUN_SHOT              = 127 #銃声


class DrumInstruments:
    #どれがあるのかわからないから一部のみ
    ACOSTIC_BASS_DRUM     = 0 
    BASS_DRUM             = 1
    SIDE_STICK            = 2
