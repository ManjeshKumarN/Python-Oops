class student:
    rno=123
    name="abc"
    branch="csc"

    def read(self):
        rno=345
        print("instance variable",self.branch)
        print("reading",rno)
        
    def write(self,fg):
        print("writing",fg)

abc = student() # object creation
df=student() 

if __name__=="__main__":
    print("r_no",abc.rno)
    print("name",abc.name)
    #abc.read(sd="hg")
    abc.write(fg=student.branch)
    abc.write(fg=student.branch)
    abc.read()
    #student.read() # throws error
    df.write(fg="rt")

    print(student.rno)