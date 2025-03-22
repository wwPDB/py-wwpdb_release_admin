# Queries a graphlql server
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport


class Query:
    def __init__(self):
        self.__transport = None

    def setup(self, urlreq, authtoken=None, getschema=False):
        headers = {
            "Content-type": "application/json",
        }
        if authtoken is not None:
            headers["Authorization"] = authtoken

        self.__transport = RequestsHTTPTransport(
            url=urlreq,
            use_json=True,
            headers=headers,
            # verify=False,
            retries=3,
        )
        self.__client = Client(transport=self.__transport, fetch_schema_from_transport=getschema)

    def query(self, query, variables=None):
        if variables is None:
            variables = {}
        return self.__client.execute(query, variable_values=variables)

    def makequery(self, query):
        return gql(query)
