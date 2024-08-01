a=["hello","word","enter"]
for word in a:
    vc=sum(1 for char in word if char.lower() in 'aeiou')
    print(f"word:{word},vc:{vc}")
