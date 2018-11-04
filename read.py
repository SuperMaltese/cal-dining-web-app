def read(b='', c='', d =''):
    text_file = open("index.csv")
    lines = text_file.read().split('\r\n')
    text_file.close

    halls = ['Cafe_3', 'Clark_Kerr_Campus', 'Foothill', 'Crossroads']
    meals = ['Breakfast', 'Brunch', 'Lunch', 'Dinner']

    def print_until(delimiter_lst, foods_lst):
        index = 0
        while index < len(foods_lst):
            if foods_lst[index] in delimiter_lst:
                break
            index = index + 1
            #print(foods_lst[index])
        return foods_lst[:index]

    def choose(lst, keyword, constraints):
        index = 0
        while index < len(lst): #if cafe_3 
            if keyword == lst[index]:
                break
            index = index + 1
        modified = [x for x in constraints if x!=keyword]
        return print_until(modified, lst[index:])

    def filter(lst, hall = '', meal = '', dish = ''):
        reduced_lst = choose(lst, hall, halls)
        reduced_lst = choose(reduced_lst, meal, meals)
        # reduced_lst = choose(reduced_lst, dish, [])
        return reduced_lst

    return filter(lines, b, c, d)