class Node: 
    def __init__(self, neighbors=[], name='unnamed'):
        self.name = name #is there a better way to do types? this feels awkward...
        self.neighbors = list(neighbors)
    def addneighbor(self, candidate):
        self.neighbors.append(candidate)
    def setname(self, string):
        self.name = str(string)
    
    def connectivity(self):
        return len(self.neighbors)

class Graph:
    def __init__(self, nodes = [], dictionary = {} ):
        #self.nodes = list(nodes)
        if len(dictionary) != 0:
            nodelist = []
            for i in range(len(dictionary.keys())):
                nodelist.append(Node(neighbors = dictionary.values()[i]))
                nodelist[i].setname(dictionary.keys()[i])
            self.nodes = nodelist
        else:
            self.nodes = list(nodes)
    def addnode(self, candidate):
        self.nodes.append(candidate)
    def size(self):
        return len(self.nodes)
    def maxcon(self):
        eset = set()
        for i in range(self.size()):
            eset.add(self.nodes[i].connectivity())
        tmax = max(eset)
        elist = []
        for i in range(self.size()):
            if self.nodes[i].connectivity() == tmax:
                elist.append(self.nodes[i].name)
        return (elist, tmax)
    def mincon(self):
        eset = set()
        for i in range(self.size()):
            eset.add(self.nodes[i].connectivity())
        eset.discard(0)
        tmin = min(eset)
        elist = []
        for i in range(self.size()):
            if self.nodes[i].connectivity() == tmin:
                elist.append(self.nodes[i].name)
        return (elist, tmin)
    def avcon(self):
        elist = []
        for i in range(self.size()):
            elist.append(self.nodes[i].connectivity())
        return (float(sum(elist))/len(elist))
    def island(self):
        elist = []
        for i in range(self.size()):
            if self.nodes[i].neighbors == []:
                elist.append(self.nodes[i])
        if elist == []:
            return 'no isolated nodes'
        else:
    	    for i in range(len(elist)):
                return elist[i].name

def makeGraph(filename = 'e06.gal'):
    import galtools as gt
    f = str(filename)
    galDict = gt.opengal(filename = f)
    nodelist = []
    for i in range(len(galDict.keys())):
        nodelist.append(Node(neighbors=galDict.values()[i]))
        nodelist[i].setname(galDict.keys()[i])
    return Graph(nodes=nodelist)

if __name__ == '__main__':
    galGraph = makeGraph() 
    print 'the average connectivity of nodes in the graph is', galGraph.avcon()
    if len(galGraph.maxcon()[0]) > 1:
        print 'the nodes {} have a maximum connectivity of {}'.format(galGraph.maxcon()[0], galGraph.maxcon()[1])
    else:
        print 'the node {} has a maximum connectivity of {}'.format(galGraph.maxcon()[0], galGraph.maxcon()[1])
    if len(galGraph.mincon()[0]) > 1:
       print 'the nodes {} have a minimum connectivity of {}'.format(galGraph.mincon()[0], galGraph.mincon()[1])
    else:
        print 'the node {} has a minimum connectivity of {}'.format(galGraph.mincon()[0], galGraph.mincon()[1])
    if galGraph.island() == 'no isolated nodes':
        print 'the graph has no nodes with no neighbors.'
    else:
        if len(galGraph.island()) > 1:
            print 'the graph has {} nodes with no neighbors: {}'.format(len(galGraph.island()), galGraph.island()[0])
        else:
            print 'the graph has one node with no neighbors: ', galGraph.island()[0]    
