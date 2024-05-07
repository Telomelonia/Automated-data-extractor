import pandas as pd

def bifurcate_urls(urls):
    html_urls = []
    pdf_urls = []
    
    for url in urls:
        if 'pdf' in url:
            pdf_urls.append(url)
        else:
            html_urls.append(url)
    
    return html_urls, pdf_urls
df304 = pd.read_csv('ss304.csv')
df304l = pd.read_csv('ss304l.csv')
df310 = pd.read_csv('ss310.csv')
df316 = pd.read_csv('ss316.csv')
df316l = pd.read_csv('ss316l.csv')
df410 = pd.read_csv('ss410.csv')
df430 = pd.read_csv('ss430.csv')
url304 = list(df304['ArticleURL'])
url304l = list(df304l['ArticleURL'])
url310 = list(df310['ArticleURL'])
url316 = list(df316['ArticleURL'])
url316l = list(df316l['ArticleURL'])
url410 = list(df410['ArticleURL'])
url430 = list(df430['ArticleURL'])

htmlurl304, pdfurl304 = bifurcate_urls(url304)
htmlurl304l, pdfurl304l = bifurcate_urls(url304l)
htmlurl310, pdfurl310 = bifurcate_urls(url310)
htmlurl316, pdfurl316 = bifurcate_urls(url316)
htmlurl316l, pdfurl316l = bifurcate_urls(url316l)
htmlurl410, pdfurl410 = bifurcate_urls(url410)
htmlurl430, pdfurl430 = bifurcate_urls(url430)

url_dict = {
    "htmlurl304": htmlurl304,
    "htmlurl304l": htmlurl304l,
    "htmlurl310": htmlurl310,
    "htmlurl316": htmlurl316,
    "htmlurl316l": htmlurl316l,
    "htmlurl410": htmlurl410,
    "htmlurl430": htmlurl430
}

for key, urls in url_dict.items():
    output_file = f"{key}_output.txt"
    with open(output_file, "w", encoding='utf-8') as file:
        for url in urls:
            text = url_opener(url)
            if text:
                file.write(f"URL: {url}\n{text}\n")
                file.write("--------------------------------------------------\n")
            else:
                file.write(f"URL: {url} - Failed to process.\n")
                file.write("--------------------------------------------------\n")