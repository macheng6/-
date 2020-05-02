#coding:utf8
import os
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)


    def output_text(self, data, path_):
        output_filename = data["title"]
        fout = open(path_ + '/' + output_filename +".txt", "w", encoding='utf-8')
        #fout = open(path_ + "/output" + str(i) + ".txt", "w", encoding='utf-8')
        # write()函数的参数是str
        #fout.write(data["url"])
        #fout.write(data["title"])
        fout.write(data["summary"])
        fout.close()


    def output_html(self):
        fout = open("output.html", "w", encoding='utf-8')
        fout.write("<html>")
        fout.write("<meta charset='utf-8'>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td width='25%%'>%s</td>" % data["url"])
            fout.write("<td width='5%%'>%s</td>" % data["title"])
            fout.write("<td width='70%%'>%s</td>" % data["summary"])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()