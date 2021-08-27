# Monster Games with Dictionaries

<b>Two versions of a game with monsters:</b>
1. Simple: uses a dictionary with names for keys and descriptions for values. User can look up monsters by name 
2. Complex: uses a dictionary with ID for keys and a list of values (including name, origin, and monster stats) to implement a turn-based fighting game

All functionality in both games is organised neatly into modules (functions and procedures) 


<b>Complex Monsters:</b> 
1. Users can select their monsters by either ID or name: users can browse through various monsters before making a permanent selection 
2. Users take turns to play moves, starting with Player 1
3. At each turn, users can first check their stats: then, they make a selection from 5 possible moves (detailed below)
4. The game ends when one of the players die (health = 0)


<b>Monster Stats:</b>
1. Attack (A): the attack power of the monster
2. Magical Force (MF): spent on restoring health (1 MF --> 1 Health)
3. Magical Defense (MD): spent on setting up a temporary defense, depletes to 0 after enemy attack 
4. Defense (D): latent; reduces effect of attacks (multiplier of MD/10 + 1)
5. Intelligence (I): latent; increases attack power (multiplier of I/10 + 1)
6. Health (H): tracks monster health, once reaches 0 the game ends
7. Experience (EXP): spent on increasing either attack or defense power (1 EXP --> 1 A or 1D)


<b>Player Abilities:</b>
1. Attack: deals damage to the opponent (formula: [int(A/6)x(I/10 + 1) - int(OtherPlayerMD/5)x(OtherPlayerD/10 + 1)])
2. RestoreHealth: restores +5 H from MF 
3. BoostDefense: increases +3 D from EXP
4. BoostAttack: increases +3 A from EXP
5. SetupDefense: player selects how much MD to spend (temporary, lasts for one attack only)
