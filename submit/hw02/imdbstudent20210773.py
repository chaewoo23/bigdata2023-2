import sys
from collections import Counter

if len(sys.argv) < 3:
    print("실행 방법: python imdbstudent20210773.py <filename1> <filename2>")
    sys.exit(1)
else:
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    with open(filename1, 'r') as file1:
        movieDat = [line.strip().split("::") for line in file1.readlines()]

    movieGenreDat = [x[2] for x in movieDat]

    genres = '|'.join(movieGenreDat).split('|')
    genre_count = Counter(genres)

    with open(filename2, 'w') as file2:
        for genre, count in genre_count.items():
            file2.write(f"{genre} {count}\n")
