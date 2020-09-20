# MarioParty5_RNG

Digging into how Mario Party 5 handles RNG.

## RNG Function

I've found two random functions in the game's code so far. They are similar to the [HSD_Rand](https://github.com/doldecomp/gnt4/blob/master/src/sysdolphin/random.c#L11) and [HSD_Randi](https://github.com/doldecomp/gnt4/blob/master/src/sysdolphin/random.c#L31) functions provided by [sysdolphin](https://wiki.mariocube.com/index.php/Sysdolphin). I've named them `rand` and `randi` respectively.

![Rand Function](/img/rand.PNG?raw=true "Rand Function")

`rand` returns a random integer. [Source](https://gist.github.com/NicholasMoser/ec152e10388a786d86ec6be85f184b9d)

![Randi Function](/img/randi.PNG?raw=true "Randi Function")

`randi` returns a random integer between 0 and the parameter provided non-inclusive. [Source](https://gist.github.com/NicholasMoser/a17c38d41692364e9cf2e4b86aae1e98)

Both are definitely a [Linear congruential generator](https://en.wikipedia.org/wiki/Linear_congruential_generator). They also appear to be a [Lehmer Random Number Generator](https://en.wikipedia.org/wiki/Lehmer_random_number_generator).

## Capsule IDs

When getting an capsule from the capsule machine, items have the following internal IDs:

- 00 = Mushroom
- 01 = Super Mushroom
- 02 = Cursed Mushroom
- 03 = Warp Pipe
- 04 = Klepto
- 05 = Bubble
- 06 = Wiggler
- 07 = ERROR CAPSULE
- 08 = ERROR CAPSULE
- 09 = ERROR CAPSULE
- 0A = Hammer Bro
- 0B = Coin Block
- 0C = Spiny
- 0D = Paratroopa
- 0E = Bullet Bill
- 0F = Goomba
- 10 = Bomb-omb
- 11 = Koopa Bank
- 12 = ERROR CAPSULE
- 13 = ERROR CAPSULE
- 14 = Kamek
- 15 = Mr. Blizzard
- 16 = Piranha Plant
- 17 = Magikoopa
- 18 = Ukiki
- 19 = Lakitu
- 1A = ERROR CAPSULE
- 1B = ERROR CAPSULE
- 1C = ERROR CAPSULE
- 1D = ERROR CAPSULE
- 1E = Tweester
- 1F = Duel
- 20 = Chain Chomp
- 21 = Bone
- 22 = Bowser
- 23 = Chance
- 24 = Miracle
- 25 = Donkey Kong
- 26 = VS
- 27 = ERROR CAPSULE
- 28 = ERROR CAPSULE (DEBUG)
- 29 = ERROR CAPSULE (DEBUG)
- 2A = ERROR CAPSULE

Obtaining an item with an item ID over 2A results in a soft lock.

![2B Or Higher Softlock](/img/2b_or_higher_softlock.PNG?raw=true "2B Or Higher Softlock")

Any capsule labeled ERROR CAPSULE looks like this when obtained:

![Error Capsule](/img/error_capsule.PNG?raw=true "Error Capsule")

When you attempt to use it, the model for it is apparently some level geometry:

![Error Capsule Use](/img/error_capsule_use.PNG?raw=true "Error Capsule Use")

If you use it on yourself it crashes the game. If you throw it though...

![Error Capsule Throw](/img/error_capsule.GIF?raw=true "Error Capsule Throw")

The items labeled `ERROR CAPSULE (DEBUG)` are capsules used for debugging the game. They have actual models but don't appear to do anything.

![Debug Capsule](/img/error_0x29.PNG?raw=true "Debug Capsule")

## Capsule Randomness

When you come to a capsule machine, you get a random capsule. The item ID you get is returned from the the result of calling the function `FUN_800c8fa0` at `0x800c0cb0`.

I've began documenting the function here: [random_capsule.c](https://gist.github.com/NicholasMoser/02b477cd16e1d5ea1ba6e8c4cea1333e)

My current understanding is that it iterates through every capsule in the game, and adds **some**[1] of those items to a list. It then iterates through that list of items **5 times** and swaps the current item in the iteration with a random other item in the list. It will not swap if the random other item happens to match the current item. Therefore, anywhere between 0 and `number of items in the list` swaps will occur.

Once the swaps are complete, a random capsule is grabbed from the list. Each item in the list has an equal chance of being grabbed.

[1] I have yet to determine how it decides which items to add. It is doing some comparison against game data, but it's not clear what it represents yet.
