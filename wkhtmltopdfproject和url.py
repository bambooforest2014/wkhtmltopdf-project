# 导入库
import pdfkit

'''将网页url生成pdf文件'''
def url_to_pdf(url, to_file):
    # 将wkhtmltopdf.exe程序绝对路径传入config对象
    path_wkthmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    # 生成pdf文件，to_file为文件路径
    pdfkit.from_url(url,to_file, configuration=config)
    print('完成')

# 这里传入我知乎专栏文章url，转换为pdf
url_to_pdf(r'https://zhuanlan.zhihu.com/p/69869004', 'out_1.pdf')