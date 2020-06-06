from random import sample


def season_schedule_order(teams, pairs):
    n_games_per_round = len(teams) // 2
    last_pairs = set()
    while pairs:
        r_pairs = set(sample(pairs, n_games_per_round))
        # Check that each team is present once in the round.
        r_teams = set(x for (x, y) in r_pairs) | set(y for (x, y) in r_pairs)
        if r_teams != teams:
            continue
        # Check that two teams doesn't face each other again.
        rev_pairs = set((y, x) for (x, y) in r_pairs)
        if rev_pairs & last_pairs:
            continue
        pairs -= r_pairs
        for p in r_pairs:
            yield p
        last_pairs = r_pairs


if __name__ == "__main__":
    teams_input = []
    players = int(input("How many teams? "))

    for player in range(players):
        team = input("Enter a team: ")
        teams_input.append(team)

    teams = set(teams_input)
    pairs = set((x, y) for x in teams for y in teams if x != y)
    for (home, away) in season_schedule_order(teams, pairs):
        print('{} vs. {}'.format(home, away))
