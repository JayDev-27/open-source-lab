"""Parses .env files into dict."""
def load_dotenv(content: str):
    env = {}
    for line in content.splitlines():
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            k, v = line.split('=', 1)
            env[k.strip()] = v.strip().strip('"\'')
    return env
