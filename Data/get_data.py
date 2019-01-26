import yaml
def get_data():
    data_list = []
    with open("E:\\就业班\\20190125\\me\\app_code09_4\\Data\\search_text.yml", "r",encoding='utf-8') as f:
        data = yaml.load(f)
        for i in data.get("test_data").values():
            data_list.append((i.get('key'),i.get('value')))
    return data_list


# print(get_data())




