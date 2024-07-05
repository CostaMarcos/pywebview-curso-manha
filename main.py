import webview


class Curso:
    HOME = './web/index.html'
    FORM = './web/form.html'

    def __init__(self):
        self.window = None
        self.activities = [1]
    
    def new_register(self):
        self.window.load_url(self.FORM)

    def open_home(self):
        self.window.load_url(self.HOME)

    # def get_list(self):
    #     self.window.evaluate_js(f"render({self.elements})")

    def save_activity(self, activity, status): 
        self.activities.append({'activity': activity, 'status': status})

    def main(self, args):
        self.window = webview.create_window('Curso de Pywebview', self.HOME)
        self.window.expose(
            self.new_register,
            self.save_activity,
            self.open_home,
            # self.get_list
        )
        webview.start(debug=True, http_server=True, gui='qt')

if __name__ == '__main__':
    import sys
    sys.exit(Curso().main(sys.argv))