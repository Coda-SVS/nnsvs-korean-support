import re
from enum_set import VerboseMode
from jamo import h2j, j2hcj
from hangul_dic import get_phn_dictionary, replace2phn


class g2p4utau(object):
    def __init__(self):
        self.g2p = None
        self.dictionary = get_phn_dictionary(False)
        self.dictionary_label_mode = get_phn_dictionary(True)

    def __call__(self, text: str, use_g2pK: bool = True, descriptive: bool = False, group_vowels: bool = False, labeling_mode: bool = True, verbose: VerboseMode = VerboseMode.NONE):
        if not use_g2pK:
            print("The g2pk option is disabled. Conversion results may contain many errors.")

        if verbose.is_flag(VerboseMode.PARAMETER):
            print("\033[1;96m[Parameter]\033[0m")
            print(f"> use_g2pK = {use_g2pK}")
            print(f"> descriptive = {descriptive}")
            print(f"> group_vowels = {group_vowels}")
            print(f"> labeling_mode = {labeling_mode}")

        text_list = text.splitlines()

        for idx in range(len(text_list)):
            text_list[idx] = text_list[idx].strip()
            text_list[idx] = re.sub(r"[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]", "", text_list[idx])

        text_list = [t for t in text_list if t]

        if len(text_list) == 0:
            return None

        token_phn_list = []
        phn_list = []

        for idx in range(len(text_list)):
            if verbose.is_flag(VerboseMode.INPUT):
                print("\033[1;96m[Input]\033[0m")
                print(text_list[idx])

            if use_g2pK:
                if self.g2p == None:
                    import g2pk

                    self.g2p = g2pk.G2p()

                if verbose.is_flag(VerboseMode.G2PK):
                    print("\033[1;96m[g2pk Processing]\033[0m")

                text_list[idx] = self.g2p(text_list[idx], descriptive=descriptive, group_vowels=group_vowels, verbose=verbose.is_flag(VerboseMode.G2PK))

            jamo_text = j2hcj(h2j(" ".join(text_list[idx])))

            phn_text = replace2phn(self.dictionary_label_mode if labeling_mode else self.dictionary, jamo_text, verbose=verbose)

            inner_token_phn_list = list(filter(lambda phn: phn != "", phn_text.split("  ")))
            token_phn_list.append(inner_token_phn_list)

            inner_phn_list = []
            for token_phn in inner_token_phn_list:
                inner_phn_list.extend(token_phn.split(" "))
            phn_list.append(inner_phn_list)

            if verbose.is_flag(VerboseMode.OUTPUT):
                print("\033[1;96m[Output]\033[0m")
                print(f"> G2P Processed: {text_list[idx]}")
                print(f"> Phoneme List: {', '.join(inner_phn_list)}")
                print(f"> Character Phoneme List: {', '.join(inner_token_phn_list)}")

        return "\n".join(text_list), phn_list, token_phn_list
