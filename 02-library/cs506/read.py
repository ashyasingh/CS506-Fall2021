def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    data = pd.read(csv_file_path)
    matrix = []
    for x in range(len(data)):
        for y in range(len(data[0])):
            matrix[x][y] = data[x][y]
    return matrix
