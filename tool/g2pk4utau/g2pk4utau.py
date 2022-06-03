import re
from enum_set import VerboseMode
from jamo import h2j, j2hcj
from hangul_dic import get_phn_dictionary, replace2phn


class g2pk4utau(object):
    def __init__(self):
        self.g2p = None
        self.empty_str_remover = lambda text: not text.isspace()
        self.dictionary = get_phn_dictionary(False)
        self.dictionary_label_mode = get_phn_dictionary(True)

    def __call__(
        self,
        text: str,
        use_g2pK: bool = True,
        descriptive: bool = False,
        group_vowels: bool = False,
        labeling_mode: bool = True,
        verbose: VerboseMode = VerboseMode.NONE,
    ):
        if not use_g2pK:
            print("The g2pk option is disabled. Conversion results may contain many errors.")

        if verbose.is_flag(VerboseMode.PARAMETER):
            print("\033[1;96m[Parameter]\033[0m")
            print(f"> use_g2pK = {use_g2pK}")
            print(f"> descriptive = {descriptive}")
            print(f"> group_vowels = {group_vowels}")
            print(f"> labeling_mode = {labeling_mode}")

        # 여러 줄의 입력 처리
        text_list = text.splitlines()

        # 앞뒤공백 제거, 특수문자 제거
        for idx in range(len(text_list)):
            text_list[idx] = text_list[idx].strip()
            text_list[idx] = re.sub(r"[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]", "", text_list[idx])
            # 공백을 구분자로 사용하므로, 불필요한 2개 이상의 공백을 제거 (단어는 공백 3개, 문자는 공백 2개로 구분)
            text_list[idx] = re.sub(r"\s{2,}|\t", r" ", text_list[idx])

        # 비어있는 문자열 제거
        text_list = list(filter(lambda t: not t.isspace(), text_list))

        # 전처리 후 입력 문자열이 없을 경우
        if len(text_list) == 0:
            return "", [], []

        phn_list = []
        token_phn_list = []
        word_phn_list = []

        for idx in range(len(text_list)):
            if verbose.is_flag(VerboseMode.INPUT):
                print("\033[1;96m[Input]\033[0m")
                print(text_list[idx])

            # g2pk로 전처리
            if use_g2pK:
                if self.g2p == None:
                    import g2pk

                    self.g2p = g2pk.G2p()

                if verbose.is_flag(VerboseMode.G2PK):
                    print("\033[1;96m[g2pk Processing]\033[0m")

                text_list[idx] = self.g2p(text_list[idx], descriptive=descriptive, group_vowels=group_vowels, verbose=verbose.is_flag(VerboseMode.G2PK))

            # 자모 분리
            jamo_text = j2hcj(h2j(" ".join(text_list[idx])))

            # 사전을 바탕으로 로마자 음소로 변환
            phn_text = replace2phn(self.dictionary_label_mode if labeling_mode else self.dictionary, jamo_text, verbose=verbose)

            # 단어 단위 묶음
            inner_word_phn_list = list(filter(self.empty_str_remover, phn_text.split("   ")))
            for phn_word in inner_word_phn_list:
                phn_tokens = list(filter(self.empty_str_remover, [phn_tokens.strip() for phn_tokens in phn_word.split("  ")]))
                word_phn_list.append(phn_tokens)

            # 글자 단위 묶음
            for phn_word in word_phn_list:
                token_phn_list.extend(phn_word)

            # 음소 단위 묶음
            for token_phn in token_phn_list:
                for phn in token_phn.split(" "):
                    phn_list.append(phn)

            if verbose.is_flag(VerboseMode.OUTPUT):
                print("\033[1;96m[Output]\033[0m")
                print(f"> G2P Processed: {text_list[idx]}")
                word_phn_temp_list = []
                for tokens in word_phn_list:
                    word_phn_temp_list.append("\033[1;32m,\033[0m ".join(tokens))
                temp_output = "\033[1;33m(\033[0m" + "\033[1;33m) (\033[0m".join(word_phn_temp_list) + "\033[1;33m)\033[0m"
                print(f"> Word Phoneme List: {temp_output}")
                temp_output = "\033[1;32m,\033[0m ".join(token_phn_list)
                print(f"> Character Phoneme List: {temp_output}")
                temp_output = "\033[1;32m,\033[0m ".join(phn_list)
                print(f"> Phoneme List: {temp_output}")

        return "\n".join(text_list), phn_list, token_phn_list, word_phn_list
