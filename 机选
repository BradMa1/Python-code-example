import random

def generate_random_numbers(num_groups, num_per_group_front, num_per_group_back, min_value_front, max_value_front, min_value_back, max_value_back):
    """
    生成指定数量的随机数组合。

    :param num_groups: 要生成的随机数组的数量
    :param num_per_group_front: 前区每个数组中的数字数量
    :param num_per_group_back: 后区每个数组中的数字数量
    :param min_value_front: 前区随机数的最小值
    :param max_value_front: 前区随机数的最大值
    :param min_value_back: 后区随机数的最小值
    :param max_value_back: 后区随机数的最大值
    :return: 包含随机数组的列表
    """
    random_groups = []
    for _ in range(num_groups):
        front_group = random.sample(range(min_value_front, max_value_front + 1), num_per_group_front)
        back_group = random.sample(range(min_value_back, max_value_back + 1), num_per_group_back)
        random_groups.append((front_group, back_group))
    return random_groups

# 示例：生成7组随机数，前区每组5个数字，范围是0到30；后区每组2个数字，范围是0到12
num_groups = 5
num_per_group_front = 5
num_per_group_back = 2
min_value_front = 0
max_value_front = 30
min_value_back = 0
max_value_back = 12

random_numbers = generate_random_numbers(num_groups, num_per_group_front, num_per_group_back, min_value_front, max_value_front, min_value_back, max_value_back)

# 将每组数据的前5个和后2个分开
for i, (front_group, back_group) in enumerate(random_numbers, 1):
    print(f"第{i}组 - 前区: {front_group}, 后区: {back_group}")
