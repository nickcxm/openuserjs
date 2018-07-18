from scrapy import cmdline

name='userjs'
cmd='scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())