import math
import re
import collections

def cos_similarity(vec1, vec2):
    dot_product = sum(x*y for x, y in zip(vec1, vec2))
    norm_vec1 = math.sqrt(sum(x**2 for x in vec1))
    norm_vec2 = math.sqrt(sum(x**2 for x in vec2))

    return dot_product / (norm_vec1 * norm_vec2)
    

def main(file1, file2):
    file1 = re.sub(r"[^a-zA-Z\s]", "", file1)
    file2 = re.sub(r"[^a-zA-Z\s]", "", file2)

    file1_words = [x.lower() for x in file1.split()]
    file2_words = [x.lower() for x in file2.split()]

    all_words = set(file1_words + file2_words)

    file1_word_count = collections.Counter(file1_words)
    file2_word_count = collections.Counter(file2_words)

    file1_matrix = [file1_word_count[word] for word in all_words]
    file2_matrix = [file2_word_count[word] for word in all_words]

    score = cos_similarity(file1_matrix, file2_matrix)

    return score

    