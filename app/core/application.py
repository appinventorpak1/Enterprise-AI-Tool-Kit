from app.config.settings import APP_NAME, APP_VERSION


class Application:
    def start(self):
        print("=" * 60)
        print(APP_NAME)
        print(f"Version : {APP_VERSION}")
        print("=" * 60)
        print("Application Started Successfully")