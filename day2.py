from itertools import pairwise

with open("input/2.txt") as inpt:
    reports = [list(map(int, ln.split())) for ln in inpt.readlines()]


def is_valid_report(report):
    diff = [a - b for a, b in pairwise(report)]
    return (all(x > 0 for x in diff) or all(x < 0 for x in diff)) and all(
        1 <= abs(x) <= 3 for x in diff
    )


print(sum(map(is_valid_report, reports)))


def is_any_valid(report):
    return any(
        is_valid_report(report[:i] + report[i + 1 :]) for i in range(len(report))
    )


print(sum(map(is_any_valid, reports)))
