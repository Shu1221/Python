name = input('あなたの名前を教えて下さい >>')
print(f'{name}さんこんにちは')
food = input(f'{name}さんの好きな食べ物を教えて下さい >>')
if 'カレー' in food:
    print('素敵です。カレーは最高ですよね!!')
else:
    print(f'私も{food}が好きですよ')
