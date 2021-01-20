laptop = {
    'brand':'MacBook',
    'os':'Mac-OS',
}
mobile = {
    'brand':'iphone',
    'os':'IOS',
}
apple = {
    'laptop':laptop,
    'mobile':mobile

}
print('Apple Products:')
for x in apple.items():
    print(x)
