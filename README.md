# Slice and Dice Probabilities

Find out the results of those wacky little dice!

Code is in the "diceprobs.py" file

Found using brute force, 1 million iterations

# Results:

Each represent the percentage chance of getting that amount of mana

AVG mana and AVG RRs are how many you can expect in a turn 

This assumes you always roll until out of RRs and does count the extra you get if you end on a mana side

| Character         											| 0 mana	| 1 mana	| 2 mana	| 3 mana	| 4 mana	| 5+ mana | AVG Mana | Avg RRs |
| :------------------------------		| :----:	|	:----:	| :----:	|	:----:	|	:----:	|	:----:	| :----:	| :----:	|
| Base Sorc 									 			| 6.4% | 19.3% | 24.0% | 28.8% | 21.6% | 0% | 2.4 | 0.6 |
| Sorc W/ 1 RR (Bard, for example) 	| 4.3% | 14.0% | 20.0% | 25.6% | 22.7% | 13.4% | 3.0 | 1.5 |
| Sorc W/ Sushi on other Char       | 3.6% | 11.6% | 16.6% | 21.7% | 20.1% | 26.4% | 3.7 | 3.0 | 
| Sorc W/ Sphere										| 2.5% | 8.9% | 14.5% | 20.3% | 21.0% | 32.7% | 3.9 | 3.0 |
| Sorc W/ 2 on each side						| 4.5% | 0.0% | 14.6% | 0.0% | 21.2% | 59.7% | 5.7 | 1.5 |
| Sorc W/ 4 starting RRs 						| 2.6% | 11.6% | 21.1% | 25.9% | 25.9% | 13.0% | 3.0 | 0.8 |


# Note!
The averages with 2 characters is slightly inflated. 
As written, it adds the mana when rerolls is 0 (like you locked dice), but if the other character rolls a reroll, it will add what they roll next too. This only happens 1/36 times, so shouldn't be too impactful, but I might come back and fix later.
