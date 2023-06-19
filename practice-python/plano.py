monthly_quota = int(input())
months = int(input())
used_mb = 0

for _ in range(months):
    used_mb += int(input())

total_mb = (months + 1) * monthly_quota
available_mb = total_mb - used_mb

print(available_mb)