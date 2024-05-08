import random

### Nuts and Bolts: --------------------------------------
## roll a die
def roll():
    r = random.randint(1, 6)
    return(r)

## simulates a turn of slice and dice
def runsim(*characters, t_roll = 3):
    global rolls
    rolls = t_roll
    while rolls > 0:
        rolls = rolls - 1
        for character in characters:
            character()
    return(mana)

## runs the simulation and finds averages
def iter_sim(*chars, iter = 100000, start_roll = 3):
    global rolls
    global mana
    global rerollcount
    results = []
    rerollcount = 0
    for i in range(iter):
        mana = 0
        runsim(*chars, t_roll = start_roll)
        results.append(mana)
    avg = sum(results) / len(results)
    rravg = rerollcount / len(results)
    zero_count = (results.count(0) / len(results)) * 100
    one_count = (results.count(1) / len(results)) * 100
    two_count = (results.count(2) / len(results)) * 100
    three_count = (results.count(3) / len(results)) * 100
    four_count = (results.count(4) / len(results)) * 100
    five_plus_count = (len([i for i in results if i >= 5]) / len(results)) * 100

    print(
        "\nAvg Mana: ", round(avg, 1), ", RRs/Turn: ", round(rravg, 1),
        "\n\nMana Gained:", 
        "\n0: ", round(zero_count, 1),  "%",
        "\n1: ", round(one_count, 1), "%",
        ", 2: ", round(two_count, 1), "%",
        ", 3: ", round(three_count, 1), "%",
        ", 4: ", round(four_count, 1), "%",
        ", 5+: ", round(five_plus_count, 1), "%",
        sep = ""
    )

### CHARACTERS: -------------------------------------------
## If yall want to add another character, just copy one of the ones here and change the if statements to match (the state variable is unused currently)
## You would have to change code to do something other than mana. However, you could use "mana" to mean pips 
    ## and just find how much damage, or shields is rolled, for example
## If there's enough demand I could implement this myself and have seperate running counts for each

## base sorc
def sorc():
    global mana
    global rolls
    global rerollcount
    state = "blank" ## if not the other sides, will show as blank
    r = roll()
    if r > 3:
        mana = mana + 1
        state = "mana"
        if rolls == 0:
            mana = mana + 1
    if r == 3:
        rolls = rolls + 1
        state = "reroll"
        rerollcount = rerollcount + 1

## Sorc with all sides set to 2
def sorc_2():
    global mana
    global rolls
    global rerollcount
    state = "blank"
    r = roll()
    if r > 3:
        mana = mana + 2
        state = "mana"
        if rolls == 0:
            mana = mana + 2
    if r == 3:
        rolls = rolls + 2
        state = "reroll"
        rerollcount = rerollcount + 2

## another character with a RR side (bard, for example)
def otherroller():
    global rolls
    global rerollcount
    r = roll()
    if r == 6:
        rolls = rolls + 1
         rerollcount = rerollcount + 1

## Sphere with 2 (1)RR sides
def sphere():
    global rolls
    global rerollcount
    r = roll()
    if r > 4:
        rolls = rolls + 1
        rerollcount = rerollcount + 1


## This is the code to test the characters ------------------------------------------------------------------------
## iter = how many iterations to test, I recomend minimum 10k to have valid results, but you only need to change if it takes too long
iter_sim(sorc, iter = 1000000)

iter_sim(sorc, otherroller, iter = 1000000)

iter_sim(sorc, sphere, iter = 1000000)

iter_sim(sorc_2, iter = 1000000)

## with 4 starting rerolls
iter_sim(sorc, iter = 1000000, start_roll = 4)
