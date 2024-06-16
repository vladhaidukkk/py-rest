from pydantic import BaseModel, PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000
    reload: bool = True


class ApiConfig(BaseModel):
    prefix: str = "/api"


class DatabaseConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 5432
    username: str = "postgres"
    password: str = ""
    name: str

    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 5
    max_overflow: int = 10

    @computed_field  # type: ignore[misc]
    @property
    def url(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            host=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            path=self.name,
        )


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiConfig = ApiConfig()
    db: DatabaseConfig

    model_config = SettingsConfigDict(
        env_prefix="APP__",
        env_nested_delimiter="__",
        extra="ignore",
    )


settings = Settings(_env_file=(".env.example", ".env"))  # type: ignore[call-arg]
