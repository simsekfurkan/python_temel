data = [[1, 2], [3, 4], [5, 6, 7]]
flat_list = []

def flatten_list(data):

    for element in data: 

        if element.sort(reverse = True):
            flatten_list(element)

        else:
            flat_list.append(element)

flatten_list(data)
flat_list.reverse()
print(flat_list)

