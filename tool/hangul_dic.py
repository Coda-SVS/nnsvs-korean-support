# 해당 자소 및 음소는 공식적인 문법이 아닐 수 있습니다. (보기에 더 좋게 설계됨)
# These consonants and phonemes may not be official grammar. (Designed to look better)

import regex


Consonants_LIST = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ", "ㄲ", "ㄸ", "ㅃ", "ㅆ", "ㅉ"]
Vowels_LIST = ["ㅏ", "ㅑ", "ㅓ", "ㅕ", "ㅗ", "ㅛ", "ㅜ", "ㅠ", "ㅡ", "ㅣ", "ㅐ", "ㅒ", "ㅔ", "ㅖ", "ㅘ", "ㅙ", "ㅚ", "ㅝ", "ㅞ", "ㅟ", "ㅢ"]


def replace2phn(regex_list: list, jamo_text: str, verbose: bool = False):
    if verbose:
        before_text = jamo_text

    for pattern, repl in regex_list:
        if verbose:
            if not before_text == jamo_text:
                print(f"> {before_text}\n-> {jamo_text}\n")
            before_text = jamo_text
        jamo_text = regex.sub(pattern, repl, jamo_text)

    if verbose:
        print(f"> {before_text}\n-> {jamo_text}\n")

    return jamo_text[:-1]


def get_phn_dictionary(labeling_mode: bool = True):

    ##### 전처리 #####
    pre_regex_list = [
        (r"ㄹ\s*ㄹ", r"l l "),
        # 모음 뒤, 'ㅎ' 앞의 'ㄹ'
        (r"ㄹ\s*ㅎ", r"r h "),
        # 모음과 모음 사이 'ㄹ'
        (r"(?<=[ㅏ-ㅣ]\s*)ㄹ(?=\s*[ㅏ-ㅣ])", r"r "),
    ]

    if labeling_mode:
        pre_regex_list.append((r"(?<=ㄱ\s*)ㅆ", r"k ss "))
        pre_regex_list.append((r"(?<=ㅂ\s*)ㅆ", r"p ss "))
    else:
        pre_regex_list.append((r"(?<=ㄱ\s*)ㅆ", r"kss "))
        pre_regex_list.append((r"(?<=ㅂ\s*)ㅆ", r"pss "))

    ########
    # 초성 #
    ########
    lead_consonants_process_regex_list = [
        (r"ㄱ(?=\s*([ㅏ-ㅣ]))", r"g "),
        (r"ㄴ(?=\s*([ㅏ-ㅣ]))", r"n "),
        (r"ㄷ(?=\s*([ㅏ-ㅣ]))", r"d "),
        (r"ㄹ(?=\s*([ㅏ-ㅣ]))", r"r "),
        (r"ㅁ(?=\s*([ㅏ-ㅣ]))", r"m "),
        (r"ㅂ(?=\s*([ㅏ-ㅣ]))", r"b "),
        (r"ㅅ(?=\s*([ㅏ-ㅣ]))", r"s "),
        # 초성에서 소리 없음
        (r"ㅇ(?=\s*([ㅏ-ㅣ]))", r""),
        (r"ㅈ(?=\s*([ㅏ-ㅣ]))", r"j "),
        (r"ㅊ(?=\s*([ㅏ-ㅣ]))", r"ch "),
        (r"ㅋ(?=\s*([ㅏ-ㅣ]))", r"k "),
        (r"ㅌ(?=\s*([ㅏ-ㅣ]))", r"t "),
        (r"ㅍ(?=\s*([ㅏ-ㅣ]))", r"p "),
        (r"ㅎ(?=\s*([ㅏ-ㅣ]))", r"h "),
        # UTAU에서 통용되는 표기는 'gg'이지만 외국 사용자들의 접근성을 위해 'kk'로 표기
        (r"ㄲ(?=\s*([ㅏ-ㅣ]))", r"kk "),
        # UTAU에서 통용되는 표기는 'dd'이지만 외국 사용자들의 접근성을 위해 'tt'로 표기
        (r"ㄸ(?=\s*([ㅏ-ㅣ]))", r"tt "),
        # UTAU에서 통용되는 표기는 'bb'이지만 외국 사용자들의 접근성을 위해 'pp'로 표기
        (r"ㅃ(?=\s*([ㅏ-ㅣ]))", r"pp "),
        (r"ㅆ(?=\s*([ㅏ-ㅣ]))", r"ss "),
        (r"ㅉ(?=\s*([ㅏ-ㅣ]))", r"jj "),
    ]

    ########
    # 중성 #
    ########
    vowels_process_regex_list = [
        (r"ㅏ", r"a "),
        (r"ㅓ", r"eo "),
        (r"ㅗ", r"o "),
        (r"ㅜ", r"u "),
        (r"ㅡ", r"eu "),
        (r"ㅣ", r"i "),
        (r"ㅔ", r"e "),
        (r"ㅐ", r"e "),
    ]

    if labeling_mode:
        vowels_process_regex_list.append((r"ㅑ", r"y a "))
        vowels_process_regex_list.append((r"ㅕ", r"y eo "))
        vowels_process_regex_list.append((r"ㅛ", r"y o "))
        vowels_process_regex_list.append((r"ㅠ", r"y u "))
        vowels_process_regex_list.append((r"ㅖ", r"y e "))
        vowels_process_regex_list.append((r"ㅒ", r"y e "))
        vowels_process_regex_list.append((r"ㅘ", r"w a "))
        vowels_process_regex_list.append((r"ㅚ", r"w e "))
        vowels_process_regex_list.append((r"ㅞ", r"w e "))
        vowels_process_regex_list.append((r"ㅙ", r"w e "))
        # UTAU에서는 사용되지 않지만 상황에 따라 'i'발음을 원순모음화 시 발생
        vowels_process_regex_list.append((r"ㅟ", r"w i "))
        # UTAU에서는 사용되지 않지만 상황에 따라 'e'발음을 원순모음화 시 발생
        vowels_process_regex_list.append((r"ㅝ", r"w eo "))
        # 라벨링을 할 때는 'wu i'로 구분
        vowels_process_regex_list.append((r"ㅢ", r"eu i "))
    else:
        vowels_process_regex_list.append((r"ㅑ", r"ya "))
        vowels_process_regex_list.append((r"ㅕ", r"yeo "))
        vowels_process_regex_list.append((r"ㅛ", r"yo "))
        vowels_process_regex_list.append((r"ㅠ", r"yu "))
        vowels_process_regex_list.append((r"ㅖ", r"ye "))
        vowels_process_regex_list.append((r"ㅒ", r"ye "))
        vowels_process_regex_list.append((r"ㅘ", r"wa "))
        vowels_process_regex_list.append((r"ㅚ", r"we "))
        vowels_process_regex_list.append((r"ㅞ", r"we "))
        vowels_process_regex_list.append((r"ㅙ", r"we "))
        # UTAU에서는 사용되지 않지만 상황에 따라 'i'발음을 원순모음화 시 발생
        vowels_process_regex_list.append((r"ㅟ", r"wi "))
        # UTAU에서는 사용되지 않지만 상황에 따라 'e'발음을 원순모음화 시 발생
        vowels_process_regex_list.append((r"ㅝ", r"weo "))
        # 라벨링을 할 때는 'wu i'로 구분
        vowels_process_regex_list.append((r"ㅢ", r"eui "))

    ########
    # 종성 #
    ########
    tail_consonants_process_regex_list = [
        # 악, 앜, 앆... 등에 쓰이는 받침
        (r"ㄱ", r"K "),
        # 안 ... 등에 쓰이는 받침
        (r"ㄴ", r"N "),
        # 앋, 앗, 앚, 앛, 앝, 앟, 았 ... 등에 쓰이는 받침
        (r"ㄷ", r"T "),
        # 알 ... 등에 쓰이는 받침
        (r"ㄹ", r"L "),
        # 암 ... 등에 쓰이는 받침
        (r"ㅁ", r"M "),
        # 압, 앞 ... 등에 쓰이는 받침
        (r"ㅂ", r"P "),
        # 앙 ... 등에 쓰이는 받침
        (r"ㅇ", r"NG "),
    ]

    ##### 후처리 #####
    post_regex_list = [
        # (r"\s{2,}", r" "),
    ]

    # if not labeling_mode:
    #     Lead_Consonants_DIC["ㅆ"] = {"+*": "ss", "-*": "ss", "ㄱ": "kss", "ㅂ": "pss"}

    #     Vowels_DIC["ㅑ"] = {"+*": "ya"}
    #     Vowels_DIC["ㅖ"] = {"+*": "ye"}
    #     Vowels_DIC["ㅒ"] = {"+*": "ye"}
    #     Vowels_DIC["ㅛ"] = {"+*": "yo"}
    #     Vowels_DIC["ㅠ"] = {"+*": "yu"}
    #     Vowels_DIC["ㅕ"] = {"+*": "yeo"}

    #     Vowels_DIC["ㅟ"] = {"+*": "i"}
    #     Vowels_DIC["ㅚ"] = {"+*": "e"}

    #     Vowels_DIC["ㅘ"] = {"+*": "wa"}
    #     Vowels_DIC["ㅚ"] = {"+*": "we"}
    #     Vowels_DIC["ㅞ"] = {"+*": "we"}
    #     Vowels_DIC["ㅙ"] = {"+*": "we"}
    #     Vowels_DIC["ㅟ"] = {"+*": "wi"}
    #     Vowels_DIC["ㅝ"] = {"+*": "weo"}

    #     Vowels_DIC["ㅢ"] = {"+*": "eui"}

    # return Lead_Consonants_DIC, Vowels_DIC, Tail_Consonants_DIC

    result = []

    result.extend(pre_regex_list)
    result.extend(lead_consonants_process_regex_list)
    result.extend(vowels_process_regex_list)
    result.extend(tail_consonants_process_regex_list)
    result.extend(post_regex_list)

    return result
