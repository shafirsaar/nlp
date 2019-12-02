from nltk.corpus import brown
import numpy as np
import hmm_tagger
import csv

def splitter(str_arr):
    final = []
    for item in str_arr:
        final.append(item.split('-')[0].split('+')[0])
    return final

def total_error(tst_set,tr_set):
    good_tag = 0
    for word in tst_set:
        if tag_word(tr_set,word[0]) == word[1]:
            good_tag += 1
    return 1-(good_tag / tst_set.shape[0])

def tag_word(tr_set, word):
    """
    finds the tag that maximizes p(tag|word)
    when p(tag|word) = |word,tag|/|word|
    """
    tr_set = tr_set[np.where(tr_set[:,0] == word)]
    tags = tr_set[:,1]
    if len(tags) == 0:
        return 'NN'
    (values, counts) = np.unique(tags,return_counts=True)
    index = np.argmax(counts)
    return values[index]


if __name__ == "__main__":
    brown_tw = np.array(brown.tagged_words(categories='news'))
    brown_tw[:, 1] = splitter(brown_tw[:, 1])
    sep = int(0.9 * len(brown_tw))
    training_set = brown_tw[:sep]
    test_set = brown_tw[sep:]
    hmm = hmm_tagger.viterbi(training_set[0:100],test_set[0:100])

else:
    print("Executed when imported")
