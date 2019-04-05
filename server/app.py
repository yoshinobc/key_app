from server import create_app

application = create_app()

if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("localhost",80000,application)
    httpd.serve_forever()
