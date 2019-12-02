import requests, json, re

url = ''
headers = {
':authority':'esf.fang.com',
':method':'GET',
':path':'/',
':scheme':'https',
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9',
'cache-control':'no-cache',
'cookie':'global_cookie=7cqec1pxgsavzddt9rnb2v6xl18k3e7s5tt; Integrateactivity=notincludemc; __utmz=147393320.1574673229.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=147393320.1144127057.1574673229.1574673229.1574755455.2; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; lastscanpage=0; resourceDetail=1; token=59c66a51681142018630f1745e1e739f; unique_cookie=U_yc551nxo9to0q9u2cb2a7pj3l1kk3fkvdpx*1; g_sourcepage=esf_fy%5Elb_pc; city=www; __utmc=147393320; __utmb=147393320.12.10.1574755455; csrfToken=FkyVjmG4MtwA1XN2J0TtoLI6',
'pragma':'no-cache',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400',
}