import moviepy.editor as mpy
import matplotlib.pyplot as plt
import numpy as np
import cv2, wave

# デバッグ用
import shutil, os

def get_music(id):
    """
    音楽の長さが何秒か(浮動小数)と
    フレーム数を返す関数

    Parameter
    ---------
    id : str
        個人識別用uuid

    Returns
    -------
    1.0 * music_frames / SAMPLING_RATE : float
        音楽の長さ(秒)
    """
    MOVIE_PATH = MOVIE_PATH = './movie/' + id + '/'
    SAMPLING_RATE = 44100

    with wave.open(MOVIE_PATH + 'sample.wav', 'r') as music:
        music_frames = music.getnframes()

    return 1.0 * music_frames / SAMPLING_RATE

def create_clip(path, id, is_icon=False):
    """
    画像から音楽と同じ長さの無音動画を作る関数

    Parameters
    ----------
    path : str
        動画化したい画像のパス
    id : str
        個人識別用uuid
    is_icon : bool
        Twitterアイコンであるかどうか

    Return
    ------
    concat_clip :
        画像から生成した音楽と同じ長さの無音動画
    """
    MOVIE_PATH = './movie/' + id + '/'
    FPS = 30
    SECONDS_PER_FRAME = 1/30

    # デバッグ用
    bpm = 30

    # 音楽の長さ，フレーム数を取得
    music_length = get_music(id)

    # 画像を格納する処理
    clips = []

    # Twitterアイコンであるかどうかを判定する
    if is_icon:
        img_list = clip_circle(path, id, bpm, music_length)

        for i in img_list:
            clip = mpy.ImageClip(i).set_duration(SECONDS_PER_FRAME)
            clips.append(clip)
    else:
        # 画像を取得
        img = cv2.imread(path, -1)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
        clip = mpy.ImageClip(img).set_duration(music_length)
        clips.append(clip)

    # 動画を作成する処理
    concat_clip = mpy.concatenate_videoclips(clips, method='compose')

    return concat_clip

def clip_circle(path, id, bpm, music_length):
    """
    正方形のTwitterアイコンを円形に切り出す関数

    Parameters
    ----------
    path : str
        正方形のTwitterアイコンのパス
    id : str
        個人識別用uuid
    bpm : int
        曲の速さ(♩/秒)
    music_length : float
        音楽の長さ(秒)

    Return
    ------
    img_list : numpy型配列
        円形に切り出したTwitterアイコンの配列
    """
    MOVIE_PATH = './movie/' + id + '/'
    FPS = 30

    # 画像の読み込み
    img_origin = cv2.imread(path, -1)
    img_origin = cv2.cvtColor(img_origin, cv2.COLOR_BGRA2RGBA)
    height, width = img_origin.shape[:2]

    img_list = []
    movie_frames = int(music_length * FPS) + 1

    for i in range(movie_frames):
        '''
        bpmに合わせて拡大縮小を行う．

        bpm
        60(s)でpbm(拍) = 60/bpm(s)で1(拍)

        fps
        1(s)で30(枚) = 60/bpm(s)で1800/bpm(枚)
        '''
        SECONDS_PER_MINUTE = 60
        FPS = 30
        FRAMES_PER_BEAT = SECONDS_PER_MINUTE * FPS // bpm
        new_size = 0

        # 深いコピー
        img = img_origin.copy()

        # 画像の拡大縮小
        if i % FRAMES_PER_BEAT < FRAMES_PER_BEAT // 2:
            new_size = 200 - 50 * (i % (FRAMES_PER_BEAT // 2)) // (FRAMES_PER_BEAT // 2)
        else:
            new_size = 150 + 50 * (i % (FRAMES_PER_BEAT // 2)) // (FRAMES_PER_BEAT // 2)

        cv2.resize(img, dsize=None, fx=new_size/200, fy=new_size/200)

        # マスク作成 (黒く塗りつぶす画素の値は0)
        mask = np.zeros((200, 200), dtype=np.uint8)

        # 円を描画する関数circle()を利用してマスクの残したい部分を 255 にしている。
        cv2.circle(mask, center=(height//2, width//2), radius=new_size//2, color=255, thickness=-1)

        # maskの値が0の画素は透過する
        img[mask==0] = [0, 0, 0, 0]
        img_list.append(img)

    return img_list

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

    # クリップを作成
    base_clip = create_clip(BASE_IMG_PATH, id)
    icon_clip = create_clip(ICON_IMG_PATH, id, is_icon=True)
    related_clip_0 = create_clip(IMGAGES_PATH + related_list[0] + '/01.PNG', id)
    related_clip_1 = create_clip(IMGAGES_PATH + related_list[1] + '/01.PNG', id)
    related_clip_2 = create_clip(IMGAGES_PATH + related_list[2] + '/01.PNG', id)

    # クリップの合成
    final_clip = mpy.CompositeVideoClip([base_clip, icon_clip.set_position((BASE_WIDTH * 0.38, BASE_HEIGHT * 0.2))])
    final_clip.write_videofile(MOVIE_PATH + 'happy_birthday.mp4', fps=FPS)
