from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import requests
import re
import os




'''
uid=''
pas=''
ip=''
port=''
proxy = 'http://%s:%s@%s:%s' % (uid,pas,ip,port)


os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
'''



def download(link,_path):    
    try:
        book_name = link.split('/')[-1]
        with open(_path, 'wb') as book:
            a = requests.get(link, stream=True)

            for block in a.iter_content(512):
                if not block:
                    break

                book.write(block)
    except:
        print '***error downloading paper***'





def convert(fname, pages=None):
    try:
        if not pages:
            pagenums = set()
        else:
            pagenums = set(pages)

        output = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)

        infile = file(fname, 'rb')
        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        output.close
        return text
    except:
        print '***error converting paper ***'







if __name__ == "__main__":


    print 'System Initialized...'

    url={'a1':'http://papers.nips.cc/paper/3330-distributed-inference-for-latent-dirichlet-allocation.pdf','a2':'http://papers.nips.cc/paper/3902-online-learning-for-latent-dirichlet-allocation.pdf'}

    for i in url:
        try:
            print '\n\ndownloading paper %s' % (i)
            _path= '%s.pdf' % (i)
            download(url[i],_path)
            print 'converting paper %s' % (i)
            print '\nABSTRACT:'
            text=convert(_path,[0])
            text = re.sub('\n', '', text)
            text=text.decode('unicode_escape').encode('ascii','ignore')   
            text=re.findall(r'Abstract(.*?)Introduction',text,re.IGNORECASE)
            print text[0]
        except:
            pass
