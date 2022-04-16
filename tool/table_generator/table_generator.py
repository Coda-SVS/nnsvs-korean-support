from tqdm import tqdm
from g2p4utau import g2p4utau
from tqdm.contrib.concurrent import process_map
from functools import partial


def table_generator(table_data, idx):
    converter = g2p4utau()

    result = []
    for char in tqdm(table_data[idx], "Converting..."):
        temp = [char]
        [temp.append(obj) for obj in converter(char, False)]
        result.append(temp)

    return result


def list_chunk(lst, n: int):
    count = len(lst) // n
    result = [lst[i * count : i * count + count] for i in range(0, n)]

    if isinstance(lst, list):
        for temp in lst[count * n :]:
            result[n - 1].append(temp)
    else:
        for temp in lst[count * n :]:
            result[n - 1] += temp
    return result


def table_gen_main(
    path="result_hangul.origndic", hangul_output_path="result_hangul.table", phn_output_path="result_phn.table", hangul_phn_output_path="result_phn_hangul.table", chunk_count=12
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
        temp_obj.append(temp)
    result_list = temp_obj

    # 음소

    result = ""
    for temp in tqdm(result_list, "[Phn] Post-processing..."):
        result += f"{''.join(temp[3])} {' '.join(temp[3])}\n"
    result = result[:-1]

    with open(phn_output_path, "w", encoding="utf-8") as result_file:
        result_file.write(result)

    # 한글

    result = ""
    for temp in tqdm(result_list, "[Han] Post-processing..."):
        result += f"{''.join(temp[0])} {' '.join(temp[3])}\n"
    result = result[:-1]

    with open(hangul_output_path, "w", encoding="utf-8") as result_file:
        result_file.write(result)

    # 한글 + 음소

    result = ""
    for temp in tqdm(result_list, "[H+P] Post-processing..."):
        result += f"{''.join(temp[0])}_{''.join(temp[3])} {' '.join(temp[3])}\n"
    result = result[:-1]

    with open(hangul_phn_output_path, "w", encoding="utf-8") as result_file:
        result_file.write(result)

    result_len = len(result.split("\n"))

    print(f"{source_len} {result_len}")
    print("done.")


def table_simplify_main(path="hangul.origndic", output_path="result_hangul.origndic", chunk_count=12):
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


if __name__ == "__main__":
    # table_simplify_main()
    table_gen_main()


# '가', '가', 'ㄱㅏ', ['g', 'a'], ['ga']
