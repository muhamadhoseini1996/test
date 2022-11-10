def moving_average(price_list, step, size):
    avg_ = []
    for i in range(step):
        if i != 0:
            avg = round(sum(price_list[:i+1]) / len(price_list[:i+1]), 2)
        else:
            avg = (price_list[0])

        avg_.append(avg)
    vector = []
    for i in range(size):
        mean = round(sum(price_list[i - step:i]) / step, 2)
        if mean == 0:
            mean = avg_[i]

        vector.append(mean)

    return vector
