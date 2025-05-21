class Student:
    name =""
    score ={}
    # 
def score_average(self):
    return (self.scores['Toán'] + self.scores['Văn'] + self.scores['Anh']) / 3

def show_rank(self):
    avg_score = int(self.score_average())
    if avg_score >= 10:
        return 'ổn'
    elif avg_score >= 8:
        return 'bình thường'
    elif avg_score >= 7:
        return 'Giốt'
    else:
        return 'quá giốt'
def show_info_student(self):
    print("Họ tên: ", self.name)
    for key in self.scores:
        print(f"Điểm môn {key}: {self.scores[key]}") 
    average_return = self.score_average() 
    average_return = round(average_return, 2)
    print("Điểm trung bình ba môn: ", average_return) 
    print("Học sinh xếp loại: ", self.show_rank()) 

self = Student()
self.name = 'Nguyễn Đức Khang'
self.scores = {
    'Toán': 10,
    'Văn': 10,
    'Anh': 10
}
self.show_info_student()
