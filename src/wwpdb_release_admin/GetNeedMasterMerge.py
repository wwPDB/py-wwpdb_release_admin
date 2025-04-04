from wwpdb_release_admin.wwpdbgit.Authorization import Authorization
from wwpdb_release_admin.wwpdbgit.Query import Query
from wwpdb_release_admin.wwpdbgit.QueryRequests import QueryRequests


def main():
    auth = Authorization()
    auth.readFile(".auth")

    q = Query()
    q.setup("https://api.github.com/graphql", auth.getBearer())
    qr = QueryRequests(q)
    master = qr.getReposBranchCommit("wwPDB", "master")
    develop = qr.getReposBranchCommit("wwPDB", "develop")
    maincom = qr.getReposBranchCommit("wwPDB", "main")

    # Iterate through the repos that have a develop branch
    print("The following repositories need to have master updated")
    for r in develop["repos"]:
        doid = develop[r]["oid"]
        # ddate = develop[r]["committedDate"]
        if r in master:
            moid = master[r]["oid"]
            # mdate = master[r]["committedDate"]
        else:
            moid = maincom[r]["oid"]
            # mdate = maincom[r]["committedDate"]
        if doid != moid:
            print(r, develop[r])


if __name__ == "__main__":
    main()
