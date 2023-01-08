import secrets

for i in range(1,10):
    et = ['I', 'He', 'She']
    v = ["like", "dont like", "hate", "love"]
    nn = ["study","working", "eating", "watching", "doing"]
    
    etgen = secrets.choice(et)
    vgen = secrets.choice(v)
    nngen = secrets.choice(nn)
    
    print(f"{etgen} {vgen} {nngen}")

