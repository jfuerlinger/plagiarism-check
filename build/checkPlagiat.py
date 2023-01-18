import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from fnmatch import fnmatch
from xml.sax.saxutils import escape

mypath = "submissions" #input("Ordner: ")
ending = "cs" #input("Filetyp: ")

student_files = []

for path, subdirs, files in os.walk(mypath):
    for name in files:
        if fnmatch(name, "*." + ending):
            fname = escape(os.path.join(path, name).replace(mypath,""))
            print (fname)
            student_files.append(fname)

print("Collect File done")
print(files)
            
student_notes = []

for _file in student_files:
    try:
        f = open(mypath + _file, "r", encoding='utf-8')
        student_notes.append(f.read())
        f.close()
    except:
        print("Nicht möglich bei " + str(_file))

def vectorize(Text): return TfidfVectorizer().fit_transform(Text).toarray()

def similarity(doc1, doc2): return cosine_similarity([doc1, doc2])

vectors = vectorize(student_notes)
s_vectors = list(zip(student_files, vectors))
plagiarism_results = set()


def check_plagiarism():
    global s_vectors
    for student_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((student_a, text_vector_a))
        del new_vectors[current_index]
        for student_b, text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((student_a, student_b))
            score = (student_pair[0], student_pair[1], sim_score, "\"C:\Program Files\WinMerge\WinMergeU.exe\" \"" + mypath + student_pair[0] + "\" \"" + mypath + student_pair[1] + "\"")
            plagiarism_results.add(score)
    return plagiarism_results


# for data in check_plagiarism():
#    print(data)

pd.DataFrame(check_plagiarism()) \
    .sort_values(2, ascending=False) \
    .replace('&amp;','&', regex=True) \
    .to_excel("Vergleich_"+mypath+".xlsx", index=False)
