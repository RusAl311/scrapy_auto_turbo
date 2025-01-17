# Scrapy settings for auto project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from auto import pipelines


BOT_NAME = 'auto'

SPIDER_MODULES = ['auto.spiders']
NEWSPIDER_MODULE = 'auto.spiders'

#Postgres
CONNECTION_STRING = "{drivername}://{user}:{passwd}@{host}:{port}/{db_name}".format(
    drivername = "postgresql+psycopg2",
    user = "postgres",
    # passwd = "realqiymet31",
    # host = "10.114.0.3",
    passwd = "",
    host = "localhost",
    port = "5432",
    db_name = "realqiymet"
)

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'auto (+http://www.yourdomain.com)'
USER_AGENT = [
    # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
    'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)',
    'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0',
    'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
    ]

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# RETRY_HTTP_CODES = [429]

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 2
# RANDOMIZE_DOWNLOAD_DELAY = True
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'auto.middlewares.AutoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy_proxies.RandomProxy': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
    # 'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    # 'auto.middlewares.TooManyRequestsRetryMiddleware': 543,
    # 'scrapy_cloudflare_middleware.middlewares.CloudFlareMiddleware': 560,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
    'auto.middlewares.AutoDownloaderMiddleware': 543,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#    'auto.pipelines.SaveAutosPipeline': 200,    
#    'auto.pipelines.AutoPipeline': 300,
#    'auto.pipelines.SaveSalonsPipeline': 200,
#    'auto.pipelines.SalonPipeline': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

RETRY_TIMES = 10
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 408]

# ROTATING_PROXY_LIST = [
#     'http://209.127.191.180:80',
#     'http://45.130.255.198:80',
#     'http://45.130.255.243:80',
#     'http://185.164.56.20:80',
#     'http://45.130.255.147:80',
#     'http://45.95.96.132:80',
#     'http://45.95.96.237:80',
#     'http://45.95.96.187:80',
#     'http://45.94.47.66:80',
#     'http://193.8.56.119:80'
#     # 'https://Selrustammaliyev:Y8v5HvY@193.233.30.93:45785'
# ]

PROXY_LIST = '../autos/auto/list.txt'
PROXY_MODE = 0

# http://smzrwyhr-dest:rqbu6c1p620k@209.127.191.180:80
# http://smzrwyhr-dest:rqbu6c1p620k@45.130.255.198:80
# http://smzrwyhr-dest:rqbu6c1p620k@45.130.255.243:80
# http://smzrwyhr-dest:rqbu6c1p620k@185.164.56.20:80
# http://smzrwyhr-dest:rqbu6c1p620k@45.130.255.147:80
# http://smzrwyhr-dest:rqbu6c1p620k@45.95.96.132:80
# http://smzrwyhr-dest:rqbu6c1p620k@45.95.96.237:80
# http://smzrwyhr-dest:rqbu6c1p620k@45.95.96.187:80
# http://smzrwyhr-dest:rqbu6c1p620k@45.94.47.66:80
# http://smzrwyhr-dest:rqbu6c1p620k@193.8.56.119:80


# http://209.127.191.180:80
# http://45.130.255.198:80
# http://45.130.255.243:80
# http://185.164.56.20:80
# http://45.130.255.147:80
# http://45.95.96.132:80
# http://45.95.96.237:80
# http://45.95.96.187:80
# http://45.94.47.66:80
# http://193.8.56.119:80