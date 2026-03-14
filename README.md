# 🔐 Repo Secret Finder 🔎

I wanted a lightweight way to scan my repositories for potential secret leaks without relying on tools like GitLeaks.

This project is a small scanner that detects common secrets in your codebase so you can catch leaks locally before they reach CI or GitHub security scans.

Detects:

- API keys (AWS, OpenAI, Stripe, GitHub tokens, generic key assignments)
- `.env` files committed to the repository
- Private keys (`.pem`, `.key`, `.p12`, `.pfx` files and key content markers)
- Secret files with overly permissive file permissions
- Missing `.gitignore` files
- Debug print statements, `breakpoint()` calls, and `pdb` usage
- Subprocess calls with `shell=True` (shell injection risk)
- Database connection strings with embedded credentials (PostgreSQL, MySQL, MongoDB, Redis, MSSQL, and ADO.NET-style strings)

## Example

```
$ python main.py /path/to/your/repo

⚠ Possible AWS key in config/settings.py
⚠ .env file detected
✔ No private keys found
```

## Install

```bash
git clone https://github.com/tdiprima/Secret-Leak-Finder.git
cd Secret-Leak-Finder
```

No external dependencies required — uses the Python standard library only.

## Usage

```bash
python main.py /path/to/your/repo
```
