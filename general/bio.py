def calculate(numRows, step, members, fecundity):
    ageClasses = [x * step for x in range(numRows)]
    lx = survivorship(members)
    lxmx = [a * b for a,b in zip(lx,fecundity)]
    r0 = sum(lxmx)
    generationTime = genTime(ageClasses, r0, lxmx)
    print("Survivorship values: ", lx[0:numRows])
    print("Net Growth Rate R0:", r0)
    print("Generation Time T: ", generationTime)

def survivorship(members):
    init = members[0]
    return [x / init for x in members]
    
def genTime(ages, r, xs):
    ys = [a * b for a,b in zip(ages, xs)]
    ret = sum(ys)/r
    return ret

def main():
    print("Enter the number of age classes")
    numClasses = int(input())
    print("Enter the age class step")
    ageStep = int(input())
    print("Enter cohort population values")
    membersAtAge = [int(x) for x in input().split()]
    print("Enter fecundity values")
    fecundity = [int(x) for x in input().split()]
    calculate(numClasses, ageStep, membersAtAge, fecundity)

if __name__ == "__main__":
    main()
