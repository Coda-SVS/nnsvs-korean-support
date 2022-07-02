#! /usr/bin/env python3
# coding: utf-8
# Copyright (c) 2020 oatsu
"""
NNSVS用のquestionを生成するやつ
"""
import os
import json
from dim_counter import dim_count


def str_phone_questions(list_all_phonemes, dict_phoneme_classification, mode):
    """
    list_all_phoneme : 全音素のリスト
    dict_phoneme_classification : 音素分類をした辞書のリスト。
    {
     分類名: [音素, 音素, ... ],
     分類名: [音素, ...]
    }
    mode : 'LL', 'L', 'C', 'R', 'RR' のいずれかを選択
    """
    # フルコンテキストラベルから検出するための左右の文字列
    d = {"LL": ("*@", "^*"), "L": ("*^", "-*"), "C": ("*-", "+*"), "R": ("*+", "=*"), "RR": ("*=", "_*")}
    sign_1, sign_2 = d[mode]

    # 1行分の文字列のリスト。改行文字なし。
    lines = {"book": [], "single": []}
    book_pad = 54
    single_pad = 29

    # 音素の分類質問を行に追加
    for key, l_val in dict_phoneme_classification.items():
        # キーの文字列
        if key == "Silence":
            s1 = f'"{mode}-{key}"'.ljust(book_pad, " ")
        else:
            s1 = f'"{mode}-Phone_{key}"'.ljust(book_pad, " ")
        # 値の文字列
        s2 = "{" + ",".join(f"{sign_1}{ph}{sign_2}" for ph in l_val) + "}"
        # くっつける
        line = " ".join(("QS", s1, s2))
        # 行のリストに追加
        lines["book"].append(line)

    # 全音素の質問を行に追加
    for ph in list_all_phonemes:
        s1 = f'"{mode}-Phone_{ph}"'.ljust(single_pad, " ")
        s2 = "{" + f"{sign_1}{ph}{sign_2}" + "}"
        line = " ".join(("QS", s1, s2))
        lines["single"].append(line)

    return lines


def str_fixed_qs_and_cqs():
    """
    音素とは関係なく必ず追加する文字列を返す
    """
    s = (
        "# The following was copied from the NNSVS hed\n"
        "\n# absolute pitch (L/C/R)\n"
        'CQS "d1_absolute_pitch"                    {/D:(\\NOTE)!}\n'
        'CQS "e1_absolute_pitch"                    {/E:(\\NOTE)]}\n'
        'CQS "f1_absolute_pitch"                    {/F:(\\NOTE)#}\n'
        "\n# relative pitch (L/C/R)\n"
        'CQS "d2_relative_pitch"                    {!(\\d+)#}\n'
        'CQS "e2_relative_pitch"                    {](\\d+)^}\n'
        'CQS "f2_relative_pitch"                    {#(\\d+)#}\n'
        "\n# phoneme-level positional features (C)\n"
        'CQS "p12_position"                         {-(\\d+)!}\n'
        'CQS "p13_position"                         {!(\\d+)[}\n'
        "\n# distance between consonant and vowel\n"
        'CQS "p14_distance_from_vowel"              {[(\\d+)$}\n'
        'CQS "p15_distance_from_vowel"              {$(\\d+)]}\n'
        "\n# number of phonemes in a syllable (L/C/R)\n"
        'CQS "a1_number_of_phonemes"                {/A:(\\d+)-}\n'
        'CQS "b1_number_of_phonemes"                {/B:(\\d+)_}\n'
        'CQS "c1_number_of_phonemes"                {/C:(\\d+)+}\n'
        "\n# syllable potional features (L/C/R)\n"
        'CQS "a2_position"                          {-(\\d+)-}\n'
        'CQS "a3_position"                          {-(\\d+)@}\n'
        'CQS "b2_position"                          {_(\\d+)_}\n'
        'CQS "b3_position"                          {_(\\d+)@}\n'
        'CQS "c2_position"                          {+(\\d+)+}\n'
        'CQS "c3_position"                          {+(\\d+)@}\n'
        "\n# length of current note (C)\n"
        'CQS "e6_length_by_syllable"                {!(\\d+)@}\n'
        'CQS "e7_length_by_10ms"                    {@(\\d+)#}\n'
        'CQS "e8_length_by_96th_note"               {#(\\d+)+}\n'
        "\n# length of previous note (L)\n"
        'CQS "d6_length_by_syllable"                {|(\\d+)&}\n'
        'CQS "d7_length_by_10ms"                    {&(\\d+);}\n'
        'CQS "d8_length_by_96th_note"               {;(\\d+)-}\n'
        "\n# length of next note (R)\n"
        'CQS "f6_length_by_syllable"                {$(\\d+)+}\n'
        'CQS "f7_length_by_10ms"                    {+(\\d+)%}\n'
        'CQS "f8_length_by_96th_note"               {%(\\d+);}\n'
        "\n# note-level positional features in measures (C)\n"
        'CQS "e10_position_by_note_in_measure"      {](\\d+)$}\n'
        'CQS "e11_position_by_note_in_measure"      {$(\\d+)|}\n'
        'CQS "e12_position_by_10ms_in_measure"      {|(\\d+)[}\n'
        'CQS "e13_position_by_10ms_in_measure"      {[(\\d+)&}\n'
        'CQS "e14_position_by_96th_note_in_measure" {&(\\d+)]}\n'
        'CQS "e15_position_by_96th_note_in_measure" {](\\d+)=}\n'
        'CQS "e16_position_by_percent_in_measure"   {=(\\d+)^}\n'
        'CQS "e17_position_by_percent_in_measure"   {^(\\d+)~}\n'
        "\n# note-level positional features in phrase (C)\n"
        'CQS "e18_position_by_note"                 {~(\\d+)#}\n'
        'CQS "e19_position_by_note"                 {#(\\d+)_}\n'
        'CQS "e20_position_by_10ms"                 {_(\\d+);}\n'
        'CQS "e21_position_by_10ms"                 {;(\\d+)$}\n'
        'CQS "e22_position_by_96th_note"            {$(\\d+)&}\n'
        'CQS "e23_position_by_96th_note"            {&(\\d+)%}\n'
        'CQS "e24_position_by_percent"              {%(\\d+)[}\n'
        'CQS "e25_position_by_percent"              {[(\\d+)|}\n'
        "\n# pitch diff\n"
        'CQS "e57" {~([pm]\\d+)+}\n'
        'CQS "e58" {+([pm]\\d+)!}'
    )
    return s


def main():
    dic_filename = "config.json"

    with open(os.path.join("tool", "hed_generator", dic_filename), mode="r", encoding="utf-8") as fj:
        d_json = json.load(fj)

    list_all_phonemes = d_json["all_phonemes"]
    dict_phoneme_classification = d_json["phoneme_classification"]

    l_lines = str_phone_questions(list_all_phonemes, dict_phoneme_classification, mode="L")
    c_lines = str_phone_questions(list_all_phonemes, dict_phoneme_classification, mode="C")
    r_lines = str_phone_questions(list_all_phonemes, dict_phoneme_classification, mode="R")

    s = ""
    for l, c, r in zip(l_lines["book"], c_lines["book"], r_lines["book"]):
        s += f"{l}\n"
        s += f"{c}\n"
        s += f"{r}\n"
        s += "\n"
    for l, c, r in zip(l_lines["single"], c_lines["single"], r_lines["single"]):
        s += f"{l}\n"
        s += f"{c}\n"
        s += f"{r}\n"
    s += "\n"
    s += str_fixed_qs_and_cqs()

    hed_file_path = "tool\\hed_generator\\korean_question.hed"

    with open(hed_file_path, mode="w", encoding="utf-8") as ft:
        ft.write(s)

    in_rest_idx, in_lfx0_idx, count_dim = dim_count(hed_file_path)

    with open(hed_file_path, mode="w", encoding="utf-8") as ft:
        lines = s.splitlines(keepends=False)
        lines.insert(0, f"# feature dim: {count_dim + 4} for acoustic model, {count_dim} for duration/timelag")
        lines.insert(1, f"# in_rest_idx: {in_rest_idx}\n# in_lfx0_idx: {in_lfx0_idx}\n")
        ft.write("\n".join(lines))


if __name__ == "__main__":
    main()
