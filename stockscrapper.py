from requests_html import HTML, HTMLSession


def scrape():
    session = HTMLSession()
    dict_of_data = {}

    for j in range(1, 12):
        r = session.get(f'http://nepalstock.com/main/todays_price/index/{j}/')
        r.html.render(timeout=20)

        table = r.html.find('tbody', first=True)
        try:
            for i in range(2, 22):
                datas = table.find('tr')[i]

                data = datas.find('td')
                list_of_stocks = []
                for elements in data:
                    elements = elements.text
                    list_of_stocks.append(elements)

                name = list_of_stocks[1].upper()

                if "LTD." in name:
                    name = name.replace("LTD.","LIMITED")
                if "LTD" in name:
                    name = name.replace("LTD","LIMITED")
                if "CO." in name:
                    name = name.replace("CO.","COMPANY")
                if "'" in name:
                    name = name.replace("'","")
                
                dict_of_data[name] = {
                    'closing_price': list_of_stocks[5], 'difference': list_of_stocks[-1]}
        except Exception as e:
            print(e,"Ignored")
           

    return dict_of_data


if __name__ == "__main__":
    print(scrape())
