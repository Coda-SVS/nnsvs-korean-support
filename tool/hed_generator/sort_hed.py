path = input("path: ").strip('"')

with open(path, "r") as f:
    lines = f.readlines()

lines.sort()

path = path.replace(".hed", "") + "_sorted.hed"

with open(path, "w") as f:
    f.writelines(lines)
