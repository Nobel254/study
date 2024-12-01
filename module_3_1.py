def count_calls(call):
    global calls
    calls=calls+1
    return calls

def string_info(string_info_):
    count_calls(0)
    isk_info = []
    up_ = str(string_info_)
    length_ = len(string_info_)
    isk_info.append(length_)
    up_ = up_.upper()
    isk_info.append(up_)
    lower_ = up_.lower()
    isk_info.append(lower_)
    isk_info_ = tuple(isk_info)
    return isk_info_

def is_contains(string_info1,string_info2):
    count_calls(0)
    string_info_lower1 = string_info1.lower()
    string_info_lower2 = str(string_info2)
    string_info_lower2 = string_info_lower2.lower()
    ets=string_info_lower1 in string_info_lower2
    return ets

calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)