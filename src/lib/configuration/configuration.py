import os

env_var = {
    # Si le serveur est en production ou en dev
    "prod": False,

    # si j'affiche ou pas les informations de log
    "debug": True,

    # Authentification
    "jwts.private.key": "3lZQWfP+tFphA3LlIzGQU8CVCkHMqzcDAX56BxfZub/RMWAjm3bxgebqtvw4HbGqw1+UXXl5hF5/2Oi4Fv2UYA==",
    "jwts.private.key.prod": "3lZQWfP+tFphA3LlIzGQU8CVCkHMqzcDAX56BxfZub/RMWAjm3bxgebqtvw4HbGqw1+UXXl5hF5/2Oi4Fv2UYA==",

    # Database
    "database.dynamodb.endpoint": "http://localhost:8000",
    "database.dynamodb.table.account": "mini-blog-iam-dev",
    "database.dynamodb.table.account.prod": "mini-blog-iam-prod",

    # Storage: S3 (MinIO on local)
    "storage.s3.endpoint": "http://localhost:9000",

}

# eu-central-1


def is_prod() -> bool:
    try:
        return bool(os.environ.get("prod", env_var["prod"]))
    except KeyError as e:
        print(e)
        return False
    except Exception as e:
        print(e)
        raise e


def is_debug() -> bool:
    try:
        return bool(os.environ.get("debug", env_var["debug"]))
    except KeyError as e:
        print(e)
        return True
    except Exception as e:
        print(e)
        raise e


def get_configuration(key):
    key_conf = key
    if is_prod():
        key_conf += ".prod"
    try:
        return os.environ.get(key_conf, env_var[key_conf])
    except KeyError as e:
        print(e)
        try:
            if is_prod():
                return os.environ.get(key, env_var[key])
            return None
        except KeyError as e2:
            print(e2)
            return None


if __name__ == '__main__':
    name_config = "database.dynamodb.table.account"

    value_config = get_configuration(name_config)
    print(f"name: {name_config} --- value: {value_config}")
