def main(path_to_excel, column_name, search_attribute, path_to_driver, num_images):
    wd = webdriver.Chrome(executable_path=path_to_driver)
    df = pd.read_excel(path_to_excel)
    key = df[column_name]
    key = key+' '+str(search_attribute)
    key = list(pd.Series(key).dropna())
    for i in key:
        search_term = str(i)
        print(i)
        try:
            search_and_download(search_term = search_term, driver_path = path_to_driver, number_images = num_images)
        except:
            pass

