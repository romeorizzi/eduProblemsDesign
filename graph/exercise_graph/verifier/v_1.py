#!/usr/bin/python

import networkx as nx
from networkx.algorithms import clique, bipartite

#n_i tupla di coordinate
def angle_left(n0,n1,n2):
    return (n1[0]-n0[0])*(n2[1]-n0[1])-(n2[0]-n0[0])*(n1[1]-n0[1])

def intersection(n1,n2,n3,n4):
    d1=angle_left(n3,n4,n1)
    d2=angle_left(n3,n4,n2)
    d3=angle_left(n1,n2,n3)
    d4=angle_left(n1,n2,n4)
    if d1==0 and d2==0 and d3==0 and d4==0:
        return(((n2[0]-n3[0])*(n1[0]-n3[0])<=0 and (n2[1]-n3[1])*(n1[1]-n3[1])<=0) or ((n2[0]-n4[0])*(n1[0]-n4[0])<=0 and (n2[1]-n4[1])*(n1[1]-n4[1])<=0) or ((n4[0]-n1[0])*(n3[0]-n1[0])<=0 and (n4[1]-n1[1])*(n3[1]-n1[1])<=0))
    else:
        return(((d1<=0 and d2>=0) or (d1>=0 and d2<=0)) and ((d3<=0 and d4>=0) or (d3>=0 and d4<=0)))

def checkedges_print(coordinates):
    k=0
    c=[]
    for i in range(len(coordinates)):
        edg=coordinates[i]
        if len(edg)==3:
            c.append([edg[0],edg[1],edg[2]])
        if len(edg)>4:
            c.append([edg[0],edg[1],edg[2]])
            for j in range(2,len(edg)-2):
                c.append([edg[0],edg[j],edg[j+1],"intermedio"])
            c.append([edg[0],edg[-2],edg[-1]])
        if len(edg)==4:
            c.append([edg[0],edg[1],edg[2]])
            c.append([edg[0],edg[2],edg[2],"intermedio"])
            c.append([edg[0],edg[-2],edg[-1]])

    for i in range(len(c)):
        for j in range(i+1,len(c)):
            edg1=c[i]
            edg2=c[j]
            if len(edg1)==3 and len(edg2)==3:
                if edg1[1]!=edg2[1] and edg1[1]!=edg2[-1] and edg1[-1]!=edg2[1] and edg1[-1]!=edg2[-1]:
                    r=intersection(edg1[1],edg1[2],edg2[1],edg2[2])
                    if r==True :
                        k+=1
                        display(Markdown("Attenzione gli archi "+ edg1[0][0]+edg1[0][1]+" e "+edg2[0][0]+edg2[0][1]+ " si incrociano"))
            else:
                if edg1[0]!=edg2[0]:
                    r=intersection(edg1[1],edg1[2],edg2[1],edg2[2])
                    if r==True :
                        k+=1
                        display(Markdown("Attenzione gli archi "+ edg1[0][0]+edg1[0][1]+" e "+edg2[0][0]+edg2[0][1]+ " si incrociano"))
        
    if k==0 :
        display(Markdown("Corretto"))




def planar(input_struct):

    G = nx.Graph()
    G.add_nodes_from(input_struct.get("nodes"))
    G.add_weighted_edges_from(input_struct.get("edges"))

    G_first_set = nx.Graph()
    G.add_nodes_from(input_struct.get("first_set_nodes"))
    G.add_weighted_edges_from(input_struct.get("first_set_edges"))
    choice = input_struct.get("choice")

    coordinates=input_struct.get("list_e_coordinates")

    # check if graph is planar
    is_planar, _ = nx.check_planarity(G)

    # user choice
    if choice:
        if is_planar == True:
            checkedges_print(coordinates)
    else:
        if is_planar == False:
        # if choice is flase and graph was not planar

            if G_first_set.number_of_nodes() == 6:

                # check k_33 graph with bipartition 
                bip_first_set = bipartite.is_bipartite(G_first_set)
                if bip_first_set:
                    display(Markdown("Controesempio corretto"))
                    #print("Controesempio corretto")
                else:
                    display(Markdown("Non è un K 3 3"))
                    #print("Non è un K 3 3")

            elif G_first_set.number_of_nodes() == 5:
                # check k 5 with clique

                clique = nx.find_cliques(G_first_set)
                sorted_list = sorted(clique, key=len) 

                if len(sorted_list[len(sorted_list)-1]) == 5:
                    display(Markdown("Controesempio corretto"))
                    #print("Controesempio corretto")
                else:
                    display(Markdown("Non è un K 5"))
                    #print("Non è un K 5")
            else:
                # wrong counterexample
                display(Markdown("Controesempio non valido"))
                #print("Controesempio non valido")
        else:
            # if choice is flase and graph was planar
            display(Markdown("Soluzione errata"))
            #print("Soluzione errata")
