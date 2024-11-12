import pandas as pd
import json
from tabulate import tabulate

# 读取数据文件
with open('data/student_course_mapping.json', 'r') as f:
    data = json.load(f)

def filter_data(data, subject, course, column):
    # 筛选出选择了特定课程的学生
    filtered_students = [student for student, courses in data.items() if course in courses.get(subject, [])]
    # 统计这些学生在其他学科选择的课程数量
    course_counts = {}
    for student in filtered_students:
        for selected_course in data[student].get(column, []):
            if selected_course in course_counts:
                course_counts[selected_course] += 1
            else:
                course_counts[selected_course] = 1
    return course_counts

def get_student_courses(data, student_ids):
    if isinstance(student_ids, str):
        student_ids = [student_ids]
    
    student_courses = {student_id: data.get(student_id, {}) for student_id in student_ids}
    
    if len(student_ids) == 1:
        student_id = student_ids[0]
        courses = student_courses.get(student_id, {})
        print(f"学生 {student_id} 的课程：")
        for subject, course_list in courses.items():
            print(f"{subject}: {', '.join(course_list)}")
    else:
        course_counts = {}
        for student_id in student_ids:
            courses = student_courses.get(student_id, {})
            for subject, course_list in courses.items():
                for course in course_list:
                    if course in course_counts:
                        course_counts[course] += 1
                    else:
                        course_counts[course] = 1
        print("学生们的课程统计：")
        sorted_course_counts = dict(sorted(course_counts.items(), key=lambda item: item[1], reverse=True))
        print(tabulate(pd.DataFrame(list(sorted_course_counts.items()), columns=['Course', 'Count']), headers='keys', tablefmt='grid'))

def main():
    # 示例：选择了Math栏目的Precalculus的学生在Math栏目选择了多少别的学科
    math_precalculus_counts = filter_data(data, 'Math', 'AP Pre-Calculus', 'Math')
    print("Math栏目的AP Pre-Calculus的学生在Math栏目选择的其他学科数量：")
    print(tabulate(pd.DataFrame(list(math_precalculus_counts.items()), columns=['Course', 'Count']), headers='keys', tablefmt='grid'))

    # 示例：选择了IGCSE Math的人在Humanities选择的占比
    igcse_math_humanities_counts = filter_data(data, 'Math', 'IGCSE Math', 'Humanities')
    print("\n选择了IGCSE Math的人在Humanities选择的课程数量：")
    print(tabulate(pd.DataFrame(list(igcse_math_humanities_counts.items()), columns=['Course', 'Count']), headers='keys', tablefmt='grid'))

    # 示例：获取单个学生的课程
    get_student_courses(data, '1')

    # 示例：获取多个学生的课程统计
    get_student_courses(data, ['1', '2', '3'])

if __name__ == '__main__':
    main()