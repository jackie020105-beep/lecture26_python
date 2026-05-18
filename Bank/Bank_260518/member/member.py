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
    