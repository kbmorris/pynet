houston_dc = ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4', '5.5.5.5', '6.6.6.6', '7.7.7.7', '8.8.8.8', '9.9.9.9', '10.10.10.10']
atlanta_dc = ['1.1.1.2', '2.2.2.3', '3.3.3.4', '4.4.4.4', '5.5.5.6', '6.6.6.6', '7.7.7.8', '8.8.8.9']
chicago_dc = ['1.1.1.1', '2.2.2.3', '3.3.3.5', '4.4.4.5', '5.5.5.6', '6.6.6.6', '7.7.7.9', '8.8.8.8']

houston_set = set(houston_dc)
atlanta_set = set(atlanta_dc)
chicago_set = set(chicago_dc)

print(f"Houston and Atlanta overlap: {houston_set.intersection(atlanta_set)}")
print(f"Houston, Chicago and Atlanta overlap: {houston_set.intersection(atlanta_set).intersection(chicago_set)}")
print(f"Chicago Uniques: {chicago_set.difference(houston_set).difference(atlanta_set)}")
