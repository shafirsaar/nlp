import numpy as np

def emission_prob(tr_set,word,tag):
    total = tr_set[np.where(tr_set[:,1] == tag)]
    portion = total[np.where(total[:,0] == word)]
    return (len(portion)/len(total))

def trans_prob(tag,prev_tag,tr_set):
    total,portion = 0,0
    for i in range(1,len(tr_set)):
        if tr_set[i-1, 1] == prev_tag:
            total += 1
            if tr_set[i, 1] == tag:
                portion += 1
    if tr_set[-1, 1] == prev_tag:
        total += 1
    return portion/total

"""def viterbi(tr_set, tst_set):
    unique_tags = np.unique(tr_set[:,1])
    l = len(unique_tags)
    n = len(tst_set)
    mat = np.zeros((n+2,l))
    max = np.zeros(n)
    for j in range(n):
        em_prob = 0
        for i in range(l):
            temp = emission_prob(tr_set, tst_set[j,0], unique_tags[i])
            if temp > em_prob:
                em_prob = temp
        if em_prob == 0:
            tst_set[j, 1] = 'NN'

    for i in range(l):
        mat[i,0] = 1
    for j in range(1,n):
        for i in range(l):
            max = 0
            em_prob = emission_prob(tr_set, tst_set[j,0], unique_tags[i])
            for k in range(l):
                temp = mat[k,j-1]*trans_prob(unique_tags[i], unique_tags[k], tr_set)
                temp = temp * em_prob
                if temp > max:
                    max = temp
            mat[i,j] = max

    return mat
"""
def viterbi(tr_set, tst_set):
    n = len(tst_set)
    unique_tags = np.unique(tr_set[:,1])
    l = len(unique_tags)
    mat = np.zeros((n+1,l))
    print(mat)

'''

