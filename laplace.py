import  numpy as np

def emission_prob(tr_set,word,tag):
    total = tr_set[np.where(tr_set[:,1] == tag)]
    portion = total[np.where(total[:,0] == word)]
    unique_words = np.unique(total[:, 0])
    return (len(portion) + 1 /(len(total) + len(unique_words)))
