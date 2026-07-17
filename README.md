# sandboxels-server
Host your own sandboxels server!

## Install & Run
- Install:
```bash
git clone https://github.com/mk-2015/sandboxels-server box && cd box
```

- Create .venv:
```
python -mvenv .venv # use uv if preffered
source .venv/bin/activate
```

- Configure:
```bash
cd server
vim config.json # Or neovim
chmod +x ./update.sh ./update-ssl.sh # MacOs or Linux (Any)
./update.sh
./update-ssl.sh
```

- Install dependinces & run:
```bash
pip install -r requirements.txt # Use uv if preffered
python server.py # use uv run if preffered
```