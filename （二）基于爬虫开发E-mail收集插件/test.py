
import sys
sys.path.append("script")
print sys.path

if __name__ == "__main__":
    m = __import__("email_check")
    print m
    spider = getattr(m, 'spider')
    p = spider()
    url = "http://www.baidu.com"
    html = "344444@qq.com"
    s =p.run(url,html)