import math
from operator import mul
from re import match

with open('./inp/11.txt') as f:
    notes = f.read().split('\n\n')

class Monkey:
    def __init__(self, id, startingItems, operation, test, true_throw_to, false_throw_to, reduce_worry = True):
        self.id = int(id)
        self.items = list(map(int, startingItems.split(', ')))
        self.operation = match(r'new = (.+)', operation).groups()[0]
        self.test = int(test.split(' ')[-1])
        self.true_throw_to = int(true_throw_to.split(' ')[-1])
        self.false_throw_to = int(false_throw_to.split(' ')[-1])
        self.activity = 0
        self.reduce_worry = reduce_worry

    def take_turn(self):
        global monkeys
        global lcm

        for item_i in range(len(self.items)):
            # Do operation
            old = self.items[item_i]
            self.items[item_i] = eval(self.operation)

            # Get bored if part A
            if self.reduce_worry:
                self.items[item_i] = self.items[item_i] // 3

            # Is divisible? 
            is_divisible = self.items[item_i] % self.test == 0

            # Part A
            if self.reduce_worry:
                if is_divisible:
                    monkeys[self.true_throw_to].items.append(self.items[item_i])
                else:
                    monkeys[self.false_throw_to].items.append(self.items[item_i])

            # Part B
            else:
                if is_divisible:
                    monkeys[self.true_throw_to].items.append( self.items[item_i] % math.lcm(lcm, monkeys[self.true_throw_to].test))
                else:
                    monkeys[self.false_throw_to].items.append(self.items[item_i] % math.lcm(lcm, monkeys[self.false_throw_to].test))

            self.activity += 1 

        self.items = []

########
# Part A
########

# Set up monkeys from input
monkeys = {}
for m_note in notes:
    monkey = Monkey(*match(r'Monkey ([0-9]):\n  Starting items: (.+)\n  Operation: (.+)\n  Test: (.+)\n    If true: throw to monkey ([0-9])\n    If false: throw to monkey ([0-9])', m_note).groups()) 
    monkeys[monkey.id] = monkey

# Run Rounds
for round in range(20):
    for m_id in range(len(notes)):
        monkeys[m_id].take_turn()

top_two = list(sorted(monkeys.values(), key=lambda m: m.activity, reverse=True))[:2]
print(top_two[0].activity * top_two[1].activity)

########
# Part B
########

monkeys = {}
for m_note in notes:
    monkey = Monkey(*match(r'Monkey ([0-9]):\n  Starting items: (.+)\n  Operation: (.+)\n  Test: (.+)\n    If true: throw to monkey ([0-9])\n    If false: throw to monkey ([0-9])', m_note).groups()) 
    monkey.reduce_worry = False
    monkeys[monkey.id] = monkey

# LCM of each monkey's test value. Used in take turn function as a global (lazy)
lcm = math.lcm(*[m.test for m in monkeys.values()])

# Run Rounds
for round in range(10000):
    for m_id in range(len(notes)):
        monkeys[m_id].take_turn()

top_two = list(sorted(monkeys.values(), key=lambda m: m.activity, reverse=True))[:2]
print(top_two[0].activity * top_two[1].activity)