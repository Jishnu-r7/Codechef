Weapon Value
Problem Code:
SC31

Problem
A competition with N participants (numbered 1 through N) is taking place in Chefland. There are N-1 rounds in the competition; in each round, two arbitrarily chosen contestants battle, one of them loses and drops out of the competition.

There are 10 types of weapons (numbered 1 through 10). You are given N strings S1, S2,.., SN for each valid i and j, the j-th character of Si is '1' if the i-th contestant initially has a weapon of type j or '0' otherwise. During each battle, for each type j such that both contestants in this battle currently have weapons of type jj, these weapons of both contestants are destroyed; after the battle, the winner collects all remaining (not destroyed) weapons of the loser. Note that each contestant may win or lose regardless of the weapons he/she has.

Chef is feeling bored watching the contest, so he wants to find the maximum possible number of weapons the winner of the tournament could have after the last battle, regardless of which contestants fight in which battles or the results of the battles. Can you help him?