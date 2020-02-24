def switch_tuple_values(tuples_list):
    if not isinstance(tuples_list, list):
        raise TypeError('arg must be a list')

    new_tuples_list = []
    for tup in tuples_list:
        if not isinstance(tup, tuple):
            raise TypeError('all elements must be tuples')

        if len(tup) != 2:
            raise ValueError('all tuples must have length 2')
            
        tup = (tup[1], tup[0])
        new_tuples_list.append(tup)

    return new_tuples_list
