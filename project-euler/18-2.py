print("Enter the pyramid numbers line by line. Finish with an empty line:")
triangle = []

while True:
    line = input()
    if line.strip() == "":
        break
    # Convert space-separated numbers to integers
    nums = list(map(int, line.strip().split()))
    triangle.append(nums)

# Display the parsed triangle
print("triangle = [")
for row in triangle:
    print(f"   {row},")
print("]")
print("]")

