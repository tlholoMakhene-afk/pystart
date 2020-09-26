class student:

    def __init__(self, _studid, _studname, _studage):
        self.studentid = _studid
        self.studentname = _studname
        self.studentage = _studage

    def __repr__(self):
        return 'Student(Student ID:{!r}, StudentName: {!r}, StudentAge: {!r})'.format(self.studentid,self.studentname,self.studentage)
