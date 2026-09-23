student = {"김철수":85, "이영희" : 92, "박민수" : 67, "최지우" : 74}
while True:
    n = int(input("1. 학생 등록\n\n2. 학생 조회\n\n3. 점수 수정\n\n4. 학생 삭제\n\n5. 전체 학생 출력\n\n6. 성적 통계\n\n7.등급별 학생 조회\n\n0.프로그램 종료\n\n==>"))
    def grade(score): #등급 계산 함수
        if(score >= 90):
             value = "A"
        elif(score < 90 and score >= 80):
            value = "B"
        elif(score < 80 and score >= 70):
            value = "C"
        elif(score < 70 and score >= 60):
            value = "D"
        else:
            value = "F"
        return value

    match n:
        case 1:# 학생 등록

            try:
                name = input("학생의 이름을 입력하시오:")
                if(name in student.keys()):
                        raise ValueError("이미 등록된 학생입니다.")
                score = int(input("학생의 점수를 입력하시오:"))
                if(score < 0 or score >100):
                    raise ValueError("0과 100 사이의 숫자를 입력하시오.")
                student[name] = score

            except ValueError as e:
                print(e.args)
            


        case 2:#학생 조회

            try:
                name = input("학생의 이름을 입력하십시오:")
                if(name not in student.keys()):
                   raise ValueError("등록되지 않은 학생입니다.")

                score = student[name]
                value = grade(score)
                print("=============================================")
                print(f"이름 = {name}, 점수 = {score}, 등급 = {value}")
                print("=============================================")
                    
            except ValueError as e:
                print(e.args)



        case 3: # 점수 수정

            try:
                name = input("학생의 이름을 입력하십시오:")
                if(name not in student.keys()):
                       raise ValueError("등록되지 않은 학생입니다.")
                bf_score = student[name]
                af_score = int(input("수정하실 점수를 입력하시오:"))
                if(af_score < 0 or af_score > 100):
                    raise ValueError("입력된 점수의 범위가 이상합니다")
                student[name] = af_score
                print("=============================================")
                print(f"변경 전 점수 = {bf_score}, 변경 후 점수 = {af_score}")
                print("=============================================")

            except ValueError as e:
                print(e.args)



        case 4:

                try:
                    name = input("학생의 이름을 입력하십시오.:")
                    if(name not in student.keys()):
                        raise ValueError("등록되지 않은 학생입니다.")
                    check = input("정말 등록된 학생을 삭제 하시겠습니까?(y/n):")
                    if(check == "y"):
                        del student[name]
                        print("삭제 되었습니다.")
                    else:
                        print("취소 되었습니다.")
                                         
               
                except ValueError as e:
                    print(e.args)
            
        case 5: #전체 학생 출력
            print("=============================================")
            for name, score in student.items():
                value = grade(score)
                num = len(student)
                
                print(f"이름 = {name}, 점수 = {score}, 등급 = {value}")
                

            print(f"전체 학생의 수 = {num}")
            print("=============================================")
            
        case 6: # 성적 통계
            import math
            scores = student.values()
            student_count = len(student)
            total_score = 0
            total_score = sum(scores)
            average_score = total_score / student_count
            highest_score = max(scores)
            lowest_score = min(scores)
            print("=============================================")
            print(f"학생 수 = {student_count}, 평균 = {average_score}, 최고점 = {highest_score}, 최저점 = {lowest_score}")
            print("=============================================")
            
        case 7:
            search_grade = input("조회할 등급(A/B/C/D/F): ").upper()

            result = []

            for name, score in student.items():
                student_grade = grade(score)

                if student_grade == search_grade:
                    result.append((name, score))

            if len(result) == 0:
                print("해당 등급의 학생이 없습니다.")
            else:
                print("=============================================")

                for name, score in result:
                    print(f"{name} : {score}점")

                print(f"총 {len(result)}명")

                print("=============================================")
             
        case 0: break
print("Good bye")
