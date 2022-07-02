class ArrayQueue:
    
    DEFAULT_CAPACITY=int(input("몇개의 숫자를 입력 하시겠습니까? ")) 
    # 입력받은 숫자만큼 self._data의 None의 개수를 정하기 위해 10대신 변경하였습니다.

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front]=None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def _resize(self, n):
        old = self._data
        self._data = [None] * n
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0    
    
    def rotate(self): #rotate 매소드 / self._data.append(self._data.pop(0))도 가능
        first_num = self._data[0] #리스트 첫번째 값 저장
        for i in range(1, len(self._data)):#리스트 마지막 값을 제외하고 앞으로 한칸씩 땡겨주기
            self._data[i-1]=self._data[i]
        X = len(self._data)-1 
        self._data[X]=first_num #리스트 마지막 인덱스에 첫번째값을 넣어주기
        
Q=ArrayQueue() #Q 인스턴스 생성
for i in range(Q.DEFAULT_CAPACITY): # DEFAULT_CAPACITY횟수만큼 숫자 입력하기
    num = int(input(">>"))
    Q.enqueue(num) #enqueue 메소드로 숫자를 추가하여 Before Rotation 만들기

print("Before Rotation:",Q._data) 
Q.rotate() 
print("After Rotation",Q._data)

"""
여러번 반복해도 문제없이 작동합니다.
Q.rotate()
print("After Rotation2",Q._data)
Q.rotate()
print("After Rotation3",Q._data)
Q.rotate()
print("After Rotation4",Q._data)
"""
