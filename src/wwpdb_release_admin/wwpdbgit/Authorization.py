# Retrieves authorization for a query


class Authorization:
    def __init__(self):
        self.__auth = None

    def readFile(self, fpath):
        with open(fpath) as fin:
            self.__auth = fin.readline().strip()

    def getBearer(self):
        ret = "Bearer " + self.__auth
        return ret


if __name__ == "__main__":
    a = Authorization()
    a.readFile(".auth")
