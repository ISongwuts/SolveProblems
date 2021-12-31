def main():
    m,n = input().split(" ")
    matrix_a = []
    matrix_b = []
    
    for mat_A in range(int(n)):
        matrix_a.append(input().split(" "))
    for mat_B in range(int(n)):
        matrix_b.append(input().split(" "))
        
    sum_of_mat = []
    for rows in range(len(matrix_a)):
        for cols in range(len(matrix_a[rows])):
            sum_of_mat.append([matrix_a[rows][cols] + matrix_b[rows][cols]])
    
    for index in range(len(n)):
        print(sum_of_mat[index], sep=" ")

if __name__ == '__main__':
    main()
    