import galtools as gat
import numpy as np
import graphtools as grt
#import networkx as nx
import pysal as ps
import pprint as pp

def shimbelize(graph):
    if type(graph) == dict:
        print 'input is not of the graphtools type "Graph". Converting...'
        graph = grt.Graph(dictionary = graph)
    s = len(graph.nodes)
    tmat = np.matrix(np.zeros((s, s)))
    d0 = np.matrix(np.zeros((s, s)))
    for i in range(s):
        for j in range(len(graph.nodes[i].neighbors)):
            d0[i, graph.nodes[i].neighbors[j]-1] = 1
        tmat[i, i] = -1   
        if graph.nodes[i].neighbors == []:
            tmat[i] = tmat[i] - 1
            tmat[:, i] = tmat[:, i]-1
    shimbel = tmat + d0
    count = 1
    s = shimbel.shape
    dlist = []
    dlist.append(d0)
    dn = np.dot(d0, d0)
    dlist.append(dn)
    while 0 in shimbel:
        count = count + 1
        tfshimbel = shimbel == 0
        for i in range(s[0]):
            for j in range(s[1]):
                if tfshimbel[i, j]:
                    if dn[i,j] > 0:
                        shimbel[i, j] = count
        dn = np.dot(d0, dn)
        dlist.append(dn)
    shimbel = shimbel.clip(0)
    return shimbel, dlist

def diameter(shimbel, *wmatrix):
    dpathlist = []
    for i in range(shimbel.shape[0]):
        for j in range(shimbel.shape[1]):
            if shimbel[i, j] == shimbel.max():
                dpathlist.append((i, j))
    #started implementing a dijkstra for w-matrix. too much duplicated effort.
    #as per directions, assume all path lengths are 1
    return shimbel.max()


if __name__ == '__main__':
    columbus = grt.makeGraph(filename = 'gals/e08_columbus.gal')
    scol = shimbelize(columbus)
    print 'The Shimbel Matrix for the Columbus gal is:\n', scol[0]
    print '\n\nThe diameter of the Columbus gal is', diameter(scol[0])
    print '\n\nThe average shortest path length is', scol[0].mean()
    summarydict = {}
    olist = []
    for i in range(scol[0].shape[0]):
        shimind_i = scol[0][i].sum()
        order_i = scol[1][0][i].sum()
        tlist = []
        #order2_i = 0
        for j in range(scol[1][0].shape[1]):
            #decided to include order using ONLY shimbel
            #if scol[0][i,j] == 1:
            #    order2_i += 1
            #Now, if only I were clever enough to do ANN, too...
            if scol[1][0][i, j] == 1:
                tlist.append(scol[1][0][j].sum())
        anorder_i = sum(tlist)/len(tlist)
        summarydict.update({i+1:(shimind_i, order_i, anorder_i)})
    print '\n\nThe following dict is in the format:\npolygonID : (shimbel index, order, average neighbor order)\n\n'
    pp.pprint(summarydict)
