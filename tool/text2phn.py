import os
import re
from tqdm import tqdm
from enunu_kor_tool import g2pk4utau

converter = g2pk4utau.g2pk4utau()


def convert(table_data: dict, text: str, use_g2p4utau=True):

    if use_g2p4utau:
        text = converter(text)[0]

    text = re.sub(r"[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》 \n]", "", text)

    result = []
    for char in tqdm(text, "Converting..."):
        char = table_data[char]
        result.append(char)

    return result


def table_loader(table_path: str):
    table_data = {}

    with open(table_path, mode="r", encoding="utf-8") as file:
        data = file.readlines()

    for line in tqdm(data, "Table data loading..."):
        line: str
        line = line.split(sep=" ", maxsplit=1)
        table_data[line[0]] = line[1].strip()

    return table_data


if __name__ == "__main__":

    use_g2p4utau = True
    table_data = table_loader("../table/result_hangul.table")
    directory_path = "Text_Source"

    for filename in os.listdir(directory_path):
        filename = os.path.join(directory_path, filename)

        with open(filename, mode="r", encoding="utf-8") as file:
            text = file.read()

        text = convert(table_data, text, use_g2p4utau)

        fname, fext = os.path.splitext(filename)

        with open(f"{fname}_phn{fext}", mode="w", encoding="utf-8") as file:
            file.write(" ".join(text))
