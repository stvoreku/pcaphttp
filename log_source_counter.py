file = "access.log"
file = 'access_new.log'
lines = None
sources = {}
with open(file, 'r') as f:
    lines = f.readlines()


for l in lines:
    s = l.split()[0]
    if s not in sources.keys():
        sources[s] = 1
    else:
        sources[s] += 1

connections_temp = sorted(sources.items(), key=lambda x:x[1], reverse=True)
connections_sorted = dict(connections_temp)


print(connections_sorted)
