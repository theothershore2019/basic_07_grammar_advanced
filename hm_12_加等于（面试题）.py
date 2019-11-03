def demo(num, num_list):

    print("函数代码")

    # num = num + num
    num += num

    # 列表变量使用 += 不会做相加再赋值的操作！
    # num_list = num_list + num_list
    # 本质上是在调用列表的 extend 方法
    # num_list.extend(num_list)
    # 由于是调用方法，所以不会修改变量的引用
    # 函数执行结束后，外部数据同样会发生变化
    num_list += num_list

    print(num)
    print(num_list)
    print("函数完成")


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
