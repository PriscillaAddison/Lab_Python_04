groceries = ['bananas','strawberries','apples','bread']
groceries.append('champagne')
print groceries
print' '
print '.................................................'
print' '

groceries.remove('bread')
print groceries
print' '
print '.................................................'
print' '

groc_list={'bananas':'b','strawberries':'s','apples':'a','champagne':'c'}
for fruit in groc_list:
    print fruit,groc_list[fruit]
print' '
print '.................................................'
print' '

stuff={'apples      ':'7.3','bananas     ':'5.5','breads      ':'1.0','carrots     ':'10.0','champagne   ':'20.9','strawberries':'32.6'}
print 'Item','        ','Price'
print '----------------------'
stuff['chicken     ']='6.5'
for item in stuff:

    print item,'',stuff[item]
print'------------------------'


in_stock=['apples','bananas','bread','carrots','champagne','strawberries']
print'This is the list of items in Shoprite: '
for i in in_stock:
    print i
print ' '
always_in_stock=('apples','bananas','bread','carrots','champagne','strawberries')
print'"Come to Shoprite! We always sell:"'
for s in always_in_stock:
    print s




