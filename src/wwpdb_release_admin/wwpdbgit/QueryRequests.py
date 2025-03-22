# Manages query requests and responses

from wwpdb_release_admin.wwpdbgit.QueryBuilder import QueryBuilder


class QueryRequests:
    def __init__(self, queryh):
        """Given a Query prepare quests"""
        self.__queryh = queryh

    def getRepos(self, org):
        qb = QueryBuilder()
        reqstr = qb.getRepos()
        req = self.__queryh.makequery(reqstr)
        variables = {"org": org}

        return self._iterreq(req, variables, self.__accRepos)

    def __accRepos(self, ret, edges):
        """Accumulates data for getRepos"""
        if "repos" not in ret:
            ret["repos"] = []
        for edge in edges:
            ret["repos"].append(edge["node"]["name"])

    def _iterreq(self, req, variables, cb=None):
        """Iterates through request and pagination"""

        ret = {}
        done = False
        while not done:
            d = self.__queryh.query(req, variables)
            repod = d["organization"]["repositories"]
            if cb:
                cb(ret, repod["edges"])
            else:
                print(repod["edges"])

            pinfo = repod["pageInfo"]
            if pinfo["hasNextPage"] is True:
                variables["after"] = pinfo["endCursor"]
            else:
                done = True

        return ret

    def getReposBranchCommit(self, org, branch):
        """Get latest commit on a branch. If branch not present, return nothing"""
        qb = QueryBuilder()
        reqstr = qb.getBranchCommits()
        req = self.__queryh.makequery(reqstr)
        variables = {"org": org, "branch": branch}

        return self._iterreq(req, variables, self.__accBranchRepos)

    def __accBranchRepos(self, ret, edges):
        """Accumulates data for getRepos"""
        if "repos" not in ret:
            ret["repos"] = []
        for edge in edges:
            name = edge["node"]["name"]
            if edge["node"]["ref"]:
                ret["repos"].append(name)
                ret[name] = edge["node"]["ref"]["target"]
