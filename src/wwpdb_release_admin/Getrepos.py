from wwpdbgit.Authorization import Authorization
from wwpdbgit.Query import Query
from wwpdbgit.QueryRequests import QueryRequests


def main():
    auth = Authorization()
    auth.readFile(".auth")

    q = Query()
    q.setup("https://api.github.com/graphql", auth.getBearer())
    qr = QueryRequests(q)
    repos = qr.getRepos("wwPDB")

    print("The following repositories exist in wwPDB orgination")
    for r in repos["repos"]:
        print(r)


if __name__ == "__main__":
    main()
