from member import MemberService

ms = MemberService()


# 회원 관리 메인 UI 및 로직 제어
def select_menu():
    while True:
        print('===========================================================================================')
        print('1. 회원가입 | 2. 회원목록 | 3. 회원상세정보 | 4. 회원정보수정 | 5. 회원탈퇴 | 0. 시스템종료')
        print('===========================================================================================')
        # 메뉴 입력받기
        # 0 ~ 5까지만 입력 받기(다른 숫자이면 올바르게 입력할 때까지 받기)
        try:
            menu = int(input('>>메뉴 선택 : '))

            if not (0 <= menu <= 5):
                raise Exception
            return menu
        except Exception:
            print('=========================[오류] 0 ~ 5까지의 숫자로만 입력하시오=========================')
    

    
print()
print('=======================================미니 프로젝트=======================================')

while True:
    menu = select_menu()

    if menu == 0: #(0. 시스템종료)
        print('===========================================================================================')
        print('====================================서비스를 종료합니다====================================')
        print('===========================================================================================')
        break

    elif menu == 1: #(1. 회원가입 [회원번호: num / 아이디: id / 비밀번호: pw / 이름: name / 전화번호: phone / 주소: address])
        # 회원번호 입력
        num = ms.check_num()
        # 아이디 입력
        id = input('> 아이디 : ')
        # 비밀번호 입력
        pw = input('> 비밀번호 : ')
        # 이름 입력
        name = ms.check_name()
        # 전화전호 입력
        phone = ms.check_phone()
        # 주소 입력
        address = input('> 주소 : ')

        if ms.Create_Member(num, id, pw, name, phone, address):
            print('====================================계정 생성되었습니다====================================')

    elif menu == 2: #(2. 회원목록)
        Member_list = ms.Get_Member_list()
        print('---------------------------------------')
        print('----------------회원목록----------------')
        print('---------------------------------------')
        for mem in Member_list:
            print(mem)


    elif menu == 3: #(3. 회원상세정보)
        print('---------------------------------------')
        print('--------------회원상세정보--------------')
        print('---------------------------------------')
        id = input('>조회할 아이디 : ')
        member = ms.Search_Member(id)
        if member:
            print(f'{member}')
        else:
            print('해당 아이디의 회원이 존재하지 않습니다')


    elif menu == 4: #(4. 회원정보수정)
        id = input('> 수정할 아이디 : ')
        if ms.Search_Member(id):
            pw = input('> 새 비밀번호 : ')
            name = ms.check_name()
            phone = ms.check_phone()
            address = input('> 새 주소 : ')
            ms.Change_Member(id, pw, name, phone, address)
            print('정보가 수정되었습니다.')
        else:
            print('아이디를 찾을 수 없습니다.')


    elif menu == 5: #(5. 회원탈퇴)
        id = input('> 탈퇴할 아이디 : ')
        if ms.Delete_Member(id):
            print('탈퇴 처리되었습니다.')
        else:
            print('아이디를 찾을 수 없습니다')