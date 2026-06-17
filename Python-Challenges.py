"""
╔══════════════════════════════════════════════════════════════════════════╗
║  PYTHON CODING CHALLENGES  —  LEARNER SHEET                              ║
║  15 problems  ·  7 MEDIUM + 8 COMPLEX                                   ║
║                                                                          ║
║  ALLOWED CONCEPTS ONLY:                                                 ║
║    Python foundations · lists · dictionaries · tuples · sets ·          ║
║    deques · I/O operations · control flow · loops                       ║
║  (No external libraries. `from collections import deque` is allowed.)   ║
╚══════════════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────────┐
│  ⚠  HOW THIS IS GRADED — READ THIS FIRST                                 │
│                                                                          │
│  Every problem below is a DELIBERATE VARIATION of a famous, well-known   │
│  problem. The variation (the "twist") is written in plain English but    │
│  is EASY TO MISS if you skim. Read each problem slowly.                  │
│                                                                          │
│  Each problem is graded with TWO sets of hidden tests:                   │
│    1. VISIBLE tests  — the obvious cases (a few are shown to you below   │
│       so you can self-check).                                            │
│    2. TRAP tests     — these specifically exercise THE TWIST.            │
│                                                                          │
│  A solution copy-pasted from an AI usually solves the FAMILIAR version   │
│  of the problem. It will pass the visible tests and FAIL the traps.      │
│  Only a solution that actually implemented the twist passes everything.  │
│                                                                          │
│  PROOF OF UNDERSTANDING (required for each problem):                     │
│    • Add a comment   `# TWIST:`  — state the variation IN YOUR OWN WORDS.│
│    • Add a comment   `# TRACE:`  — hand-compute ONE intermediate value   │
│      for the given canary input and show your working (one line).        │
│  A pasted answer will not contain a correct, specific trace unless you   │
│  genuinely understood the problem.                                       │
│                                                                          │
│  Fill in each  solve_*  function, then run this file to self-check the   │
│  visible cases.                                                          │
└──────────────────────────────────────────────────────────────────────────┘
"""

from collections import deque


# ════════════════════════════════════════════════════════════════════════════
#  MEDIUM 1 — "Lucky FizzBuzz"
# ════════════════════════════════════════════════════════════════════════════
#  Return a list of strings for 1..n following these rules, checked TOP to
#  bottom (first match wins):
#    • If the number's digits contain a '7' anywhere  -> "Lucky"
#    • else if divisible by 15                        -> "BuzzFizz"
#    • else if divisible by 3                         -> "Fizz"
#    • else if divisible by 5                         -> "Buzz"
#    • else                                           -> the number as a string
#
#  Canary input: n = 70   (look closely at 7, 15, 17, 70)
#  Visible self-check below uses n = 5.
#
#  # TWIST: I check for the digit 7 first. If it is present, I add Lucky.
#  # TRACE: In n = 70, number 7 gives "Lucky" because 7 is present  the number.
def solve_m1(n):
    result = []
    for num in range(1, n + 1):
        if "7" in str(num):
            result.append("Lucky")
        elif num % 15 == 0:
            result.append("BuzzFizz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(num))
    return result
 
# ════════════════════════════════════════════════════════════════════════════
#  MEDIUM 2 — "Sometimes-Y Vowel Counter"
# ════════════════════════════════════════════════════════════════════════════
#  Count vowels in a sentence. Vowels are a, e, i, o, u (any case). ALSO count
#  the letter 'y' as a vowel — BUT ONLY when it is NOT the first letter of its
#  word. Return the total count (an int).
#
#  Canary input: "yummy yellow sky"
#
# # TWIST: Count 'y' as a vowel only when it is not the first letter of a word.
# # TRACE: in "sky", 'y' is counted because it is not the first letter.
def solve_m2(sentence):
    count = 0
    words = sentence.split()
    for word in words:
        for index in range(len(word)):
            ch = word[index].lower()
            if ch in "aeiou":
                count += 1
            elif ch == "y" and index != 0:
                count += 1
    return count

# ════════════════════════════════════════════════════════════════════════════
#  MEDIUM 3 — "Keep the LAST One"
# ════════════════════════════════════════════════════════════════════════════
#  Remove duplicate values from a list. Keep each value at the position of its
#  LAST occurrence (NOT its first). Return the de-duplicated list.
#
#  Canary input: [1, 2, 3, 2, 1, 4]
#
#  # TWIST: If a value is repeated, keep only its last occurrence.
#  # TRACE: In [1, 2, 3, 2, 1, 4], the last 1 comes after the last 2, so the result is [3, 2, 1, 4].
def solve_m3(items):
    last_index = {}
    for index in range(len(items)):
        last_index[items[index]] = index
    result = []
    for index in range(len(items)):
        value = items[index]
        if last_index[value] == index:
            result.append(value)
    return result



# ════════════════════════════════════════════════════════════════════════════
#  MEDIUM 4 — "Running Max with Reset"
# ════════════════════════════════════════════════════════════════════════════
#  Walk the list left to right, outputting the maximum seen so far at each
#  step. BUT every time you hit a 0, output 0 AND reset the running maximum
#  (start fresh from after the zero). Return the list of running values.
#
#  Canary input: [3, 1, 4, 0, 2, 5, 1]
#
#  # TWIST: When 0 appears, reset the running maximum and start again.
#  # TRACE: In [3, 1, 4, 0, 2, 5, 1], after 0 the maximum starts again from 2.
def solve_m4(nums):
    result = []
    running_max = None
    for num in nums:
        if num == 0:
            result.append(0)
            running_max = None
        else:
            if running_max is None or num > running_max:
                running_max = num
            result.append(running_max)

    return result


# ════════════════════════════════════════════════════════════════════════════
#  MEDIUM 5 — "Top Word, Original Casing"
# ════════════════════════════════════════════════════════════════════════════
#  Find the most frequent word in a sentence, counting case-INsensitively
#  ("Go" and "go" are the same word). RETURN the winner spelled in the casing
#  it was FIRST seen in. Tie-break rules, in order:
#    1. higher count wins
#    2. if counts tie, the SHORTER word wins
#    3. if still tied, the alphabetically-first (lowercased) word wins
#
#  Canary input: "Go go STOP Stop go Stop"
#
#  # TWIST: ____________________________________________________________
#  # TRACE: counts are go=__ , stop=__ ; winner chosen because ________
def solve_m5(sentence):
    # your code here
    pass


# ════════════════════════════════════════════════════════════════════════════
#  MEDIUM 6 — "Circle Count with Boundary Penalty"
# ════════════════════════════════════════════════════════════════════════════
#  Given a list of (x, y) integer points and a radius r (circle centred at the
#  origin), return a single integer score:
#    • +1 for each point STRICTLY inside the circle
#    • -1 for each point EXACTLY on the boundary
#    •  0 (ignore) for points outside
#  Use integer math: compare x*x + y*y against r*r (avoid floats).
#
#  Canary input: points=[(0,0),(3,0),(5,0),(0,5),(4,3)], r=5
#
#  # TWIST: A point inside the circle gives +1, but a point exactly on the boundary gives -1.
#  # TRACE: For point (5, 0) and radius 5, the point is on the boundary, so the score becomes -1.
def solve_m6(points, r):
    score = 0
    radius_squared = r * r
    for point in points:
        x = point[0]
        y = point[1]
        distance_squared = x * x + y * y
        if distance_squared < radius_squared:
            score += 1
        elif distance_squared == radius_squared:
            score -= 1

    return score


# ════════════════════════════════════════════════════════════════════════════
#  MEDIUM 7 — "Symmetric Difference, No Fives"
# ════════════════════════════════════════════════════════════════════════════
#  Given two lists, compute the values that appear in exactly one of them
#  (the symmetric difference). THEN drop any value that is a multiple of 5.
#  Return the survivors as a sorted (ascending) list.
#
#  Canary input: a=[1,2,3,4,5,10], b=[3,4,5,6,15]
#
#  # TWIST: Take values present in only one list and remove multiples of 5.
#  # TRACE: From [1, 2, 3, 10] and [3, 6, 15], the unique values are [1, 2, 6, 10, 15]; after removing multiples of 5, the result is [1, 2, 6].
def solve_m7(a, b):
    set_b = set(b)
    set_a = set(a)
    difference = (set_a - set_b) | (set_b - set_a)
    result = []

    for value in difference:
        if value % 5 != 0:
            result.append(value)

    result.sort()
    return result


# ════════════════════════════════════════════════════════════════════════════
#  COMPLEX 1 — "Brackets + Loose Angles"
# ════════════════════════════════════════════════════════════════════════════
#  Validate a string of brackets. The (), [], {} pairs must be properly
#  nested (use a stack). HOWEVER, the angle brackets < and > only need to be
#  balanced in TOTAL COUNT — their order and nesting do NOT matter, and they
#  do NOT interact with the other brackets' nesting at all. Return True/False.
#
#  Canary input: "(<)>"   (note the angle brackets straddle the parens)
#
#  # TWIST: ____________________________________________________________
#  # TRACE: for "(<)>", the parens are ____ ; '<' count=__ , '>' count=__
def solve_c1(s):
    # your code here
    pass


# ════════════════════════════════════════════════════════════════════════════
#  COMPLEX 2 — "FIFO Inventory with Oversell Flag"
# ════════════════════════════════════════════════════════════════════════════
#  Process a list of transactions, each a tuple:
#      ("buy",  qty, price)   add a lot of inventory at that unit price
#      ("sell", qty, price)   sell units, matched to oldest inventory FIRST
#  Accumulate profit = units_sold * (sell_price - buy_price_of_those_units),
#  using FIFO cost basis. Selling more than you currently hold IS allowed and
#  creates a deficit. At the END, if any deficit remains, return the string
#  "INVALID: oversold by N" (N = leftover deficit). Otherwise return the
#  total profit as an int.
#
#  Canary input: [("buy",10,5),("sell",4,8),("buy",5,6),("sell",8,9)]
#
#  # TWIST: ____________________________________________________________
#  # TRACE: first sell matches __ units from the 10@5 lot -> profit += ____
def solve_c2(txns):
    # your code here
    pass


# ════════════════════════════════════════════════════════════════════════════
#  COMPLEX 3 — "Round Robin, Two-Strikes-Out"
# ════════════════════════════════════════════════════════════════════════════
#  Given a list of team names and a list of results (teamA, teamB, winner),
#  processed IN ORDER, return the surviving teams (sorted). A team is
#  ELIMINATED the moment it loses TWO MATCHES IN A ROW (a win resets its
#  losing streak to zero). Once a team is eliminated, any later match that
#  involves it is SKIPPED entirely (it has no effect on anyone).
#
#  Canary input:
#    teams = ["A","B","C"]
#    results = [("A","B","B"),("A","C","C"),("A","B","A"),
#               ("B","C","C"),("B","C","C")]
#
#  # TWIST: ____________________________________________________________
#  # TRACE: A loses match 1 (streak=1) then match 2 (streak=__) -> A is ____
def solve_c3(teams, results):
    # your code here
    pass


# ════════════════════════════════════════════════════════════════════════════
#  COMPLEX 4 — "CSV with Quotes and a SUM Formula"
# ════════════════════════════════════════════════════════════════════════════
#  Parse one CSV line into a list of fields. Fields are comma-separated, but a
#  comma INSIDE double quotes is literal text (and the quote characters
#  themselves are removed). THEN: any field whose text starts with '=' is a
#  FORMULA equal to the SUM of all integer-valued fields to its RIGHT. Replace
#  that field with the computed sum (as a string). Return the list of fields.
#
#  Canary input: 'x,=,10,20,foo,30'
#
#  # TWIST: ____________________________________________________________
#  # TRACE: the '=' field sums the integers to its right: __ + __ + __ = ____
def solve_c4(line):
    # your code here
    pass


# ════════════════════════════════════════════════════════════════════════════
#  COMPLEX 5 — "Maze BFS with Teleports"
# ════════════════════════════════════════════════════════════════════════════
#  A grid (list of equal-length strings):  'S' start, 'E' end, '#' wall,
#  '.' open floor. Lowercase letters are TELEPORT pads: stepping onto a pad
#  instantly moves you to the OTHER pad with the same letter (the teleport
#  itself costs no extra step). Find the FEWEST steps from S to E moving in 4
#  directions. Return the step count, or -1 if E is unreachable.
#
#  Canary input: ["S.b", "###", "b.E"]
#
#  # TWIST: ____________________________________________________________
#  # TRACE: stepping onto 'b' at (0,2) teleports you to ______
def solve_c5(grid):
    # your code here
    pass


# ════════════════════════════════════════════════════════════════════════════
#  COMPLEX 6 — "Instant Runoff, Eliminate Alphabetically-Last on Ties"
# ════════════════════════════════════════════════════════════════════════════
#  Run instant-runoff voting. Each ballot is a ranked list of candidate names.
#  Each round: count first-choice votes among still-active candidates. If a
#  candidate has STRICTLY MORE than half of the ballots, they win. Otherwise
#  eliminate the candidate with the FEWEST first-choice votes and re-count
#  (ballots fall through to their next active choice). TWIST: when several
#  candidates TIE for fewest, eliminate the one whose name is alphabetically
#  LAST. Return the winning candidate.
#
#  Canary input:
#    ballots = [["A","B","C"],["B","A","C"],["C","A","B"]]
#    candidates = ["A","B","C"]
#
#  # TWIST: ____________________________________________________________
#  # TRACE: round 1 counts are A=__ B=__ C=__ ; tie -> eliminate ____
def solve_c6(ballots, candidates):
    # your code here
    pass


# ════════════════════════════════════════════════════════════════════════════
#  COMPLEX 7 — "Curved Grades"
# ════════════════════════════════════════════════════════════════════════════
#  Given a list of integer scores, assign letter grades RELATIVE to the class
#  average (avg = sum // len, integer division). Boundaries:
#    A: score >= avg + 15
#    B: score >= avg + 5
#    C: score >= avg - 5
#    D: score >= avg - 15
#    F: otherwise
#  Return a list of letter grades aligned with the input order.
#
#  Canary input: [50, 55, 60, 62, 63]
#
#  # TWIST: Grades are decided using the class average, not fixed mark boundaries.
#  # TRACE: For [50, 55, 60, 62, 63], the average is 58, so the grade limits are calculated from 58.
def solve_c7(scores):
    if len(scores) == 0:
        return []
    average = sum(scores) // len(scores)
    grades = []
    for score in scores:
        if score >= average + 15:
            grades.append("A")
        elif score >= average + 5:
            grades.append("B")
        elif score >= average - 5:
            grades.append("C")
        elif score >= average - 15:
            grades.append("D")
        else:
            grades.append("F")

    return grades

# ════════════════════════════════════════════════════════════════════════════
#  COMPLEX 8 — "Rebuild the Chain, or Detect a Cycle"
# ════════════════════════════════════════════════════════════════════════════
#  Given a list of pairs (a, b), each meaning "a comes immediately before b",
#  rebuild the single linear ordering of all items and return it as a list.
#  Every item has at most one successor and one predecessor. If the links form
#  a CYCLE (so there is no valid starting point / linear order), return the
#  string "CYCLE DETECTED" instead.
#
#  Canary input: [("c","d"),("a","b"),("b","c")]
#
#  # TWIST: ____________________________________________________________
#  # TRACE: the unique start is the item with no predecessor, which is ____
def solve_c8(pairs):
    # your code here
    pass


# ════════════════════════════════════════════════════════════════════════════
#  SELF-CHECK  (VISIBLE cases only — passing these is NOT enough!)
#  The hidden TRAP tests check the twist. Read each problem carefully.
# ════════════════════════════════════════════════════════════════════════════
def _row(name, got, expected):
    status = "ok " if got == expected else "XX "
    if got is None:
        status = "-- "   # not attempted yet
    print(f"  [{status}] {name:<5} got={str(got):<22} expected={expected}")

def self_check():
    print("=" * 64)
    print("  VISIBLE SELF-CHECK  (the obvious cases only)")
    print("  Passing every line here does NOT mean you passed — the")
    print("  hidden trap tests check the twist in each problem.")
    print("=" * 64)

    # MEDIUM visible cases
    m1 = solve_m1(5) if solve_m1(5) is not None else None
    _row("M1", m1[2] if m1 else None, "Fizz")          # n=3
    _row("M2", solve_m2("apple orange"), 5)
    _row("M3", solve_m3([1, 2, 3]), [1, 2, 3])
    _row("M4", solve_m4([3, 1, 4, 2]), [3, 3, 4, 4])
    _row("M5", solve_m5("hi hi bye"), "hi")
    _row("M6", solve_m6([(0, 0), (1, 1)], 5), 2)
    _row("M7", solve_m7([1, 2, 3], [3, 4]), [1, 2, 4])

    # COMPLEX visible cases
    _row("C1", solve_c1("([]){}"), True)
    _row("C2", solve_c2([("buy", 10, 5), ("sell", 4, 8)]), 12)
    _row("C3", solve_c3(["A", "B"], [("A", "B", "A")]), ["A", "B"])
    _row("C4", solve_c4("a,b,c"), ["a", "b", "c"])
    _row("C5", solve_c5(["S.", ".E"]), 2)
    _row("C6", solve_c6([["A"], ["A"], ["B"]], ["A", "B"]), "A")
    _row("C7", solve_c7([70, 70, 70]), ["C", "C", "C"])
    _row("C8", solve_c8([("a", "b"), ("b", "c")]), ["a", "b", "c"])

    print("-" * 64)
    print("  Reminder: fill in your  # TWIST:  and  # TRACE:  comments.")
    print("  The grader runs HIDDEN trap tests on the canary inputs.")
    print("=" * 64)


if __name__ == "__main__":
    self_check()
