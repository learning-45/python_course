class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        for sandwich in sandwiches:
            if sandwich in students:
                students.remove(sandwich)
            else:
                break
        return len(students)

def main():
    sol = Solution()
    students   = list(map(int,input().split()))
    sandwiches = list(map(int,input().split()))
    print(sol.countStudents(students, sandwiches))

if __name__ == '__main__':
    main()
