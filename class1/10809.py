S = input()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
answer = []
for i in alphabet:
    if i in S:
        answer.append(S.index(i))
    else:
        answer.append(-1)

print(" ".join(map(str, answer)))