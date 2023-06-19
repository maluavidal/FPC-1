camila = int(input())
cibele = int(input())
celeste = int(input())

youngest = cibele
oldest = camila
if cibele > camila:
    oldest = cibele
    youngest = camila
if celeste < youngest:
    middle_child = youngest
elif celeste > oldest:
    middle_child = oldest
else:
    middle_child = celeste

print(middle_child)
