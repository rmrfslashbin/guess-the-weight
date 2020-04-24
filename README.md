# guess-the-weeight
[Z3 solver](https://github.com/Z3Prover/z3) PoC to calculate a weight plate combo to hit the desired weight.

## Install
Use [pipenv](https://github.com/pypa/pipenv) to set up the envionment or `pip install -r requirements.txt`.

## Use
```
$ ./test  --help
usage: test [-h] [--tries TRIES] --goal GOAL --bar {7,22} {range,pong} ...

Optimize plates

positional arguments:
  {range,pong}   sub-command help

optional arguments:
  -h, --help     show this help message and exit
  --tries TRIES  Max number of tries (default: 10)
  --goal GOAL    Weight goal
  --bar {7,22}   Bar weight
```
## Example
```
$ ./test --bar 7 --goal 100 pong
After 2 tries...

10 * 4 = 40
8.8 * 2 = 17.6
8 * 2 = 16
5 * 4 = 20

Bar: 7
Plates: 12
Total: 100.6
```
## Weights
The weights (a, b, c, d, and e) and the bar (q) are statically designated in the code:
```
weights = {
    "a": {"wght": 13.2, "qty": 4},
    "b": {"wght": 10, "qty": 4},
    "c": {"wght": 8.8, "qty": 6},
    "d": {"wght": 8, "qty": 2},
    "e": {"wght": 5, "qty": 4},
    "q": {"wght": bar, "qty": 1}
}
```
For example, I have four 13.2 lbs plates and six 8.8 lbs plates (among others). The bar weights are designated in the `argparser` as either 7 or 22 lbs.

## Methodology
I have two non-standard bars to go with a pile of non-standard weight plates. The bars weigh 7 and 22 pounds, respectively. I wanted to easily calculate the best bar/plate combo to hit near or at a specified weight. I also wanted to tinker with Z3 Solver. Sounds like a good PoC to me!
### Pong and Range
Z3 Solver can get close to the target weight (which is defined by a upper and lower bound range), but sometimes the odd combos makes the results a bit off. To help Z3 get closer to the target weight I created two methods to solve the problem: pong and range. For example, to hit 100 pounds total, a target range may be internally defined as 95 lbs to 105 lbs. The goal is to get *close* to 100 lbs.
#### Pong
Pong, which is more accurate but slower, starts with the target and then tests incrementally distant weights above and below the target until a maximum number of tries:
```
goal = 100
try = {try #}

Try 0:
Upper = goal + try + 1
Lower = goal + try - 1

Try 1:
Upper = goal - try + 1
Lower = goal - try - 1
```

#### Range
Range is a little simpler than pong, but less accurate and faster. For each test loop, the range is expanded by +1 a -1 pound until the problem is solved until a maximum number of tries.





