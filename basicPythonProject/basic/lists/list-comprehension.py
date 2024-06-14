
## list comprehension and nested list
def list_comprehension(name):
    ## List methods: different type, append, extend, insert
    first_list = [1, 3, 5, 4, 8, 9]
    print([x * 10 for x in first_list])
    print(x / 2 for x in first_list)

    name = 'huwefwe'
    print([char.upper() for char in name])
    name_list = ['we', 'are', 'the', 'champion']
    print([name[0].upper() for name in name_list])    ## have name first letter captalized

    ## more examples:
    print([num * 10 for num in range(1, 10)])
    print([str(num) for num in first_list ])
    print([str(num) + "Hello" for num in first_list])

    ## conditional list
    print([num for num in first_list if num % 2 == 0])    ## even
    print([num * 2 if num % 2 == 0 else num / 2 for num in first_list])   ## if else

    with_vowels = "This is so fun!!"
    print([char for char in with_vowels if char not in 'aeiou'])
    print(''.join([char for char in with_vowels if char not in 'aeiou']))

    ## Examples!!!
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    answer = [val for val in list1 if val in list2]
    print(answer)
    # answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
    list2 = ["Elie", "Tim", "Matt"]
    answer2_0 = [name[::-1] for name in list2]     ### slice => reversed
    answer2 = [name.lower() for name in answer2_0]  ## ['eile', 'mit', 'ttam']
    print(answer2)

    ## nested list comprehension
    nested_list = [[1,2,3],[4,5,6],[7,8,9]]
    [[print(val) for val in l] for l in nested_list]
    nested_list0 = [["X" if num % 2 != 0 else "O" for num in range(1, 4)] for val in range(1, 4)]     ## val is number of rows, repeating this list comprehension three times [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]
    print(nested_list0)

    print(["*" for num in range(1, 4)])


    ## make it through

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_comprehension('Hhahahaha')