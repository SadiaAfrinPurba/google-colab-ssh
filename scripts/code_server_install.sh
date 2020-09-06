#!/bin/bash

curl -fsSL https://code-server.dev/install.sh | sh
echo "Code server install done!"
nohup code-server --port 9000 --auth none &