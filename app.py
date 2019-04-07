from server import create_app

application = create_app()

if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("192.168.0.36",9000,application)
    print("run server")
    httpd.serve_forever()
