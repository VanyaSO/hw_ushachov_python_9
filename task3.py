
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

if start > end :
    let = start
    start = end
    end = let
    
while start <= end :
    number = int(input("Enter number in range: "))
    
    # Checking if a number is in a range
    if start <= number <= end :
        
        # Find the number that the user entered
        while start <= end : 
            if start == number :
                print(f"!{number}!", end=" ")
            else: print (start, end=" ")
            start += 1
        start += 1
