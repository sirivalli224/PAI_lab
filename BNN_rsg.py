# General Bayesian Network Solver for Rain-Sprinkler-GrassWet

from itertools import product

# ----------- INPUT SECTION -----------

P_Rain = float(input("Enter P(Rain=True): "))

print("\nEnter P(Sprinkler=True | Rain):")
P_S_given_R = float(input("P(S=True | R=True): "))
P_S_given_notR = float(input("P(S=True | R=False): "))

print("\nEnter P(GrassWet=True | Rain, Sprinkler):")
P_G_given_RS = float(input("P(G=True | R=True, S=True): "))
P_G_given_R_notS = float(input("P(G=True | R=True, S=False): "))
P_G_given_notR_S = float(input("P(G=True | R=False, S=True): "))
P_G_given_notR_notS = float(input("P(G=True | R=False, S=False): "))

# ----------- PROBABILITY TABLES -----------

def P_R(r):
    return P_Rain if r else (1 - P_Rain)

def P_S(s, r):
    if r:
        return P_S_given_R if s else (1 - P_S_given_R)
    else:
        return P_S_given_notR if s else (1 - P_S_given_notR)

def P_G(g, r, s):
    table = {
        (True, True): P_G_given_RS,
        (True, False): P_G_given_R_notS,
        (False, True): P_G_given_notR_S,
        (False, False): P_G_given_notR_notS
    }
    return table[(r, s)] if g else (1 - table[(r, s)])

# ----------- JOINT PROBABILITY -----------

def joint_prob(r, s, g):
    return P_R(r) * P_S(s, r) * P_G(g, r, s)

# ----------- INFERENCE ENGINE -----------

def query_probability(query_var, query_val, evidence):
    total_query = 0
    total_evidence = 0

    for r, s, g in product([True, False], repeat=3):
        assignment = {'R': r, 'S': s, 'G': g}

        prob = joint_prob(r, s, g)

        # Check evidence match
        if all(assignment[var] == val for var, val in evidence.items()):
            total_evidence += prob

            if assignment[query_var] == query_val:
                total_query += prob

    if total_evidence == 0:
        return 0
    return total_query / total_evidence

# ----------- USER QUERY -----------

print("\nVariables: R = Rain, S = Sprinkler, G = GrassWet")

query_var = input("Enter query variable (R/S/G): ").upper()
query_val = input("Enter query value (True/False): ") == "True"

n = int(input("Enter number of evidence variables: "))
evidence = {}

for _ in range(n):
    var = input("Evidence variable (R/S/G): ").upper()
    val = input("Value (True/False): ") == "True"
    evidence[var] = val

# ----------- RESULT -----------

result = query_probability(query_var, query_val, evidence)

print("\nResult:")
print(f"P({query_var}={query_val} | evidence) =", result)
