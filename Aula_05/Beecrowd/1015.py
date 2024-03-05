p1 = input().split()
p2 = input().split()
p1[0] = float(p1[0])
p2[0] = float(p2[0])
p1[1] = float(p1[1])
p2[1] = float(p2[1])

x1 = p1[0]
x2 = p2[0]
y1 = p1[1]
y2 = p2[1]

r = (((x2-x1)**2)+((y2-y1)**2))**(1/2)

print(f"{r:.4f}")