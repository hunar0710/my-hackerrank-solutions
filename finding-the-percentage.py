if __name__ == '__main__':
    n = int(input().strip())
    student_marks = {}

    # Read each student's name and 3 marks
    for _ in range(n):
        name, *marks = input().split()
        student_marks[name] = list(map(float, marks))

    # Read query name
    query_name = input().strip()

    # Compute average and print with 2 decimal places
    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{avg:.2f}")
