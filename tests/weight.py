from random import choices

bo = ["a", "b", "c"]
choice = "c"


WEIGH_A = 0.3
WEIGH_B = 0.3
WEIGH_C = 0.3

match choice:
    case "a":
        WEIGH_A -= 0.05
        WEIGH_B += 0.05
        WEIGH_C += 0.1
    case "b":
        WEIGH_A += 0.05
        WEIGH_B -= 0.05
        WEIGH_C += 0.1
    case "c":
        WEIGH_A += 0.05
        WEIGH_B += 0.05
        WEIGH_C -= 0.1

RESPONSE = (choices(bo, weights=[WEIGH_A, WEIGH_B, WEIGH_C], k=100000))
print("A = " + str(RESPONSE.count("a")))
print("B = " + str(RESPONSE.count("b")))
print("C = " + str(RESPONSE.count("c")))
