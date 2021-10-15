# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(snail_map):
    result=[]
    if snail_map==[[]]:
        return []
    while len(snail_map)>=1:
        for x in range(len(snail_map)):
            result.append(snail_map[0][x])
        snail_map.pop(0)
        for y in range(len(snail_map)):
            result.append(snail_map[y][-1])
        for y in range(len(snail_map)):
            snail_map[y].pop()
        for x in range(1,len(snail_map)+1):
            result.append(snail_map[y][-x])
        try:
            snail_map.pop()
        except:
            return result
        for y in range(1,len(snail_map)+1):
            result.append(snail_map[-y][0])
        for y in range(len(snail_map)):
            snail_map[y].pop(0)
    return result
