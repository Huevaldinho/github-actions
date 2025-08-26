from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings, loaded from environment variables or a .env file.

    Looks for variables prefixed with 'APP__'.
    e.g. APP__HOST, APP__PORT
    """
    model_config = SettingsConfigDict(
        env_prefix='APP__',
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
    )

    host: str
    port: int
