from typing import List


class Status:

    def __init__(self, name) -> None:
        self.name = name
        self.status = []
        self.create_status(self.name)
        # print(self.name, self.status)

    def create_status(self, name) -> None:
        """dataファイルからステータス情報を生成する

        Parameters
        ----------
        name: ポケモンの英語名
        dataディレクトリにあるポケモン名ファイルを読み込む

        """
        path = f"./data/status/{name}"
        try:

            with open(path) as f:
                lines = f.readlines()
                lines.pop(0)
                for line in lines:
                    data = [float(x.strip()) for x in line.split("\t")]
                    data[0] = int(data[0])
                    self.status.append({
                        "level": data[0],
                        "hp": data[1],
                        "atk": data[2],
                        "def": data[3],
                        "spa": data[4],
                        "spd": data[5],
                        "crit_rate": data[6],
                        "cdr": data[7],
                        "life_steal": data[8],
                        "atk_spd": data[9] + 100
                    })
        except Exception as e:
            print(e)


    def get_as(self) -> List:
        """レベルごとの攻撃速度リストを返す

        """
        as_list = [item["atk_spd"] for item in self.status]
        return as_list

if __name__ == "__main__":
    
    data = Status("eldegoss")





