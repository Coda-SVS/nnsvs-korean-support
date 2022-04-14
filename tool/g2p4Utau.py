import re
from jamo import h2j, j2hcj
from hangul_dic import get_phn_dictionary, Vowels_LIST


class g2p4Utau(object):
    def __init__(self):
        self.g2p = None
        self.set_dictionary_mode()

    def set_dictionary_mode(self, labeling_mode: bool = True):
        self.dictionary = get_phn_dictionary(labeling_mode)

    def __call__(self, text: str, use_g2pK: bool = True, descriptive: bool = False, group_vowels: bool = False):
        text_list = text.split("\n")

        for idx in range(len(text_list)):
            text_list[idx] = re.sub(r"[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]", "", text_list[idx])

        text_list = [t for t in text_list if t]

        if len(text_list) == 0:
            return None

        phn_list = []
        token_phn_list = []
        for idx in range(len(text_list)):
            if use_g2pK:
                if self.g2p == None:
                    import g2pk

                    self.g2p = g2pk.G2p()

                text_list[idx] = self.g2p(text_list[idx], descriptive=descriptive, group_vowels=group_vowels)

            before_jamo = ""
            for token in text_list[idx]:
                if token == " " or token == "\n":
                    continue

                token_jamo = j2hcj(h2j(token))

                token_phn = ""
                for idx, jamo in enumerate(token_jamo):
                    phn = self.replace_jamo(idx, jamo, before_jamo)

                    if phn != "":
                        for ph in phn.split(" "):
                            phn_list.append(ph)
                            token_phn += ph

                    before_jamo = jamo

                if token_phn != "":
                    token_phn_list.append(token_phn)

        return "\n".join(text_list), phn_list, token_phn_list

    def replace_jamo(self, idx: int, jamo: str, before_jamo: str = ""):
        jamo_dic = self.dictionary[idx][jamo]

        if before_jamo in jamo_dic.keys():
            return jamo_dic[before_jamo]
        else:
            if before_jamo == "":
                if idx == 0:
                    prefix = "+*"
                elif idx == 1:
                    prefix = "+*"
                else:
                    prefix = "-*"
            else:
                if before_jamo in Vowels_LIST:
                    prefix = "-*"
                else:
                    prefix = "+*"

            return jamo_dic[prefix]


if __name__ == "__main__":
    tester = g2p4Utau()

    def pretty_print(obj):
        print(f"> G2P Processed: {obj[0]}")
        print(f"> Phoneme List: {', '.join(obj[1])}")
        print(f"> Character Phoneme List: {', '.join(obj[2])}")

    text = "안녕하세요\n둥근 해가 떴습니다\n바깥 공기가 상쾌하다\n의사 선생님\n악수를 합시다"

    for text_token in text.split("\n"):
        print("라벨링: True")
        pretty_print(tester(text_token))
        tester.set_dictionary_mode(False)
        print()
        print("라벨링: False")
        pretty_print(tester(text_token))
        tester.set_dictionary_mode(True)
        print("\n#############################\n")

    # while True:
    #     try:
    #         text = input()
    #     except KeyboardInterrupt:
    #         print("Done.")
    #         break

    #     pretty_print(tester(text))
    #     tester.set_dictionary_mode(False)
    #     pretty_print(tester(text))
    #     tester.set_dictionary_mode(True)

    # print(tester("Test"))

############################ My Test Case ############################
# print(tester("""재밌어"""))
# print(tester("빙그르르"))
# print(
#     tester(
#         """에이 비 씨 디 이 에프 지
# 에이치 아이 제이 케이 엘 엠 엔
# 오 피 큐 알 에스 티 유
# 브이 더블유 엑스 와이 지

# 우리 모두 다 함께
# 에이 비 씨 디 불러요

# 에이 비 씨 디 이 에프 지
# 에이치 아이 제이 케이 엘 엠 엔
# 오 피 큐 알 에스 티 유
# 브이 더블유 엑스 와이 지

# 친구들과 다 함께
# 에이 비 씨 디 재밌어"""
#     )
# )
# print(
#     tester(
#         """애, 얘, 외, 왜, 에, 예, 웨, 웨"""
#         # """ㅐ, ㅒ, ㅚ, ㅙ, ㅔ, ㅖ, ㅞ, ㅞ"""
#     )
# )

# print(tester("""긔"""))

# print(
#     tester(
#         """
# 가 갸 거 겨 고 교 구 규 그 기 게 계 과 궈 귀 궤 긔
# 나 냐 너 녀 노 뇨 누 뉴 느 니 네 녜 놔 눠 뉘 눼 늬
# 다 댜 더 뎌 도 됴 두 듀 드 디 데 뎨 돠 둬 뒤 뒈 듸
# 라 랴 러 려 로 료 루 류 르 리 레 례 롸 뤄 뤼 뤠 릐
# 마 먀 머 며 모 묘 무 뮤 므 미 메 몌 뫄 뭐 뮈 뭬 믜
# 바 뱌 버 벼 보 뵤 부 뷰 브 비 베 볘 봐 붜 뷔 붸 븨
# 사 샤 서 셔 소 쇼 수 슈 스 시 세 셰 솨 숴 쉬 쉐 싀
# 아 야 어 여 오 요 우 유 으 이 에 예 와 워 위 웨 의
# 자 쟈 저 져 조 죠 주 쥬 즈 지 제 졔 좌 줘 쥐 줴 즤
# 차 챠 처 쳐 초 쵸 추 츄 츠 치 체 쳬 촤 춰 취 췌 츼
# 카 캬 커 켜 코 쿄 쿠 큐 크 키 케 켸 콰 쿼 퀴 퀘 킈
# 타 탸 터 텨 토 툐 투 튜 트 티 테 톄 톼 퉈 튀 퉤 틔
# 파 퍄 퍼 펴 포 표 푸 퓨 프 피 페 폐 퐈 풔 퓌 풰 픠
# 하 햐 허 혀 호 효 후 휴 흐 히 헤 혜 화 훠 휘 훼 희
# 까 꺄 꺼 껴 꼬 꾜 꾸 뀨 끄 끼 께 꼐 꽈 꿔 뀌 꿰 끠
# 따 땨 떠 뗘 또 뚀 뚜 뜌 뜨 띠 떼 뗴 똬 뚸 뛰 뛔 띄
# 빠 뺘 뻐 뼈 뽀 뾰 뿌 쀼 쁘 삐 뻬 뼤 뽜 뿨 쀠 쀄 쁴
# 싸 쌰 써 쎠 쏘 쑈 쑤 쓔 쓰 씨 쎄 쎼 쏴 쒀 쒸 쒜 씌
# 짜 쨔 쩌 쪄 쪼 쬬 쭈 쮸 쯔 찌 쩨 쪠 쫘 쭤 쮜 쮀 쯰
# 악 억 옥 욱 윽 익 엑
# 안 언 온 운 은 인 엔
# 앋 얻 옫 욷 읃 읻 엗
# 알 얼 올 울 을 일 엘
# 암 엄 옴 움 음 임 엠
# 압 업 옵 웁 읍 입 엡
# 앙 엉 옹 웅 응 잉 엥
# """
#     )
# )

# print(
#     tester(
#         """우리 법령 속에도 어려운 한자어나 일상에서 쓰지 않는 일본식 용어, 외래어가 많이 담겨 있다.
# 게다가 문장까지 복잡한 경우도 많다."""
#     )
# )

# print(
#     tester(
#         """
# 있\n
# 있어\n
# 있기\n
# """
#     )
# )

# print(
#     tester(
#         """
# 악 억 옥 욱 윽 익 엑
# 안 언 온 운 은 인 엔
# 앋 얻 옫 욷 읃 읻 엗
# 알 얼 올 울 을 일 엘
# 암 엄 옴 움 음 임 엠
# 압 업 옵 웁 읍 입 엡
# 앙 엉 옹 웅 응 잉 엥
#     """
#     )
# )
