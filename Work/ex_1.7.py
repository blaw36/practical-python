# Ex 1.7

# Try-except
with open("C:\\Users\\brend\\Documents\\python\\practical-python\\Work\\Data\\portfolio.csv", 'rt') as f:
    all_shares = []
    for line in f:
        fields = line.split(",")
        try:
            shares = int(fields[1])
            all_shares.append(shares)
        except ValueError:
            print("Couldn't parse", line)

print(all_shares)
# raise RuntimeError("What a kerfuffle")
print(f"When you raise a runtime error, that's a thing with type: {type(RuntimeError('What a kerfuffle'))}")

def greeting(name):
    'Issues a greeting'
    print('Hello', name)
greeting('Guido')
greeting('Paula')