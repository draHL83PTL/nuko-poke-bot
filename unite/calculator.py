from decimal import Clamped
from typing import List
import copy
from unite.status import Status


class Calculator:
    def __init__(self, name) -> None:
        self.status = Status(name)

    def get_actual_as(self, as_list, rate):
        res = copy.copy(as_list)
        cur = 1
        for i in range(len(res)):
            while(rate[cur] < res[i]):
                cur += 1
            res[i] = round(rate[cur - 1])
        return res

    def red_medal(self):
        as_list = self.status.get_as()
        rate = read_as_rate()
        patterns = read_as_pattern()
        if len(as_list) < 1:
            return "データが見つかりません"
        content = ""
        for pattern in patterns:
            actual_as_list = self.get_actual_as([i + pattern["as_diff"] for i in as_list], rate)
            content += "---" + pattern["name"] + "---\n"
            content += str(actual_as_list) + "\n"
        return content

def read_as_rate() -> List[int]:
    path = "./data/conf/as_rate"
    res = []
    with open(path) as f:
        for as_rate in [int(line.strip()) for line in f.readlines()]:
            res.append(as_rate)
    res.append(100000)
    return res
    
def read_as_pattern() -> List:
    path = "./data/conf/as_pattern"
    res = []
    with open(path, encoding="utf-8") as f:
        for as_pattern in [line.strip().split(" ") for line in f.readlines()]:
            item = {
                "name": as_pattern[0],
                "as_diff": float(as_pattern[1])
            }
            res.append(item)
    return res


if __name__ == "__main__":

    print(Calculator("eldegos").red_medal())

