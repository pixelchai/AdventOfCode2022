score_matrix = [
    [3,6,0],
    [0,3,6],
    [6,0,3],
]  # rock paper scissors matrix [player1][player2] -> score
shape_score = [1,2,3]

total_score = 0
for line in open("input.txt"):
    line = line.strip()
    if len(line) > 0:
        player1, player2 = line.split(" ")
        index_player1 = "ABC".index(player1)
        index_player2 = "XYZ".index(player2)

        score = score_matrix[index_player1][index_player2] + shape_score[index_player2]
        total_score += score

print(total_score)