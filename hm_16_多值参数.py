# 多值参数
# *args  存放元组
# **kwargs   存放字典


def demo(num, *nums, **person):

    print(num)
    print(nums)
    print(person)


demo(1)
demo(1, 2, 3, 4, name="小明", age="18")
