# 定义三条路线坐标

road = [[], [], []]

for i in range (25):

    road[0].append({1: (270, 560 - i * 20), 2: (290, 560 - i * 20), 3: (310, 560 - i * 20)})

    road[2].append({1: (370 + 20 * i, 620), 2: (370 + 20 * i, 640), 3: (370 + 20 * i, 660)})

for i in range (25, 50):

    road[0].append({1: (20 * i -170, 20), 2: (20 * i -170, 40), 3: (20 * i -170, 60)})

    road[2].append({1: (870, 1100 - 20 * i), 2: (890, 1100 - 20 * i), 3: (910, 1100 - 20 * i)})

for i in range (12):

    road[1].append({1: (330 + i * 20, 560 - i * 20), 2: (350 + i * 20, 580 - i * 20), 3: (370 + i * 20, 600 - i * 20)})

    road[1].append({1: (350 + i * 20, 560 - i * 20), 2: (370 + i * 20, 580 - i * 20), 3: (390 + i * 20, 600 - i * 20)})

road[1].append({1: (330 + 12 * 20, 560 - 12 * 20), 2: (350 + 12 * 20, 580 - 12 * 20), 3: (370 + 12 * 20, 600 - 12 * 20)})

for i in range (12):

    road[1].append({1: (570 + i * 20, 300 - i * 20), 2: (590 + i * 20, 320 - i * 20), 3: (610 + i * 20, 340 - i * 20)})
    
    road[1].append({1: (590 + i * 20, 300 - i * 20), 2: (610 + i * 20, 320 - i * 20), 3: (630 + i * 20, 340 - i * 20)})
    
