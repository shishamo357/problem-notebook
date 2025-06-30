from collections import defaultdict

N = int(input())
user_books = defaultdict(set)

for _ in range(N):
    op, uid, bid = input().split()
    uid, bid = int(uid), int(bid)
    
    if op == "buy":
        user_books[uid].add(bid)

for uid in sorted(user_books):
    if user_books[uid]:
        print(uid, *sorted(user_books[uid]))
