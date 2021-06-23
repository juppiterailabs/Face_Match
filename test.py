from facematch.face import match

f = open('Path to your first image', 'rb')
data1 = f.read()
f.close()

f = open('path to your id image', 'rb')
data2 = f.read()
f.close()

result, distance, data = match(data1, data2)

f = open('out.png', 'wb')
f.write(data)
f.close()

print(distance)
print(result)
