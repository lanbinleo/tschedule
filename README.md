# 问题描述 / Problem Description

我们目前的问题是我有很多课程，每个课程有若干个班级，每个班级有很多学生。

现在我要首先把每一个学生放在一个班级里，然后再把每一个班级排到课程表里。

课程表一共有24个时段，每个时段可以有若干班级，一个学生不可以在同一时段的两个班级里，如果在的话就说明发生了冲突，这不是一个很好的选项。我们要做的就是找到一种方法，安排学生并排列课表，使得冲突最小。现在的最大问题是，当我们修改学生的安排后，可能会影响现有时间表的冲突数量。

换而言之就是学生的安排和班级课表安排是互相影响的。

Our current problem is that we have many courses, each course has several classes, and each class has many students. Now we need to first place each student in a class, and then schedule each class into the timetable. The timetable has 24 time slots, and each time slot can have several classes. A student cannot be in two classes at the same time slot; if they are, it indicates a conflict, which is not a good option. What we need to do is find a way to arrange students and schedule classes to minimize conflicts. The biggest problem now is that when we modify the arrangement of students, it may affect the number of conflicts in the existing timetable. In other words, the arrangement of students and the scheduling of classes are interdependent.