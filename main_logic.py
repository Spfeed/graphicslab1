R = 50  # Исходный радиус

#файл, содержащий логику, предназанченный для раннера

def increase_radius():
    global R
    R += 10
    return R

def decrease_radius():
    global R
    if R > 10:
        R -= 10
    return R
