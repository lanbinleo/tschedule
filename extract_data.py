import pandas as pd
import json
import os

def check_folder_exists():
    # 创建需要的文件夹
    if not os.path.exists('data'):
        os.makedirs('data')

def read_excel_file(file_path, sheet):
    # 使用pandas读取Excel文件
    data = pd.read_excel(file_path, sheet_name=sheet)
    return data

def remove_all_RNM(data_frames):
    # 传入一个包含dataframe的字典，遍历其所有表格，将任何字段中的“ RNM”替换为空，使用.replace()方法
    for key, df in data_frames.items():
        data_frames[key] = df.replace(' RNM', '', regex=True)
    return data_frames

def process_courses_selection(data_courses, data_selection):
    # 将所有课程加入字典
    all_courses_dict = data_courses.set_index('Subject').to_dict('index')

    # 将年级字段转换为字符串类型
    data_selection['Grade'] = data_selection['Grade'].astype(str)
    data_selection = remove_all_RNM(data_selection)

    # 创建课程-学生映射字典
    course_student_mapping = {course: [] for course in all_courses_dict.keys()}

    # 创建学生-课程映射字典
    student_course_selection = {}
    for _, row in data_selection.iterrows():
        student_number = row['Student Number']
        # 初始化学生选课字典
        if student_number not in student_course_selection:
            student_course_selection[student_number] = {
                'Math': [],
                'English': [],
                'Chinese': [],
                'Humanities': [],
                'Science': [],
                'Computer Science': [],
                'Art': [],
            }
        
        # 添加学生选择的课程
        for subject in student_course_selection[student_number].keys():
            course_name = row.get(subject)
            course_names = str(course_name).split('; ')
            for course in course_names:
                if pd.notnull(course) and course in all_courses_dict:
                    student_course_selection[student_number][subject].append(course)
                    course_student_mapping[course].append(student_number)
    
    return student_course_selection, all_courses_dict, course_student_mapping

def store_data(filename, data, prefix='data/'):
    # 将NaN替换成null
    with open(prefix + filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    # 检查文件夹是否存在
    check_folder_exists()

    # 假设Excel文件路径如下，需要替换为实际的文件路径
    sheet_name_courses = 'Courses'
    sheet_name_selection = 'Course Selection'
    file_path = "raw_data.xlsx"
    
    # 读取Excel文件
    courses_data = read_excel_file(file_path, sheet_name_courses)
    selection_data = read_excel_file(file_path, sheet_name_selection)

    # 处理课程和学生选择信息
    table, all_courses, mapping = process_courses_selection(courses_data, selection_data)

    # 打印处理后的数据
    store_data('course_stuId_mapping.json', mapping)
    store_data('course_details.json', all_courses)
    store_data('student_course_mapping.json', table)