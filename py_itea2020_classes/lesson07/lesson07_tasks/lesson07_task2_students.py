import sqlite3


class UserConnection:

    def __init__(self, file_name):
        self._connect = sqlite3.connect(file_name)
        self._cursor = self._connect.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cursor.close()

    def get_all_students(self):
        self._cursor.execute('select * from student')
        return self._cursor.fetchall()

    def get_excellent_students(self):
        self._cursor.execute('select s.id, s.first_name, s.last_name, s.group_id, s.student_ticket_number, '\
                             '       avg(sm.mark) avg_mark '\
                             '  from student s '\
                             '  inner join student_mark sm on s.id = sm.student_id '\
                             ' group by s.id, s.first_name, s.last_name, s.group_id, s.student_ticket_number '\
                             ' having avg(sm.mark)>4.5')
        return self._cursor.fetchall()

    def get_student_by_student_ticket_number(self, num):
        self._cursor.execute('select * from student where student_ticket_number = ?',(num,))
        return self._cursor.fetchall()

    def get_full_student_info_by_id(self, id_):
        self._cursor.execute('select s.id, s.first_name, s.last_name, s.student_ticket_number, '\
                             '       g.group_number, f.faculty_name'\
                             '   from student s'\
                             '   left join "group" g on s.group_id = g.id'\
                             '   left join faculty f on g.faculty_id = f.id'\
                             '  where s.id=?', (id_,))
        student_info = self._cursor.fetchall()
        self._cursor.execute('select s.subject_name, sm.mark '\
                             '   from student_mark sm'\
                             '   left join subject s on sm.subject_id = s.id'\
                             '  where sm.student_id=?', (id_,))
        marks_info = self._cursor.fetchall()
        return student_info, marks_info

class AdminConnection(UserConnection):

    def add_new_student(self, first_name, last_name, group_id, ticket_number):
        self._cursor.execute('insert into student (first_name, last_name, group_id, student_ticket_number) values (?, ?, ?, ?)',(first_name, last_name, group_id, ticket_number))

    def modify_student(self, id_, first_name, last_name, group_id, ticket_number):
        self._cursor.execute('update student set first_name=?, last_name=?, group_id=?, student_ticket_number=? where id=?',(first_name, last_name, group_id, ticket_number, id_))

print('******User Connection******')
with UserConnection('students.db') as regular_user:
    print('***All users***')
    print(regular_user.get_all_students())
    print('***Excellent users***')
    print(regular_user.get_excellent_students())
    print('***Find user with student number fgf6563g')
    print(regular_user.get_student_by_student_ticket_number('fgf6563g'))
    print('***Get full information for user with id = 5')
    user_info, marks = regular_user.get_full_student_info_by_id(5)
    print(user_info)
    print(marks)

print('******Admin Connection******')
with AdminConnection('students.db') as admin_user:
    print('***Adding new user***')
    admin_user.add_new_student('Charles', 'Tompson', 3, 'dfdf567')
    print('***Modify user with id = 2')
    admin_user.modify_student(2, 'Mary', 'Lewis', 2, 'fgf6563g')
    print('***All users***')
    print(admin_user.get_all_students())
    print('***Excellent users***')
    print(admin_user.get_excellent_students())
    print('***Find user with student number fgf6563g')
    print(admin_user.get_student_by_student_ticket_number('fgf6563g'))
    print('***Get full information for user with id = 5')
    user_info, marks = admin_user.get_full_student_info_by_id(5)
    print(user_info)
    print(marks)
