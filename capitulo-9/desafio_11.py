with open('anajulia.txt', 'r', encoding='utf-8') as file:
    conta_anna = 0
    for linha in file.readlines():
        if 'Anna' in linha:
            conta_anna += 1

print(conta_anna)

# with open('anajulia.txt', 'r', encoding='utf-8') as file:
#     conta_anna = []
#     for linha in file.readlines():
#         if 'Anna' in linha:
#             conta_anna.append(linha)
#
# print(len(conta_anna))
