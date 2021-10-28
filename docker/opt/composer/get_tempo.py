def get_bpm(related_value_list, positive_param):
    """
    パラメータごとのテンポを返す

    Parameter
    ---------
    related_value_list : [str]
        言語分析の結果を格納したリスト
    positive_param : float
        Tweetから算出されたポジティブ度

    Return
    ------
    bpm
        そのパラメータに対応したbpm
    """
    bpm = 100 
    NO_ITEM   = 0
    ONE_ITEMS = 1
    TWO_ITEMS = 2

    prime_value = 'none'
    secondary_value = 'none'
    third_value = 'none'

    if len(related_value_list)   == NO_ITEM:
        prime_value = 'none'
        secondary_value = 'none'
        third_value = 'none'
    elif len(related_value_list) == ONE_ITEMS:
        prime_value     = related_value_list[0]
    elif len(related_value_list) == TWO_ITEMS:
        prime_value     = related_value_list[0]
        secondary_value = related_value_list[1]
    else:
        prime_value     = related_value_list[0]
        secondary_value = related_value_list[1]
        third_value     = related_value_list[2]
    
    if prime_value == 'sea':
        if positive_param < 0.33:
            bpm = 100 
        elif positive_param < 0.66:
            bpm = 100
        else:
            bpm = 100
    elif prime_value == 'cherry':
        if positive_param < 0.5:
            bpm = 100 
        else:
            bpm = 100
    elif prime_value == 'cat':
        bpm = 100 
    elif prime_value == 'dog':
        bpm = 100 
    elif prime_value == 'train':
        bpm = 134 
    elif prime_value == 'pc':
        bpm = 100 
    elif prime_value == 'gourmet':
        bpm = 120 
    elif prime_value == 'sport':
        bpm = 100 
    elif prime_value == 'soccer':
        bpm = 100 
    elif prime_value == 'baseball':
        bpm = 100 
    elif prime_value == 'tabletennis':
        bpm = 120 
    elif prime_value == 'japanese':
        bpm = 100 
    elif prime_value == 'scandinavian':
        bpm = 100 
    elif prime_value == 'tropical':
        bpm = 100 
    elif prime_value == 'school':
        bpm = 100 
    elif prime_value == 'idol':
        bpm = 100 
    elif prime_value == 'outdoor':
        bpm = 100 
    elif prime_value == 'car':
        bpm = 100 
    elif prime_value == 'bike':
        bpm = 100 
    elif prime_value == 'drama':
        bpm = 120 
    elif prime_value == 'picture':
        bpm = 100 
    elif prime_value == 'rock':
        bpm = 100 
    elif prime_value == 'electronic':
        bpm = 100 
    elif prime_value == 'jazz':
        bpm = 100 
    elif prime_value == 'ghost':
        bpm = 100 
    elif prime_value == 'sword':
        bpm = 100 
    elif prime_value == 'gun':
        bpm = 100 
    elif prime_value == 'history':
        bpm = 100 
    elif prime_value == 'chuni':
        bpm = 100 
    elif prime_value == 'fairy':
        bpm = 100 
    elif prime_value == 'child':
        bpm = 100 
    elif prime_value == 'mystery':
        bpm = 100 
    elif prime_value == 'shopping':
        bpm = 100 
    else:
        bpm = 100 

    return bpm