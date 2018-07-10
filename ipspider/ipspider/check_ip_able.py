import urllib
import urllib.request
import time


def validateIp(host, port):
    # 头文件
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}
    proxy = {'http': 'http://%s:%s' % (host, port)}

    # 代理设置
    proxy_handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)

    # 请求网址
    validateUrl = 'https://www.baidu.com'
    req = urllib.request.Request(url=validateUrl, headers=headers)
    # 延时,等待反馈结果
    time.sleep(4)

    # 判断结果
    try:
        res = urllib.request.urlopen(req)
        # 延时,等待反馈结果
        time.sleep(2)
        content = res.read()
        # 验证成功返回
        if content:
            msg = 200
            return msg
        else:
            msg = 500
            return msg
    except urllib.request.URLError as e:
        msg = 500
        return msg
