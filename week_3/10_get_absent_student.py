all_students = ["초롱", "보미", "은지", "나은", "남주", "하영"]
present_students = ["보미", "은지", "나은", "남주", "하영"]


def get_absent_student(all_array, present_array):
    dict = {}
    for key in all_array:
        dict[key] = True

    for key in present_array:
        del dict[key]

    for key in dict.keys():
        return key


print(get_absent_student(all_students, present_students))