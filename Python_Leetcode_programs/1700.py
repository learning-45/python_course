class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        while(len(students)!=0):
            if(sandwiches[0] not in students):
                return(len(students))
            if(students[0]==sandwiches[0]):
                students.pop(0)
                sandwiches.pop(0)
            else:
                a=students.pop(0)
                students.append(a)
        return(len(students))

def main():
    sol = Solution()
    students   = list(map(int,input().split()))
    sandwiches = list(map(int,input().split()))
    print(sol.countStudents(students, sandwiches))

if __name__ == '__main__':
    main()
