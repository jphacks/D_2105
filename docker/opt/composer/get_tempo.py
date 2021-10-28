def get_BPM(related_value_list)
    """
    パラメータごとのテンポを返す

    Parameter
    ---------
    related_value_list : [str]
        言語分析の結果を格納したリスト

    Return
    ------
    bpm
        そのパラメータに対応したBPM
    """
    BPM = 100 
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
        BPM = 100 
    elif prime_value == 'cherry':
        BPM = 100 
    elif prime_value == 'cat':
        BPM = 100 
    elif prime_value == 'dog':
        BPM = 100 
    elif prime_value == 'train':
        BPM = 100 
    elif prime_value == 'pc':
        BPM = 100 
    elif prime_value == 'gourmet':
        BPM = 100 
    elif prime_value == 'sport':
        BPM = 100 
    elif prime_value == 'soccer':
        BPM = 100 
    elif prime_value == 'baseball':
        BPM = 100 
    elif prime_value == 'tabletennis':
        BPM = 100 
    elif prime_value == 'japanese':
        BPM = 100 
    elif prime_value == 'scandinavian':
        BPM = 100 
    elif prime_value == 'tropical':
        BPM = 100 
    elif prime_value == 'school':
        BPM = 100 
    elif prime_value == 'idol':
        BPM = 100 
    elif prime_value == 'outdoor':
        BPM = 100 
    elif prime_value == 'car':
        BPM = 100 
    elif prime_value == 'bike':
        BPM = 100 
    elif prime_value == 'drama':
        BPM = 100 
    elif prime_value == 'picture':
        BPM = 100 
    elif prime_value == 'rock':
        BPM = 100 
    elif prime_value == 'electronic':
        BPM = 100 
    elif prime_value == 'jazz':
        BPM = 100 
    elif prime_value == 'ghost':
        BPM = 100 
    elif prime_value == 'sword':
        BPM = 100 
    elif prime_value == 'gun':
        BPM = 100 
    elif prime_value == 'history':
        BPM = 100 
    elif prime_value == 'chuni':
        BPM = 100 
    elif prime_value == 'fairy':
        BPM = 100 
    elif prime_value == 'child':
        BPM = 100 
    elif prime_value == 'mystery':
        BPM = 100 
    elif prime_value == 'shopping':
        BPM = 100 
    else:
        BPM = 100 

    return BPM