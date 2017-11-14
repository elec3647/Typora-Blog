from tornado import web, gen, escape
from tornado.options import options


class PageNotFoundHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('error.html', code='404')

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('error.html', code='404')
        else:
            self.render('error.html', code='500')


class IndexHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('index.html', page_num=int((len(options.config['posts']) + 4) / options.config['paging']))

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('error.html', code='404')
        else:
            self.render('error.html', code='500')


class PostsHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        current_page = abs(int(self.get_argument('page', 1)))
        total_page = int((len(options.config['posts']) + 4) / options.config['paging'])
        if current_page < total_page:
            posts = options.config['posts'][(current_page - 1) * options.config['paging']:
                                            current_page * options.config['paging']]
        elif current_page == total_page:
            posts = options.config['posts'][(current_page - 1) * options.config['paging']:
                                            len(options.config['posts'])]
        else:
            posts = []
        respon_json = escape.json_encode(posts)
        self.write(respon_json)

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('error.html', code='404')
        else:
            self.render('error.html', code='500')


class PostHandler(web.RequestHandler):
    @gen.coroutine
    def get(self, url):
        found_post = False
        for post in options.config['posts']:
            if url == post['id']:
                found_post = True
                break
        if found_post:
            self.render('post/' + post['title'] +
                        '.html', timestamp=post['timestamp'])
        else:
            self.render('error.html', code='404')

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('error.html', code='404')
        else:
            self.render('error.html', code='500')


class AchiveHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('achive.html', posts=options.config['posts'])

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('error.html', code='404')
        else:
            self.render('error.html', code='500')


class ShareHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('share.html')

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('error.html', code='404')
        else:
            self.render('error.html', code='500')


class ProductHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('product.html')

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('error.html', code='404')
        else:
            self.render('error.html', code='500')


class LinkHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('link.html')

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('error.html', code='404')
        else:
            self.render('error.html', code='500')


class AboutHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('about.html')

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('error.html', code='404')
        else:
            self.render('error.html', code='500')
