class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        dist=[100000000]*V
        dist[src]=0
        for i in range(V):
            for edge in edges:
                u, v, wt=edge
                #relaxation of the nodes cases
                if dist[u]!=100000000 and dist[u]+wt<dist[v]:
                    # if the node is not reachable
                    if i==V-1:
                        return[-1]
                        # update the nodes weight
                    dist[v]=dist[u]+wt
        return dist