import random

file =  open("dataset.txt", 'r', encoding="utf8")

count = 0

sentences = []
sentence = []

num_clusters = []
temp_clusters = 0

word_count = 0

for line in file:
    if line in ['\n', '\r\n']:
        sentences.append(sentence)
        num_clusters.append(temp_clusters)
        sentence = []
        temp_clusters = 0
        word_count = 0
        continue
    count+=1
    word, pos = line.split()
    sentence.append((word, pos, word_count))
    word_count += 1
    if pos in ["N_NN", "N_NNP", "V_VM", "PR_PRP"]:
        temp_clusters += 1
#     if count > 60:
#         break
#
# with open("logs.txt", "a", encoding="utf8") as text_file:
#     print(sentences[0], file=text_file)

# with open("logs.txt", "a", encoding="utf8") as text_file:
#     print(file=text_file)

for i in range(0, len(sentences)):

    clusters = []
    centroid_indices = []

    for centroid_index in random.sample(range(0, len(sentences[i])), num_clusters[i]):
        temp_cluster = []
        temp_cluster_word, temp_cluster_pos, temp_cluster_count = sentences[i][centroid_index]
        temp_cluster.append({(temp_cluster_word, temp_cluster_count): temp_cluster_pos})
        clusters.append(temp_cluster)
        centroid_indices.append(centroid_index)

    # with open("logs.txt", "a", encoding="utf8") as text_file:
    #     print(clusters, file=text_file)

    long = True

    if len(clusters) == 0:
        long = False
        final_clusters = sentences[i]

    epochs = 5

    while epochs != 0 and long:
        # print(epochs)
        for word in sentences[i]:
            word_index = word[2]
            distances = {}
            centroid_count = 0
            for centroid in centroid_indices:
                distance = abs(centroid-word_index)
                distances[centroid_count] = distance
                centroid_count += 1

            sorted_distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}

            sorted_distances_list = list(sorted_distances.values())
            sorted_distances_key_list = list(sorted_distances.keys())

            # if(len(sorted_distances_list) == 0):
            #     print(clusters)

            if sorted_distances_list[0] != 0:
                if len(sorted_distances_list) > 1:
                    if sorted_distances_list[0] == sorted_distances_list[1]:
                        if word[1] == "PSP":
                            clusters[sorted_distances_key_list[0]].append({(word[0], word[2]): word[1]})
                        else:
                            clusters[sorted_distances_key_list[1]].append({(word[0], word[2]): word[1]})
                    else:
                        clusters[sorted_distances_key_list[0]].append({(word[0], word[2]): word[1]})
                else:
                    clusters[sorted_distances_key_list[0]].append({(word[0], word[2]): word[1]})

        # with open("logs.txt", "a", encoding="utf8") as text_file:
        #     print(clusters, file=text_file)

        new_clusters = []
        centroid_indices = []

        for cluster in clusters:
            noun_found = False
            for token in cluster:
                if noun_found:
                    break
                if list(token.values())[0] in  ["N_NN", "N_NNP", "V_VM", "PR_PRP"]:
                    noun_found = True
                    temp_cluster = []
                    centroid_index = sentences[i].index((list(token.keys())[0][0], list(token.values())[0], list(token.keys())[0][1]))
                    temp_cluster_word, temp_cluster_pos, temp_cluster_count  = sentences[i][centroid_index]
                    temp_cluster.append({(temp_cluster_word, temp_cluster_count): temp_cluster_pos})
                    new_clusters.append(temp_cluster)
                    centroid_indices.append(centroid_index)
            if noun_found == False:
                for token in cluster:
                    noun_found = True
                    temp_cluster = []
                    centroid_index = sentences[i].index((list(token.keys())[0][0], list(token.values())[0], list(token.keys())[0][1]))
                    temp_cluster_word, temp_cluster_pos, temp_cluster_count  = sentences[i][centroid_index]
                    temp_cluster.append({(temp_cluster_word, temp_cluster_count): temp_cluster_pos})
                    new_clusters.append(temp_cluster)
                    centroid_indices.append(centroid_index)
                    break

        final_clusters = clusters.copy()
        clusters = new_clusters.copy()

        epochs -= 1

    chunks = {}

    for z in range(0, num_clusters[i]):
        phrase_type = "OTHER"
        for clusters in final_clusters[z]:
            for cluster in clusters.values():
                if cluster in  ["N_NN", "N_NNP", "PR_PRP"]:
                    phrase_type = "NP"
                    break
                elif cluster in ["V_VM"]:
                    phrase_type = "VP"
                    break
        for clusters in final_clusters[z]:
            for cluster in clusters.keys():
                chunks[cluster[1]] = phrase_type

    for word in sentences[i]:
        # print(word)
        phrase = "OTHER"
        if word[2] in chunks:
            phrase = chunks[word[2]]
        if word[1] == "RD_PUNC":
            phrase = "BLK"
        with open("output.txt", "a", encoding="utf8") as text_file:
            print(word[0], phrase, file=text_file)

    # UNCOMMENT TO SEE CLUSTERS
    # with open("clusters.txt", "a", encoding="utf8") as text_file:
    #     print(final_clusters, file=text_file)
