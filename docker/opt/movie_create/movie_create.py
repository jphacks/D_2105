import moviepy.editor as mpy
import cv2, wave, os
import settings
# デバッグ用
import shutil

def get_music_length(music_frames):
    """
    音楽の長さが何秒かを浮動小数で返す関数

    Parameter
    ---------
    music_frames : int
        フレームレート数

    Return
    ------
    1.0 * music_frames / SAMPLING_RATE : float
        音楽の長さ(秒)
    """
    SAMPLING_RATE = 44100

    return 1.0 * music_frames / SAMPLING_RATE

def movie_create(id):
    """
    Parameter
    ---------
    id : str
        個人識別用uuid
    """
    MOVIE_PATH = './movie/' + id + '/'
    BASE_IMG_PATH = './movie_create/common_images/cake.PNG'
    BASE_HEIGHT = 720
    BASE_WIDTH = 720

    # デバッグ用
    if os.path.isfile(os.path.abspath('./movie/sample.wav')):
        shutil.copy2('./movie/sample.wav', './movie/' + id + '/sample.wav')
    else:
        with open('log.log', mode='w') as f:
            f.write('現在の階層は')
            f.write(os.getcwd())
        raise Exception

    # 背景画像を取得
    base_img = cv2.imread(BASE_IMG_PATH)
    base_img = cv2.cvtColor(base_img, cv2.COLOR_BGRA2RGBA)

    # 音楽とその長さを取得
    with wave.open(MOVIE_PATH + 'sample.wav', 'r') as music:
        music_length = get_music_length(music.getnframes())

    # 動画を作る元となる背景画像を格納する処理
    clips = []
    clip = mpy.ImageClip(base_img).set_duration(music_length)
    clip = clip.resize(newsize=(BASE_WIDTH, BASE_HEIGHT))
    clips.append(clip)

    # 動画を作成する処理
    concat_clip = mpy.concatenate_videoclips(clips, method='compose')
    concat_clip.write_videofile(MOVIE_PATH + 'happy_birthday.mp4', fps=30)
