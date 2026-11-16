from itertools import product
# Step 1: Define implication
def implies(a, b):
    return (not a) or b
# Step 2: Define Knowledge Base
def knowledge_base(P, Q, R):
    s1 = implies(Q, P)
    s2 = implies(P, not Q)
    s3 = Q or R
    return s1, s2, s3


# Step 3: Check propositional entailment
def entails(query):
    symbols = ['P', 'Q', 'R']

    for values in product([True, False], repeat=3):
        model = dict(zip(symbols, values))

        P = model['P']
        Q = model['Q']
        R = model['R']

        s1, s2, s3 = knowledge_base(P, Q, R)
        kb = s1 and s2 and s3

        if kb and not query(P, Q, R):
            return False

    return True


# Step 4: Generate truth table
print("P Q R | Q->P | P->~Q | QvR | KB")
print("--------------------------------------")

valid_models = []

for values in product([True, False], repeat=3):
    P, Q, R = values

    s1, s2, s3 = knowledge_base(P, Q, R)
    kb = s1 and s2 and s3

    print(
        P, Q, R, "|",
        s1, "|", s2, "|", s3, "|", kb
    )

    if kb:
        valid_models.append((P, Q, R))


# Step 5: Display valid models
print("\nModels where KB is True:")
for model in valid_models:
    print(model)


# Step 6: Test all given queries
print("\nEntailment Results:")

print("KB entails R:",
      entails(lambda P, Q, R: R))

print("KB entails R -> P:",
      entails(lambda P, Q, R: implies(R, P)))

print("KB entails Q -> R:",
      entails(lambda P, Q, R: implies(Q, R)))

