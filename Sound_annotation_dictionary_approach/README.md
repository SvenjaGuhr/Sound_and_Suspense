# Tidy_Sound_annotation_dictionary_approach
Read a csv file with the literary text prepared for annotation (tokenized + "O" column) (*_for_annotation.csv).
Define a list of sound words (lemma from manual annotations) and use a simple list comparison to annotate automatically the read csv-file by overwriting the  annotation column with the respective sound annotations according to the sound words in the list.

Evaluate the dictionary-based annotation with commun metrics like: precision, recall, f1-score, accuracy.
Bonus: Calculate the interannotator agreement (Cohen's kappa) of two manual annotations of the same text by two independant annotators.
