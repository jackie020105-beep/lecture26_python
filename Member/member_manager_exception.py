class Member:
    def __init__(self, num, id, pw, name, phone, address):
        self.__num = num
        self.__id = id
        self.__pw = pw
        self.__name = name
        self.__phone = phone
        self.__address = address

    def __str__(self):
        return f' 회원번호: {self.__num}\t 아이디: {self.__id}\t 비밀번호: {self.__pw}\t 이름: {self.__name}\t 전화번호: {self.__phone}\t 주소: {self.__address}'

    def get_num(self):
        return self.__num
    def get_id(self):
        return self.__id
    def get_pw(self):
        return self.__pw
    def get_name(self):
        return self.__name
    def get_phone(self):
        return self.__phone
    def get_address(self):
        return self.__address


class MemberService:
    def __init__(self):
        self.__Member_list = []

    def list_account(self):
        return self.__Member_list

    # 1. 회원가입
    def Create_Member(self, num, id, pw, name, phone, address):
        member = Member(num, id, pw, name, phone, address)
        self.__Member_list.append(member)
        return True

    # 회원번호 예외처리    
    def check_num(self):
        while True:
            try:
                num = int(input('> 회원번호 : '))
                return num
            except ValueError:
                print('[오류] 숫자로만 입력하시오')
        
    # 전화번호 예외처리  
    def check_phone(self):
        while True:
            try:
                phone = int(input('> 전화번호 : '))
                return phone
            except ValueError:
                print('[오류] 숫자로만 입력하시오')

    # 이름 예외처리  
    def check_name(self):
        while True:
            try:
                name = input('> 이름 : ')
                if name.isdigit():
                    raise Exception
                return name
            except Exception:
                print('[오류] 문자로만 입력하시오')


    # 2. 회원목록
    def Get_Member_list(self):
        return self.__Member_list
    

    # 3. 회원상세정보
    def Search_Member(self, id):
        for member in self.__Member_list:
            if member.get_id() == id:
                return member
        return None
    
    
    # 4. 회원정보수정
    def Change_Member(self, id, pw, name, phone, address):
        member = self.Search_Member(id)
        if member:
            mlst = self.__Member_list.index(member)
            num = member.get_num()
            self.__Member_list[mlst] = Member(num, id, pw, name, phone, address)
            return True
        return False
        

    # 5. 회원탈퇴
    def Delete_Member(self, id):
        member = self.Search_Member(id)
        if member:
            self.__Member_list.remove(member)
            return True
        return False
    

# 회원 관리 메인 UI 및 로직 제어
def select_menu():
    while True:
        print('===========================================================================================')
        print('1. 회원가입 | 2. 회원목록 | 3. 회원상세정보 | 4. 회원정보수정 | 5. 회원탈퇴 | 0. 시스템종료')
        print('===========================================================================================')
        # 메뉴 입력받기
        try:
            menu = int(input('>>메뉴 선택 : '))
            if not (0 <= menu <= 5):
                raise Exception
            return menu
        except Exception:
            print('=========================[오류] 0 ~ 5까지의 숫자로만 입력하시오=========================')
    

aservice = MemberService()


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
        num = aservice.check_num()
        # 아이디 입력
        id = input('> 아이디 : ')
        # 비밀번호 입력
        pw = input('> 비밀번호 : ')
        # 이름 입력
        name = aservice.check_name()
        # 전화전호 입력
        phone = aservice.check_phone()
        # 주소 입력
        address = input('> 주소 : ')

        if aservice.Create_Member(num, id, pw, name, phone, address):
            print('====================================계정 생성되었습니다====================================')

    elif menu == 2: #(2. 회원목록)
        Member_list = aservice.Get_Member_list()
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
        member = aservice.Search_Member(id)
        if member:
            print(f'{member}')
        else:
            print('해당 아이디의 회원이 존재하지 않습니다')


    elif menu == 4: #(4. 회원정보수정)
        id = input('> 수정할 아이디 : ')
        if aservice.Search_Member(id):
            pw = input('> 새 비밀번호 : ')
            name = aservice.check_name()
            phone = aservice.check_phone()
            address = input('> 새 주소 : ')
            aservice.Change_Member(id, pw, name, phone, address)
            print('정보가 수정되었습니다.')
        else:
            print('아이디를 찾을 수 없습니다.')


    elif menu == 5: #(5. 회원탈퇴)
        id = input('> 탈퇴할 아이디 : ')
        if aservice.Delete_Member(id):
            print('탈퇴 처리되었습니다.')
        else:
            print('아이디를 찾을 수 없습니다')