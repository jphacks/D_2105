import moviepy.editor as mpy
import matplotlib.pyplot as plt
import numpy as np
import cv2, wave

# デバッグ用
import shutil, os

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

def create_clip(path, music_length, id):
    """
    画像から音楽と同じ長さの無音動画を作る関数

    Parameters
    ----------
    path : str
        動画化したい画像のパス
    music_length : float
        動画にする音楽の長さ(秒)
    id : str
        個人識別用uuid

    Return
    ------
    concat_clip :
        画像から生成した音楽と同じ長さの無音動画
    """
    MOVIE_PATH = './movie/' + id + '/'
    FPS = 30

    # 画像を取得
    img = cv2.imread(path, -1)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)

    # 画像を格納する処理
    clips = []
    clip = mpy.ImageClip(img).set_duration(music_length)
    clips.append(clip)

    # 動画を作成する処理
    concat_clip = mpy.concatenate_videoclips(clips, method='compose')

    return concat_clip

def clip_circle(path, id):
    """
    正方形のTwitterアイコンを円形に切り出す関数

    Parameters
    ----------
    path : str
        正方形のTwitterアイコンのパス
    id : str
        個人識別用uuid
    """
    MOVIE_PATH = './movie/' + id + '/'

    # 画像の読み込み
    img = cv2.imread(path, -1)
    height, width = img.shape[:2]

    # マスク作成 (黒く塗りつぶす画素の値は0)
    mask = np.zeros((height, width), dtype=np.uint8)
    # 円を描画する関数circle()を利用してマスクの残したい部分を 255 にしている。
    cv2.circle(mask, center=(height // 2, width // 2), radius=100, color=255, thickness=-1)

    # maskの値が0の画素は透過する
    img[mask==0] = [0, 0, 0, 0]

    cv2.imwrite(MOVIE_PATH + 'icon_circle.png', img)

def movie_create(id):
    """
    Parameter
    ---------
    id : str
        個人識別用uuid
    """
    MOVIE_PATH = './movie/' + id + '/'
    BASE_IMG_PATH = './movie_create/common_images/cake_background.PNG'
    ICON_IMG_PATH = MOVIE_PATH + '/icon.png'
    ICON_CIRCLE_PATH = MOVIE_PATH + '/icon_circle.png'
    IMGAGES_PATH = './movie_create/images/'
    BASE_HEIGHT = 720
    BASE_WIDTH = 720
    ICON_HEIGHT = 200
    ICON_WIDTH = 200
    FPS = 30

    # デバッグ用
    related_list = ['baseball', 'car', 'cat']
    if os.path.isfile(os.path.abspath('./movie/sample.wav')):
        shutil.copy2('./movie/sample.wav', MOVIE_PATH + '/sample.wav')
        shutil.copy2('./movie/icon.png', MOVIE_PATH + '/icon.png')
    else:
        with open('log.log', mode='w') as f:
            f.write('現在の階層は')
            f.write(os.getcwd())
        raise Exception

    # 音楽とその長さを取得
    with wave.open(MOVIE_PATH + 'sample.wav', 'r') as music:
        music_length = get_music_length(music.getnframes())

    # Twitterアイコンを円形にくり抜く
    clip_circle(ICON_IMG_PATH, id)

    # クリップを作成
    base_clip = create_clip(BASE_IMG_PATH, music_length, id)
    icon_clip = create_clip(ICON_CIRCLE_PATH, music_length, id)
    related_clip_0 = create_clip(IMGAGES_PATH + related_list[0] + '/01.PNG', music_length, id)
    related_clip_1 = create_clip(IMGAGES_PATH + related_list[1] + '/01.PNG', music_length, id)
    related_clip_2 = create_clip(IMGAGES_PATH + related_list[2] + '/01.PNG', music_length, id)

    # クリップの合成
    final_clip = mpy.CompositeVideoClip([base_clip, icon_clip.set_position((BASE_WIDTH * 0.38, BASE_HEIGHT * 0.2))])
    final_clip.write_videofile(MOVIE_PATH + 'happy_birthday.mp4', fps=FPS)
