def calculate_result():
    print("--- Student Result Calculator ---")
    
    # Get marks for 3 subjects
    math = float(input("Enter Math marks: "))
    science = float(input("Enter Science marks: "))
    english = float(input("Enter English marks: "))
    
    # Calculate total and percentage
    total = math + science + english
    percentage = (total / 300) * 100
    
    print(f"\nTotal Marks: {total} / 300")
    print(f"Percentage: {percentage:.2f}%")
    
    # Check Pass or Fail
    if percentage >= 35:
        print("Result: PASS ✅")
    else:
        print("Result: FAIL ❌")

calculate_result()
