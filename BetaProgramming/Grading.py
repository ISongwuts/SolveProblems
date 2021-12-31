def calGrade(keep_point:int, mid_point:int, final_point:int) -> str:
    total_point = keep_point + mid_point + final_point
    point_pattern = [
        [80,100],
        [75,79],
        [70,74],
        [65,69],
        [60,64],
        [55,59],
        [50,54],
        [0,49]
    ]
    dict_grade = {
        0: "A",
        1: "B+",
        2: "B",
        3: "C+",
        4: "C",
        5: "D+",
        6: "D",
        7: "F"
    }
    for index in range(len(point_pattern)):
        if total_point >= 0 and total_point <= 100 and total_point >= point_pattern[index][0] and total_point <= point_pattern[index][1]:
            return dict_grade[index]
    
    

def main():
    keep_point:int = int(input())
    mid_point:int = int(input())
    final_point:int = int(input())
    print(calGrade(keep_point, mid_point, final_point))

if __name__ == '__main__':
    main()
    