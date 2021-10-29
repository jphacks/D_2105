import moviepy.editor as mpy
import matplotlib.pyplot as plt
import numpy as np
import cv2, wave
import settings

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
    MOVIE_PATH = MOVIE_PATH = '/root/opt/movie/' + id + '/'
    WAVE_PATH = MOVIE_PATH + settings.WAV_FILE_NAME
    SAMPLING_RATE = 44100

    with wave.open(WAVE_PATH, 'r') as music:
        music_frames = music.getnframes()

    return 1.0 * music_frames / SAMPLING_RATE

def create_clip(path, id, bpm=0, is_icon=False, is_related=False):
    """
    画像から音楽と同じ長さの無音動画を作る関数

    Parameters
    ----------
    path : str
        動画化したい画像のパス
    id : str
        個人識別用uuid
    bpm : int
        作成した曲のbpm
    is_icon : bool
        Twitterアイコンであるかどうか
    is_related : bool
        その人に関係ある画像であるかどうか

    Return
    ------
    concat_clip :
        画像から生成した音楽と同じ長さの無音動画
    """
    MOVIE_PATH = f'/root/opt/movie/{id}/'
    FPS = 30
    SECONDS_PER_FRAME = 1/30

    # 音楽の長さ，フレーム数を取得
    music_length = get_music(id)

    # 画像を格納する処理
    clips = []

    if is_icon: # Twitterアイコンのとき
        img_list = clip_circle(path, id, bpm, music_length)

        for i in img_list:
            clip = mpy.ImageClip(i).set_duration(SECONDS_PER_FRAME)
            clips.append(clip)
    elif is_related: # 関係ある画像のとき
        img_list = clip_related(path, id, bpm, music_length)

        for i in img_list:
            clip = mpy.ImageClip(i).set_duration(SECONDS_PER_FRAME)
            clips.append(clip)
    else: # 背景のとき
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
    正方形のTwitterアイコンを円形に切り出し，
    スライドショー用の配列に格納する関数

    Parameters
    ----------
    path : str
        正方形のTwitterアイコンのパス
    id : str
        個人識別用uuid
    bpm : int
        作成した曲のbpm
    music_length : float
        音楽の長さ(秒)

    Return
    ------
    img_list : ndarray
        円形に切り出したTwitterアイコンの配列
    """
    MOVIE_PATH = '/root/opt/movie/' + id + '/'
    FPS = 30

    # 画像の読み込み
    img_origin = cv2.imread(path, -1)
    img_origin = cv2.cvtColor(img_origin, cv2.COLOR_BGRA2RGBA)

    img_list = []
    movie_frames = int(music_length * FPS)

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

        # 深いコピー
        img = img_origin.copy()

        # 画像の拡大縮小
        if i % FRAMES_PER_BEAT < FRAMES_PER_BEAT // 2:
            new_size = 200 - 50 * (i % (FRAMES_PER_BEAT // 2)) // (FRAMES_PER_BEAT // 2)
        else:
            new_size = 150 + 50 * (i % (FRAMES_PER_BEAT // 2)) // (FRAMES_PER_BEAT // 2)

        # マスク作成 (黒く塗りつぶす画素の値は0)
        mask = np.zeros((new_size, new_size), dtype=np.uint8)

        # 円を描画する関数circle()を利用してマスクの残したい部分を 255 にしている。
        cv2.circle(mask, center=(new_size//2, new_size//2), radius=new_size//2, color=255, thickness=-1)

        # 画像の拡縮
        img = cv2.resize(img, dsize=(new_size, new_size))

        # maskの値が0の画素は透過する
        img[mask==0] = [0, 0, 0, 0]
        img_list.append(img)

    return img_list

def clip_related(path, id, bpm, music_length):
    """
    その人に関係ある画像を，
    スライドショー用の配列に格納する関数

    Parameters
    ----------
    path : str
        その人に関係ある画像のパス
    id : str
        個人識別用uuid
    bpm : int
        曲の速さ(♩/秒)
    music_length : float
        音楽の長さ(秒)

    Return
    ------
    img_list : ndarray
        その人に関係ある画像の配列
    """
    MOVIE_PATH = '/root/opt/movie/' + id + '/'
    FPS = 30

    # 画像の読み込み
    img_origin = cv2.imread(path, -1)
    img_origin = cv2.cvtColor(img_origin, cv2.COLOR_BGRA2RGBA)
    height = img_origin.shape[0]
    width = img_origin.shape[1]

    img_list = []
    movie_frames = int(music_length * FPS)

    for i in range(movie_frames):
        '''
        bpmに合わせてスイングを行う．

        bpm
        60(s)でpbm(拍) = 60/bpm(s)で1(拍)

        fps
        1(s)で30(枚) = 60/bpm(s)で1800/bpm(枚)
        '''
        SECONDS_PER_MINUTE = 60
        FPS = 30
        FRAMES_PER_BEAT = SECONDS_PER_MINUTE * FPS // bpm

        # 深いコピー
        img = img_origin.copy()

        # 画像を回転する角度を決定
        if i % FRAMES_PER_BEAT < FRAMES_PER_BEAT // 2:
            angle = 15 - 30 * (i % (FRAMES_PER_BEAT // 2)) // (FRAMES_PER_BEAT // 2)
        else:
            angle = -15 + 30 * (i % (FRAMES_PER_BEAT // 2)) // (FRAMES_PER_BEAT // 2)

        rad_angle = np.radians(angle)
        width_rot = int(np.round(width*abs(np.cos(rad_angle)) + height*abs(np.sin(rad_angle))))
        height_rot = int(np.round(width*abs(np.sin(rad_angle)) + height*abs(np.cos(rad_angle))))

        # 回転行列を生成
        mat = cv2.getRotationMatrix2D((width//2, height), angle, 1)
        mat[0][2] += -width/2 + width_rot/2
        mat[1][2] += -height/2 + height_rot/2

        # アフィン変換
        affine_img = cv2.warpAffine(img, mat, (width_rot, height_rot))
        img_list.append(affine_img)

    return img_list

def movie_create(id, bpm, related_list):
    """
    Parameters
    ----------
    id : str
        個人識別用uuid
    bpm : int
        作成した曲のbpm
    related_list : array
        関連するキーワードのリスト
    """
    MOVIE_PATH = '/root/opt/movie/' + id + '/'
    WAVE_PATH = MOVIE_PATH + settings.WAV_FILE_NAME
    BASE_IMG_PATH = '/root/opt/movie_create/common_images/cake_background.PNG'
    ICON_IMG_PATH = MOVIE_PATH + '/icon.png'
    IMGAGES_PATH = '/root/opt/movie_create/images/'
    BASE_HEIGHT = 720
    BASE_WIDTH = 720
    FPS = 30

    # クリップを作成
    base_clip = create_clip(BASE_IMG_PATH, id)
    icon_clip = create_clip(ICON_IMG_PATH, id, bpm, is_icon=True)
    related_clip_0 = create_clip(IMGAGES_PATH + related_list[0] + '/01.PNG', id, bpm, is_related=True)
    related_clip_1 = create_clip(IMGAGES_PATH + related_list[1] + '/01.PNG', id, bpm, is_related=True)
    related_clip_2 = create_clip(IMGAGES_PATH + related_list[2] + '/01.PNG', id, bpm, is_related=True)

    # クリップの合成
    final_clip = mpy.CompositeVideoClip([base_clip, icon_clip.set_position((BASE_WIDTH * 0.38, BASE_HEIGHT * 0.2)), \
    related_clip_0.set_position((0, BASE_HEIGHT * 0.55)), related_clip_1.set_position((BASE_WIDTH * 0.37, BASE_HEIGHT * 0.65)), \
    related_clip_2.set_position((BASE_WIDTH * 0.7, BASE_HEIGHT * 0.55))])

    # 音と動画を合成
    final_clip = final_clip.set_audio(mpy.AudioFileClip(WAVE_PATH))
    final_clip.write_videofile(filename = MOVIE_PATH + 'happy_birthday.mp4', codec='libx264', audio_codec='aac', fps=FPS)
