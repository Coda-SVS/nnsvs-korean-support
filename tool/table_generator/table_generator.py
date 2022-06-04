import os
from tqdm import tqdm
from utils import list_chunk
from enunu_kor_tool import g2pk4utau
from tqdm.contrib.concurrent import process_map
from functools import partial

converter = g2pk4utau.g2pk4utau()


def table_generator(table_data, idx):
    result = []
    for char in tqdm(table_data[idx], "Converting..."):
        temp = [char]
        [temp.append(obj) for obj in converter(char)]
        result.append(temp)

    return result


def table_gen_main(
    path="hangul_all.origndic", hangul_output_path="result_hangul.table", phn_output_path="result_phn.table", hangul_phn_output_path="result_phn_hangul.table", chunk_count=12
):
    """
    한글 테이블 생성

    자소 음소 테이블을 생성합니다.
    """

    with open(path, "r", encoding="utf-8") as table_file:
        table_source = table_file.readlines()

    table_source = ("".join(table_source)).replace("\n", "").replace(" ", "")

    source_len = len(table_source)

    print(f"Source count: {source_len}")

    table_source = list_chunk(table_source, chunk_count)

    result_list = process_map(partial(table_generator, table_source), range(len(table_source)), max_workers=len(table_source))

    # 결과물 병합

    temp_obj = []
    for temp in tqdm(result_list, "Merging..."):
        for temp_ in temp:
            temp_obj.append(temp_)
    result_list = temp_obj

    # temp_obj = []
    # post_processed_dic = []
    # for temp in tqdm(result_list, "Post-processing..."):
    #     dup_key = "".join(temp[3])
    #     if dup_key not in post_processed_dic:
    #         post_processed_dic.append(dup_key)
    #         temp_obj.append(temp)
    # result_list = temp_obj

    temp_obj = []
    for temp in tqdm(result_list, "Post-processing..."):
        lst = [temp[0], temp[1]]
        lst.extend(temp[2])
        lst.extend(temp[3])
        temp_obj.append(lst)
    result_list = temp_obj

    # 음소

    result = ""
    for temp in tqdm(result_list, "[Phn] Post-processing..."):
        result += f"{''.join(temp[2])} {' '.join(temp[2])}\n"
    result = result[:-1]

    with open(phn_output_path, "w", encoding="utf-8") as result_file:
        result_file.write(result)

    # 한글

    result = ""
    for temp in tqdm(result_list, "[Han] Post-processing..."):
        result += f"{''.join(temp[0])} {' '.join(temp[2])}\n"
    result = result[:-1]

    with open(hangul_output_path, "w", encoding="utf-8") as result_file:
        result_file.write(result)

    # 한글 + 음소

    result = ""
    for temp in tqdm(result_list, "[H+P] Post-processing..."):
        result += f"{''.join(temp[0])}_{''.join(temp[2])} {' '.join(temp[2])}\n"
    result = result[:-1]

    with open(hangul_phn_output_path, "w", encoding="utf-8") as result_file:
        result_file.write(result)

    result_len = len(result.split("\n"))

    print(f"{source_len} {result_len}")
    print("done.")


def table_simplify_main(path="hangul_all.origndic", output_path="result_hangul.origndic", chunk_count=12):
    """
    한글 테이블 축소

    음절끝소리 규칙 등으로 발음(음소)이 겹치는 자소를 제거합니다.

    단, g2p 모듈에 따라 결과가 달라질 수 있습니다.
    """

    with open(path, "r", encoding="utf-8") as table_file:
        table_source = table_file.readlines()

    table_source = ("".join(table_source)).replace("\n", "").replace(" ", "")

    source_len = len(table_source)

    print(f"Source count: {source_len}")

    table_source = list_chunk(table_source, chunk_count)

    result_list = process_map(partial(table_generator, table_source), range(len(table_source)), max_workers=len(table_source))

    temp_obj = []
    for temp in tqdm(result_list, "Merging..."):
        for temp_ in temp:
            temp_[3] = "".join(temp_[3])
            temp_obj.append(temp_)
    result_list = temp_obj

    post_processed = ""
    post_processed_dic = []
    for temp in tqdm(result_list, "Post-processing..."):
        if temp[3] not in post_processed_dic:
            post_processed_dic.append(temp[3])
            post_processed += temp[1]

    with open(output_path, "w", encoding="utf-8") as result_file:
        result_file.write(post_processed)

    result_len = len(post_processed)

    print(f"{source_len} {len(result_list)} {result_len}")
    print("done.")


def table_gen2_main(
    path="hangul_all.origndic", hangul_output_path="result_hangul.table", phn_output_path="result_phn.table", hangul_phn_output_path="result_phn_hangul.table", chunk_count=12
):
    """
    한글 테이블 생성

    자소 음소 테이블을 생성합니다.
    자소 음소 테이블을 생성합니다.
    """

    with open(path, "r", encoding="utf-8") as table_file:
        table_source = table_file.readlines()

    table_source = ("".join(table_source)).replace("\n", "").replace(" ", "")

    source_len = len(table_source)

    print(f"Source count: {source_len}")

    table_source = list_chunk(table_source, chunk_count)

    result_list = process_map(partial(table_generator, table_source), range(len(table_source)), max_workers=len(table_source))

    # 결과물 병합

    temp_obj = []
    for temp in tqdm(result_list, "Merging..."):
        for temp_ in temp:
            temp_obj.append(temp_)
    result_list = temp_obj

    # temp_obj = []
    # post_processed_dic = []
    # for temp in tqdm(result_list, "Post-processing..."):
    #     dup_key = "".join(temp[3])
    #     if dup_key not in post_processed_dic:
    #         post_processed_dic.append(dup_key)
    #         temp_obj.append(temp)
    # result_list = temp_obj

    temp_obj = []
    for temp in tqdm(result_list, "Post-processing..."):
        lst = [temp[0], temp[1]]
        lst.extend(temp[2])
        lst.extend(temp[3])
        temp_obj.append(lst)
    result_list = temp_obj

    # 음소

    result = ""
    for temp in tqdm(result_list, "[Phn] Post-processing..."):
        result += f"{''.join(temp[2])} {' '.join(temp[2])}\n"
    result = result[:-1]

    with open(phn_output_path, "w", encoding="utf-8") as result_file:
        result_file.write(result)

    # 한글

    result = ""
    for temp in tqdm(result_list, "[Han] Post-processing..."):
        result += f"{''.join(temp[0])} {' '.join(temp[2])}\n"
    result = result[:-1]

    with open(hangul_output_path, "w", encoding="utf-8") as result_file:
        result_file.write(result)

    # 한글 + 음소

    result = ""
    for temp in tqdm(result_list, "[H+P] Post-processing..."):
        result += f"{''.join(temp[0])}_{''.join(temp[2])} {' '.join(temp[2])}\n"
    result = result[:-1]

    with open(hangul_phn_output_path, "w", encoding="utf-8") as result_file:
        result_file.write(result)

    result_len = len(result.split("\n"))

    print(f"{source_len} {result_len}")
    print("done.")


if __name__ == "__main__":
    base_path = "tool/table_generator"

    table_gen_main_path = [os.path.join(base_path, path) for path in ["hangul_all.origndic", "result_hangul.table", "result_phn.table", "result_phn_hangul.table"]]

    # table_simplify_main()
    # table_gen_main(table_gen_main_path[0], table_gen_main_path[1], table_gen_main_path[2], table_gen_main_path[3])
    table_gen2_main(table_gen_main_path[0], table_gen_main_path[1], table_gen_main_path[2], table_gen_main_path[3])


# '가', '가', 'ㄱㅏ', ['g', 'a'], ['ga']
