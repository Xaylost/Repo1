import random
bitmap =[{'r':random.randint(0,255),'g':random.randint(0,255),'b':random.randint(0,255)} for i in range(20000)]
def find_colour(colours):
    list_of_colours = []
    for colour in colours:
        if colour['r'] > colour['g'] and colour['r'] > colour['b']:
            list_of_colours.append('red')
        elif colour['g'] > colour['r'] and colour['g'] > colour['b']:
            list_of_colours.append('green')
        elif colour['b'] > colour['r'] and colour['b'] > colour['g']:
            list_of_colours.append('blue')
    return list_of_colours
def most_frequent(lst):
    count = {}
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    max_count = 0
    most_frequent_num = None
    for key, value in count.items():
        if value > max_count:
            max_count = value
            most_frequent_num = key
    return most_frequent_num

print(f'Самый используемый цвет: {most_frequent(find_colour(bitmap))}')