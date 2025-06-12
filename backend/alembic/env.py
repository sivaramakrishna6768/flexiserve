from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys

# Add app folder to sys.path to resolve imports properly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Load your models so Alembic can detect them
from app.database import Base
from app.models import user  # This makes sure User model is registered

# Load DB URL from env
config = context.config
config.set_main_option("sqlalchemy.url", os.environ.get("DATABASE_URL"))

# Logging setup
fileConfig(config.config_file_name)

# Assign target_metadata for autogeneration
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
