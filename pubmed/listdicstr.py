list1 = ['Ancistrobrevidines', 'Ancistrobreviquinones', 'Ancistrocladus abbreviatus', 'Anticancer agents', 'Naphthylisoquinoline alkaloids', 'Pancreatic cancer']
str = str(list1).replace(']','').replace('[','').replace("'", "")
print(str)