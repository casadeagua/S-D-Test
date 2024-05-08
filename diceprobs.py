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
    return avg, rravg

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

## Sorc with all mana sides set to 2
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
        rolls = rolls + 1
        state = "reroll"
        rerollcount = rerollcount + 1

## another character with a RR side
def otherroller():
    global rolls
    r = roll()
    if r == 6:
        rolls = rolls + 1

## another character with a 2 RR side
def otherroller_2():
    global rolls
    r = roll()
    if r == 6:
        rolls = rolls + 2


## This is the code to test the characters ------------------------------------------------------------------------
## iter = how many iterations to test, I recomend minimum 10k to have valid results
iter_sim(sorc, iter = 1000000)

iter_sim(sorc, otherroller, iter = 1000000)

iter_sim(sorc, otherroller_2, iter = 1000000)

iter_sim(sorc_2, iter = 1000000)

## with 4 starting rerolls
iter_sim(sorc, iter = 1000000, start_roll = 4)
