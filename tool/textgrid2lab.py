import os
import textgrid
from tqdm import tqdm
from glob import glob

nano_sec = 10_000_000

input_dir = "CSD/output"

file_list = sorted(glob(os.path.join(input_dir, "**/*.TextGrid")))

for file_name in tqdm(file_list):
    tg = textgrid.TextGrid.fromFile(file_name)

    for item in tg:
        if item.name != "phones":
            continue
        else:
            dir, file_name_ = os.path.split(file_name)
            fname, fext = os.path.splitext(file_name_)
            dir = os.path.join("output_lab", dir)
            save_path = os.path.join(dir, f"{fname}.lab")

            os.makedirs(dir, exist_ok=True)

            outf = open(save_path, "w")
            inf = open(file_name)

            for phn_item in item:
                # print(phn_item.minTime)
                # print(phn_item.maxTime)
                # print(phn_item.mark)

                xmin = int(phn_item.minTime * nano_sec)
                xmax = int(phn_item.maxTime * nano_sec)
                text = "pau" if phn_item.mark == "" else phn_item.mark

                outf.write(f"{xmin} {xmax} {text}\n")

            outf.close()
            inf.close()
