# Source of this code: https://github.com/r9y9/nnsvs/pull/81

from nnmnkwii.io import hts


def dim_count(hed_file_path: str = "tool\\hed_generator\\result_question_generator.hed"):
    binary_dict, continuous_dict = hts.load_question_set(hed_file_path)
    in_rest_idx = 0
    in_lfx0_idx = 0

    for n in range(len(binary_dict)):
        if binary_dict[n][0] == "C-Phone_Muon":
            in_rest_idx = n
            print("in_rest_idx:", in_rest_idx)
            break

    for n in range(len(continuous_dict)):
        if continuous_dict[n][0] == "e1":  # the absolute pitch of the current note
            in_lfx0_idx = n + len(binary_dict)
            print("in_lfx0_idx:", in_lfx0_idx)
            break

    return in_rest_idx, in_lfx0_idx


if __name__ == "__main__":
    dim_count()
