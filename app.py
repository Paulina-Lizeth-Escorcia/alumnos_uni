import web #pip install web.py
urls = (
    '/alumnos/?','aplication.controllers.alumnos.Alumnos'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = True
    app.run()