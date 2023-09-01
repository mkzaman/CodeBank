
def get_required_transposition(source : [], target : []) -> []:
    if(len(source) != len(target)):
        return
    result = []
    target_lenght = len(target)
    for i in range(0, target_lenght - 1):
        if(target[i] == source[i]):
            print(target)
            print(source)
            continue
        try:
            source_index =  source.index(target[i])
            result.append((i, source_index))
            source[i], source[source_index] = source[source_index], source[i]
        except ValueError:
            return
        
    return result
        
print(get_required_transposition([3, 4, 0, 2, 1], [0, 1, 3, 4, 2]))