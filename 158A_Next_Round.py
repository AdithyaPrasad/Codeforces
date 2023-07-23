n_and_k = input().split()
n = int(n_and_k[0])
k = int(n_and_k[-1])
scores = input().split()
scores= [int(i) for i in scores]
the_score = scores[k-1]
count = 0
for j in scores:
    if j >= the_score and j > 0:
        count += 1
print(count)