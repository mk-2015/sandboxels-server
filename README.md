# sandboxels-server
Host your own sandboxels server!

## Install & Run
- Install:
```bash
git clone https://github.com/mk-2015/sandboxels-server box && cd box
```

- Configure:
```bash
cd server
vim config.json # Or neovim
chmod +x ./update.sh ./update-ssl.sh # MacOs or Linux (Any)
./update.sh
./update-ssl.sh
```

- Install dependincies:
```bash
cd .. && python -mvenv .venv && cd server
pip install -r requirements.txt
```

- Run:
```bash
source ../.venv/bin/activate
python server.py
```