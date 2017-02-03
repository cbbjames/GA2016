from sys import argv
from numpy import *
from itertools import combinations, product
from math import log
import pdb
#BB=[] #[[0,3], [1], [2]]
#x={} #{BB1:{00:1/4, 01:2/3,,},,,}
#best_BB=[]


def D_model(n, BB):
    ans=0
    for bb in BB:
        ans+=(2**(len(bb))-1)#
        
    return ans*log(size,2)
    
def D_data(x, n):
    ans=0
    for bb in x.values():
        for v in bb.values():
            if v>0:
                ans+=v*log(v, 2)
            
    return -ans*size

def init_BB():
    BB=[[i] for i in range(n)]
    return BB 

def prob_of_population(population):
    lenth=len(population[0])
    p=[[0 for _ in range(lenth)],[0 for _ in range(lenth)]]
    
    for chrm in population:
        for i in range(lenth):
            assert chrm[i]<=1, chrm[i]
            p[chrm[i]][i]+=1
    
    p=[[i/size for i in p[0]],[i/size for i in p[1]]]
    return p

def making_x(BB):
    
    x = {}
    for bb in BB:
        bb.sort()
        bb=tuple(bb)
        x[bb]={}
        for seg in product(range(2), repeat=len(bb)):
            if len(bb)==1:
                x[bb][seg]=p[seg[0]][bb[0]]
            else:
                
                sets=[]
                for zero_or_one, idx in zip(seg, bb):
                    sets.append(which[idx][zero_or_one])
                    
                x[bb][seg]=x[bb].get(seg,0)+ (len(set.intersection(*sets))/size)
                    
                '''
                for chrm in population:
                    has=True
                    for zero_or_one, idx in zip(seg, bb):
                        if not chrm[idx]==zero_or_one: 
                            has = False
                            break
                
                    x[bb][seg]=x[bb].get(seg,0)+ (1/size if has else 0)
                '''
    return x

def build_mpm(BB):
    best_BB=BB[:]
    cost=D_model(n, best_BB)+D_data(making_x(best_BB), n)
    print("init BB: ", best_BB, D_model(n, best_BB), D_data(making_x(best_BB), n))
    #print(making_x(best_BB))
    for match in combinations(range(len(BB)),2):
        
        temp_BB=BB[:]
        new_bb = BB[match[0]]+BB[match[1]]
        pop1, pop2=temp_BB[match[0]], temp_BB[match[1]]
        temp_BB.remove(pop1)
        temp_BB.remove(pop2)
        temp_BB.append(new_bb)
        temp_cost = D_model(n, temp_BB)+D_data(making_x(temp_BB), n)
        #print(temp_BB, D_model(n, temp_BB), D_data(making_x(temp_BB), n))
        #print(making_x(temp_BB))
        #print(temp_BB, cost)
        if temp_cost<cost:
            best_BB=temp_BB[:]
            cost= temp_cost
            print("best_BB", best_BB, cost)
            
    return best_BB

    
def cnt_zero(population):

    which=[[set(),set()] for _ in range(len(population[0]))]
    
    for i, chrm in enumerate(population):
        for j, bit in enumerate(chrm):
            which[j][bit].add(i)
    return which
    
def print_BB(BB):
    print(BB)
    BB=sorted(BB,key=lambda x: x[0])
    print(BB)
    for bb in BB:
        print(len(bb), ' '.join([str(i) for i in bb]))
        
cntn = open(argv[1]).readlines()
population=[[int(i) for i in L.split()] for L in cntn]
n = len(population[0])
size=len(population)
p=prob_of_population(population)
BB=init_BB()

ans_BB=BB[:]

which=cnt_zero(population)



for i in range(30):
    old_BB=ans_BB[:]
    
    if i==0: ans_BB = build_mpm(BB)
    else: ans_BB = build_mpm(ans_BB)
        
    if old_BB==ans_BB: break
    
    print("best mpm: ",ans_BB)

print_BB(ans_BB)