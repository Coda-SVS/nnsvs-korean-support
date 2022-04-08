#!/usr/bin/env python3
# Copyright (c) 2020 oatsu
"""
ローマ字の音素を、先頭音素や母音で分類する
ALL_PHONEMES: 全音素のリスト
DICT_INIT: 分類するための初期の辞書。分類に合わない音素はothersに追加される。

로마자의 음소를 선두 음소와 모음으로 분류하다
ALL_PHONEMES: 온음소 리스트
DICT_INIT: 분류하기 위한 초기 사전분류에 맞지 않는 음소는 others에 추가된다.
"""

ALL_PHONEMES = [
    "br", "cl", "pau", "sil", "a", "i", "ye", "u", "vu", "va", "wi", "vi", "we", "ve", "wo", "vo", "bya", "byu", "byo", "e", "o", "ka", "ga", "ki", "gi", "kye", "gye", "kya", "gya", "kyu", "gyu", "kyo", "gyo", "ku", "gu", "kwa", "gwa", "kwi", "gwi", "kwu", "gwu", "kwe", "gwe", "kwo", "gwo", "ke", "ge", "ko", "go", "sa", "za", "shI", "ji", "si", "she", "je", "sha", "ja", "shu", "ju", "sho", "jo", "su", "zu", "zi", "se", "ze", "so", "zo", "ta", "da", "chi", "che", "cha", "chu", "cho", "tsu", "tsa", "tsi", "tse", "tso", "te", "de", "ti", "di", "dye", "tya", "dya", "tyu", "dyu", "tyo", "dyo", "to", "do", "tu", "du", "na", "ni", "nye", "nya", "nyu", "nyo", "nu", "ne", "no", "ha", "ba", "pa", "hi", "bi", "pi", "hye", "bye", "pye", "hya", "pya", "hyu", "pyu", "hyo", "pyo", "fu", "bu", "pu", "fa", "fi", "fe", "fo", "he", "be", "pe", "ho", "bo", "po", "ma", "mi", "mye", "mya", "myu", "myo", "mu", "me", "mo", "ya", "yu", "yo", "ra", "ri", "rye", "rya", "ryu", "ryo", "ru", "re", "ro", "wa", "N"
]
# リストの辞書
DICT_INIT = {
    'others': [],
    'mono': [],
    'x_a': [],
    'x_i': [],
    'x_u': [],
    'x_e': [],
    'x_o': [],
    'k_x': [],
    'kw_x': [],
    'ky_x': [],
    's_x': [],
    'sh_x': [],
    # 'sy_x': [],
    't_x': [],
    'ts_x': [],
    'ch_x': [],
    'ty_x': [],
    'n_x': [],
    'ny_x': [],
    'h_x': [],
    'f_x': [],
    'hy_x': [],
    'm_x': [],
    'my_x': [],
    'y_x': [],
    'r_x': [],
    'ry_x': [],
    'w_x': [],
    'g_x': [],
    'gy_x': [],
    'gw_x': [],
    'z_x': [],
    # 'zy_x': [],
    'j_x': [],
    'd_x': [],
    'dy_x': [],
    'b_x': [],
    'by_x': [],
    'v_x': [],
    'p_x': [],
    'py_x': [],
    'ALL': ALL_PHONEMES,
}


def classify_roma_phonemes(d_init, all_phonemes):
    """
    母音とか子音を判別して適当に分類します。
    """
    d = d_init
    for ph in all_phonemes:
        if ph in ('pau', 'sil', 'cl', 'br'):
            d['others'].append(ph)
            continue
        try:
            if len(ph) == 1:
                d['mono'].append(ph)
                if ph != 'N':
                    d[f'x_{ph}'].append(ph)
            elif len(ph) == 2:
                d[f'x_{ph[1]}'].append(ph)
                d[f'{ph[0]}_x'].append(ph)
            elif len(ph) == 3:
                d[f'x_{ph[2]}'].append(ph)
                d[f'{ph[:2]}_x'].append(ph)
            else:
                raise ValueError(ph)
        except KeyError:
            d['others'].append(ph)
    return d


def main():
    """
    辞書を読みやすい文字列にしてjsonとしてファイル出力する。
    """
    d = classify_roma_phonemes(DICT_INIT, ALL_PHONEMES)
    s_out = '{' + ',\n'.join([f'\'{k}\': {v}' for k, v in d.items()]) + '}'
    s_out = s_out.replace('\'', '\"')
    with open('result_roma_classifier.json', mode='w') as fj:
        fj.write(s_out)


if __name__ == '__main__':
    main()
