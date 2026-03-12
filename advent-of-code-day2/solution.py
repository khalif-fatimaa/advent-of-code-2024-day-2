def is_safe(report):
    nums = [int(x) for x in report.split()]
    
    diffs = []
    for i in range(len(nums) - 1):
        diffs.append(nums[i+1] - nums[i])
    
    increasing = all(1 <= d <= 3 for d in diffs)
    decreasing = all(-3 <= d <= -1 for d in diffs)
    
    return increasing or decreasing


safe_count = 0

with open("input.txt") as f:
    for line in f:
        if is_safe(line.strip()):
            safe_count += 1

print(safe_count)