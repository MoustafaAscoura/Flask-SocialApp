class Config:
    @staticmethod
    def init_app():
        pass

class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI= "sqlite:///project.sqlite"

class ProdConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI= "postgresql://flask_products:12345@localhost:5432/flaskproducts"

projectConfig={
    "dev": DevConfig,
    'prd': ProdConfig
}