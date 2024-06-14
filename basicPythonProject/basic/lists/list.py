

def test_list(name):
    # way1:
    demo_list = ["test", "wendy", False, 1]
    print(demo_list)
    ## built_in
    len(demo_list)

    #way2:
    tasks = list(range(1, 3))
    print(tasks)

    # change value
    print(demo_list[1])
    demo_list[1] = "hh"
    print(demo_list)

    ## index
    print(demo_list[-1])

    # check if value in list
    print("hh" in demo_list)
    print(3.2 in demo_list)

    string_list = ["huhu", "meimei", "bpbo"]
    # iterate over list
    for str in string_list:
        print("haha " + str)
    # i = 0
    # while i < len(string_list):
    #     print(string_list[i])
    #     i += 1

    ## List methods: different type, append, extend, insert
    first_list = [1, 3, 5, 4, 8, 9]
    first_list.append("jiji")
    print(first_list)
    first_list.extend([3, 5, "yesyes"])
    print(first_list)
    ## insert
    first_list.insert(0, "ticket")
    print(first_list)
    first_list.insert(len(first_list), "kokooo")
    print(first_list)

    ## List methods: clear, pop, remove
    first_list.clear()
    second_list = ["hhh", "jioi", 12, False, "yes"]
    the_element = second_list.pop(1)    ## pop at given index
    print(f"second_list is {second_list}")
    print(f"third_list is {the_element}")
    second_list.pop()
    second_list.remove("hhh")    ## remove element
    print(second_list)

    ## List methods: Index, Count, Reverse, Join
    test_list = [5, 6, 5, 8, 5, 10, 11]
    print(test_list.index(5))
    print(test_list.index(5, 1))   # start from index 1
    print(test_list.count(5))   # how many times
    test_list.reverse()
    print(test_list)
    test_list.sort()
    print(test_list)
    test_str_list = ["we", "are", "the", "champion"]
    test_join1 = " ".join(test_str_list)    # concatenate a base string between each item of iterable
    test_join2 = ", ".join(test_str_list)
    print(test_join1)
    print(test_str_list)    ## unchangeable
    print(test_join2)

    ## Slice [start:end:step]
    slice_list1 = [1, 2, 3, 4, 5, 6, 7]
    print(slice_list1[1:2])
    print(slice_list1)     ## It's copy of list, list not changeable
    print(slice_list1[-2:])
    slice_list2 = slice_list1[0:]
    print(slice_list2 == slice_list1)
    print(slice_list2 is slice_list1)
    ## negative number
    print(slice_list1[:-2])  ## [1, 2]
    ## step
    print(slice_list1[:-1:2])  ## [1, 3, 5]
    print(slice_list1[::2])
    print(slice_list1[1::-1])   ## [2, 1] step back, backawards
    print(slice_list1[::-1])   ## reverse list: [7, 6, 5, 4, 3, 2, 1]
    slice_list3 = ["yes", "no", "meiweiif", "oweifwe"]
    print(slice_list3[2][::-1])  ## fiiewiem
    print(slice_list3[3][:4])  ## owei










# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_list('Hhahahaha')