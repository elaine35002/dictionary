# dctiontary

words = {
    
    'raman': '拉麵',   # 左邊單字是key 右邊是value
    'pasta': '義大利麵'
}
words['tea'] = '茶'  #增加新的key
print(words)

#字典與清單混用
p0 = {
    'name': '麥香奶茶',
    'price': '10'
}

p1 = {
    'name': '珍珠奶茶',
    'price': '60'
}

drinks = [p0, p1]  
print(drinks[0]['name'])
print(drinks[1]['price'])