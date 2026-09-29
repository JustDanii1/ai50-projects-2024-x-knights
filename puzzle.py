from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

def structure(*pairs):
    """pairs — список кортежей (XKnight, XKnave) для всех персонажей задачи."""
    clauses = []
    for knight, knave in pairs:
        clauses.append(Or(knight, knave))
        clauses.append(Not(And(knight, knave)))
    return And(*clauses)


knowledge0 = And(
    structure((AKnight, AKnave)),
    Biconditional(AKnight, And(AKnight, AKnave))
)

knowledge1 = And(
    structure((AKnight, AKnave), (BKnight, BKnave)),
    Biconditional(AKnight, And(AKnave, BKnave))
)

knowledge2 = And(
    structure((AKnight, AKnave), (BKnight, BKnave)),
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight)))
)

knowledge3 = And(
    structure((AKnight, AKnave), (BKnight, BKnave), (CKnight, CKnave)),
    Or(
        Biconditional(AKnight, AKnight),
        Biconditional(AKnight, AKnave)
    ),
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    Biconditional(BKnight, CKnave),
    Biconditional(CKnight, AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
