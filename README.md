# TournamentValidation

This code is to validade the input of participants of a tournament.
The tournament has X number of participants, for example 8, these participants are represented by consecutive numbers starting from 1 that are in an array.
And the number of each participant is the score for each participant, the number 1 being the highest score and 8 the lowest score.

Rule: Highest rank should always be matched with lowest available rank
1 - 8
2 - 7
3 - 6
4 - 5

The tournament rounds are in pairs and are defined based on the scores, always combining the highest score with the lowest and the participant with the highest score will always win. Example:

Input: [1, 8, 4, 5, 2, 7, 3, 6]
1st: [1, 8] [4, 5], [2, 7], [3, 6]
2nd: [1, 4], [2, 3]
Final: [1, 2]
Winner: 1
