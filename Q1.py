


t = int(input("enter th where"))


for i in range(t):
    n = int(input("input"))
    
    b = input().split()
    donor_count = {'A': 0, 'B': 0, 'AB': 0, 'O': 0}
    for blood_group in b:
        donor_count[blood_group] += 1
    
    
    chain_length = min(donor_count['A'], donor_count['AB'])
    chain_length += min(donor_count['B'], donor_count['AB'])
    chain_length += min(donor_count['O'], donor_count['A'], donor_count['B'], donor_count['AB'])
    
print(chain_length)





