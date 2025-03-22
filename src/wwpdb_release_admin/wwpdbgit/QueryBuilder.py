# Returns strings for GraphQL queries


class QueryBuilder:
    def getRepos(self):
        """Returns query for repositories. Must set org, optional after"""
        s = """query ($org: String! $after: String){
organization(login: $org)
  {
    repositories(first: 100, after: $after) {
      edges {
        node {
          name
        }
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}"""
        return s

    def getBranchCommits(self):
        """Query requires an org and branch to get data"""
        return """query something($org: String!, $branch: String!, $after: String) {
  organization(login: $org) {
    repositories(first: 100, after: $after) {
      totalCount
      edges {
        node {
          name
          ref(qualifiedName: $branch) {
            name
            target {
              ... on Commit {
                oid
                committedDate
              }
            }
          }
        }
      }
      pageInfo {
        endCursor
        hasNextPage
      }
    }
  }
}"""
