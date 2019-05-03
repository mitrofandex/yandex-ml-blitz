data = []
y_sum = 0
y2_sum = 0
with open('stump.in') as file:
    n = int(file.readline())
    for line in file:
        x, y = map(float, line.split())

        y_sum += y
        y2_sum += y**2

        data.append([x, y])

data.sort()

loss_min = y2_sum - y_sum**2 / n
opt_abc = (y_sum / n, 0, data[-1][0] + 1)

y_lsum = 0
y2_lsum = 0
for i in range(n - 1):

    y_lsum += data[i][1]
    y_rsum = y_sum - y_lsum

    if data[i][0] != data[i + 1][0]:
        c = (data[i][0] + data[i + 1][0]) / 2
        a = y_lsum / (i + 1)
        b = y_rsum / (n - i - 1)

        loss = y2_sum - a * y_lsum - b * y_rsum

        if loss < loss_min:
            loss_min = loss
            opt_abc = (a, b, c)


with open('stump.out', 'w') as f_out:
    a, b, c = opt_abc
    f_out.write('{:.6f} {:.6f} {:.6f}'.format(a, b, c))
