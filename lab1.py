from functools import reduce

C_temp = [25, 0, 10, -5, 30, 15, -2]

katu_nuktesi = list(filter(lambda f: f < 32, map(lambda c: c * 9/5 + 32, C_temp)))

katu_nuktesi_ort = reduce(lambda x, y: x + y, katu_nuktesi) / len(katu_nuktesi)

print("Фарангейт температурасы:", list(map(lambda c: c * 9/5 + 32, C_temp)))
print("Қату нүктесінен төмен мәндер:", katu_nuktesi)
print("Орташа мәні:", katu_nuktesi_ort)
